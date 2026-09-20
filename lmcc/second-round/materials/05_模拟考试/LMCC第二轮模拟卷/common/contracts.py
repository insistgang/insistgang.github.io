"""Strict JSON contracts modeled after the 2025 T1/T2 output shapes."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Any


@dataclass
class ValidationResult:
    valid: bool
    errors: list[str]
    parsed: dict[str, Any] | None


def _parse_exact_json(raw_output: Any) -> tuple[dict[str, Any] | None, list[str]]:
    if not isinstance(raw_output, str):
        return None, ["raw_output 必须是字符串"]
    text = raw_output.strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        if start >= 0:
            try:
                _, end = json.JSONDecoder().raw_decode(text[start:])
                if text[:start].strip() or text[start + end :].strip():
                    return None, ["存在 JSON 外的多余文本"]
            except json.JSONDecodeError:
                pass
        return None, ["不是有效 JSON"]
    if not isinstance(parsed, dict):
        return None, ["顶层必须是 JSON 对象"]
    return parsed, []


def validate_t1_output(
    raw_output: Any, *, student_id: str, expected_count: int
) -> ValidationResult:
    parsed, errors = _parse_exact_json(raw_output)
    if parsed is None:
        return ValidationResult(False, errors, None)
    for key in ("student_id", "judgements"):
        if key not in parsed:
            errors.append(f"缺少字段：{key}")
    if "student_id" in parsed:
        if not isinstance(parsed["student_id"], str):
            errors.append("student_id 必须是字符串")
        elif parsed["student_id"] != student_id:
            errors.append("student_id 与输入不一致")
    judgements = parsed.get("judgements")
    if "judgements" in parsed and not isinstance(judgements, list):
        errors.append("judgements 必须是数组")
    elif isinstance(judgements, list):
        if len(judgements) != expected_count:
            errors.append(f"judgements 长度应为 {expected_count}，实际为 {len(judgements)}")
        for index, value in enumerate(judgements):
            if type(value) is not bool:
                errors.append(f"judgements[{index}] 必须是 JSON 布尔值")
    return ValidationResult(not errors, errors, parsed)


def validate_t2_output(raw_output: Any, *, expected_answer: str) -> ValidationResult:
    parsed, errors = _parse_exact_json(raw_output)
    if parsed is None:
        return ValidationResult(False, errors, None)
    for key in ("reasoning", "answer"):
        if key not in parsed:
            errors.append(f"缺少字段：{key}")
    if "reasoning" in parsed and (
        not isinstance(parsed["reasoning"], str) or not parsed["reasoning"].strip()
    ):
        errors.append("reasoning 必须是非空字符串")
    if "answer" in parsed:
        answer = parsed["answer"]
        if not isinstance(answer, str):
            errors.append("answer 必须是字符串")
        elif answer.strip() != answer or not re.fullmatch(r"-?\d+(?:\.\d+)?", answer):
            errors.append("answer 必须只包含数字")
        elif answer != expected_answer:
            errors.append("answer 与期望答案不一致")
    return ValidationResult(not errors, errors, parsed)
