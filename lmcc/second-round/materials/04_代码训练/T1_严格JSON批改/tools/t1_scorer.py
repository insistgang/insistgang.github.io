#!/usr/bin/env python3
"""Score T1-style raw model output against answer files kept outside exercises/."""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    # Package import: used by unit tests from the training-pack root.
    from tools.t1_validator import validate_raw_output
except ModuleNotFoundError:
    # Direct script execution from the tools directory.
    from t1_validator import validate_raw_output


@dataclass
class ScoreResult:
    total_items: int
    correct_items: int
    invalid_records: int


def score_records(
    output_records: list[dict[str, Any]],
    expected_by_student: dict[str, list[bool]],
) -> ScoreResult:
    """Score valid outputs item by item; invalid output earns zero for that student."""
    outputs = {record.get("student_id"): record for record in output_records}
    correct_items = 0
    invalid_records = 0

    for student_id, expected in expected_by_student.items():
        record = outputs.get(student_id)
        if record is None:
            invalid_records += 1
            continue
        result = validate_raw_output(
            record.get("raw_output"),
            expected_student_id=student_id,
            expected_count=len(expected),
        )
        if not result.valid:
            invalid_records += 1
            continue
        actual = result.parsed["judgements"]
        correct_items += sum(got == want for got, want in zip(actual, expected))

    return ScoreResult(
        total_items=sum(len(values) for values in expected_by_student.values()),
        correct_items=correct_items,
        invalid_records=invalid_records,
    )


def _read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="批量自测 T1 输出的格式与判断结果")
    parser.add_argument("--outputs", type=Path, required=True, help="你的输出 JSONL，字段：student_id、raw_output")
    parser.add_argument("--answers", type=Path, required=True, help="隐藏答案 JSONL，字段：student_id、judgements")
    args = parser.parse_args()

    for path in (args.outputs, args.answers):
        if not path.is_file():
            parser.error(f"找不到文件：{path}")

    output_records = _read_jsonl(args.outputs)
    expected_by_student = {
        record["student_id"]: record["judgements"] for record in _read_jsonl(args.answers)
    }
    result = score_records(output_records, expected_by_student)
    print(
        f"得分：{result.correct_items}/{result.total_items}；"
        f"格式无效或缺失记录：{result.invalid_records}"
    )
    return 0 if result.invalid_records == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
