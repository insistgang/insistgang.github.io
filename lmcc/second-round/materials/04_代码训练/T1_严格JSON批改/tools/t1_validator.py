#!/usr/bin/env python3
"""Strict local validator for LMCC T1-style model output.

The 2025 official evaluator can extract JSON from surrounding text.  This
trainer is intentionally stricter: it teaches the safer exam habit of emitting
one JSON object and nothing else.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class ValidationResult:
    valid: bool
    errors: list[str]
    parsed: dict[str, Any] | None


def _has_surrounding_text(text: str) -> bool:
    """Return True when a JSON object exists but is surrounded by prose."""
    start = text.find("{")
    if start < 0:
        return False
    try:
        _, end = json.JSONDecoder().raw_decode(text[start:])
    except json.JSONDecodeError:
        return False
    return bool(text[:start].strip() or text[start + end :].strip())


def validate_raw_output(
    raw_output: str,
    *,
    expected_student_id: str | None = None,
    expected_count: int = 5,
) -> ValidationResult:
    """Validate one raw LLM output against the T1 JSON contract."""
    errors: list[str] = []
    if not isinstance(raw_output, str):
        return ValidationResult(False, ["raw_output 必须是字符串"], None)

    text = raw_output.strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        message = "存在 JSON 外的多余文本" if _has_surrounding_text(text) else "不是有效 JSON"
        return ValidationResult(False, [message], None)

    if not isinstance(parsed, dict):
        return ValidationResult(False, ["顶层必须是 JSON 对象"], None)

    for field in ("student_id", "judgements"):
        if field not in parsed:
            errors.append(f"缺少字段：{field}")

    student_id = parsed.get("student_id")
    if "student_id" in parsed and not isinstance(student_id, str):
        errors.append("student_id 必须是字符串")
    elif expected_student_id is not None and student_id != expected_student_id:
        errors.append("student_id 与输入不一致")

    judgements = parsed.get("judgements")
    if "judgements" in parsed and not isinstance(judgements, list):
        errors.append("judgements 必须是数组")
    elif isinstance(judgements, list):
        if len(judgements) != expected_count:
            errors.append(f"judgements 长度应为 {expected_count}，实际为 {len(judgements)}")
        for index, judgement in enumerate(judgements):
            if type(judgement) is not bool:
                errors.append(f"judgements[{index}] 必须是 JSON 布尔值")

    return ValidationResult(not errors, errors, parsed)


def validate_output_jsonl(path: Path, *, expected_count: int) -> list[ValidationResult]:
    """Validate records shaped as {student_id, raw_output} in a JSONL file."""
    results: list[ValidationResult] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError:
            results.append(ValidationResult(False, [f"第 {line_number} 行不是有效 JSONL 记录"], None))
            continue
        if not isinstance(record, dict):
            results.append(ValidationResult(False, [f"第 {line_number} 行必须是对象"], None))
            continue
        result = validate_raw_output(
            record.get("raw_output"),
            expected_student_id=record.get("student_id"),
            expected_count=expected_count,
        )
        if result.errors:
            result.errors[:] = [f"第 {line_number} 行：{error}" for error in result.errors]
        results.append(result)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description="校验 T1 模型输出是否为严格 JSON")
    parser.add_argument("--outputs", type=Path, required=True, help="JSONL：每行含 student_id 和 raw_output")
    parser.add_argument("--expected-count", type=int, default=5, help="每名学生应有多少个判断")
    args = parser.parse_args()

    if args.expected_count <= 0:
        parser.error("--expected-count 必须为正数")
    if not args.outputs.is_file():
        parser.error(f"找不到文件：{args.outputs}")

    results = validate_output_jsonl(args.outputs, expected_count=args.expected_count)
    failed = 0
    for index, result in enumerate(results, 1):
        if result.valid:
            print(f"第 {index} 条：✅ 结构合法")
        else:
            failed += 1
            print(f"第 {index} 条：❌ {'；'.join(result.errors)}")
    print(f"汇总：{len(results) - failed}/{len(results)} 条结构合法")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
