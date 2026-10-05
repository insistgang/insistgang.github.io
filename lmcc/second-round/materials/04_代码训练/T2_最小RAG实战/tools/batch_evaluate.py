#!/usr/bin/env python3
"""Local batch evaluator for T2 retrieval and strict JSON output training."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from tools.tiny_torch import TinyTensor, install_torch_shim
except ModuleNotFoundError:
    from tiny_torch import TinyTensor, install_torch_shim


@dataclass
class OutputValidation:
    valid: bool
    errors: list[str]


def _has_surrounding_text(text: str) -> bool:
    start = text.find("{")
    if start < 0:
        return False
    try:
        _, end = json.JSONDecoder().raw_decode(text[start:])
    except json.JSONDecodeError:
        return False
    return bool(text[:start].strip() or text[start + end :].strip())


def validate_raw_answer_output(raw_output: str, *, expected_answer: str) -> OutputValidation:
    """Require one JSON object with string reasoning and numeric string answer."""
    if not isinstance(raw_output, str):
        return OutputValidation(False, ["raw_output 必须是字符串"])
    text = raw_output.strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        error = "存在 JSON 外的多余文本" if _has_surrounding_text(text) else "不是有效 JSON"
        return OutputValidation(False, [error])
    if not isinstance(parsed, dict):
        return OutputValidation(False, ["顶层必须是 JSON 对象"])

    errors: list[str] = []
    if not isinstance(parsed.get("reasoning"), str) or not parsed["reasoning"].strip():
        errors.append("reasoning 必须是非空字符串")
    answer = parsed.get("answer")
    if not isinstance(answer, str):
        errors.append("answer 必须是字符串")
    else:
        if answer.strip() != answer or not re.fullmatch(r"-?\d+(?:\.\d+)?", answer):
            errors.append("answer 必须只包含数字")
        elif answer != expected_answer:
            errors.append("answer 与期望答案不一致")
    return OutputValidation(not errors, errors)


def mock_embedding(text: str, _model=None, _tokenizer=None, *, dimensions: int = 64) -> TinyTensor:
    """Deterministic character/token hashing for offline pipeline practice only."""
    vector = [0.0] * dimensions
    tokens = re.findall(r"[A-Za-z]+|\d+|[\u4e00-\u9fff]", text.lower())
    for token in tokens:
        index = int(hashlib.sha256(token.encode("utf-8")).hexdigest()[:8], 16) % dimensions
        vector[index] += 1.0
    return TinyTensor(vector)


def load_submission(path: Path):
    try:
        import torch  # noqa: F401
    except ModuleNotFoundError:
        install_torch_shim()
    spec = importlib.util.spec_from_file_location("t2_user_submission", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"无法加载 submission：{path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def evaluate_retrieval(
    submission,
    problem_bank: list[dict[str, Any]],
    tests: list[dict[str, Any]],
    expected: dict[str, dict[str, Any]],
) -> tuple[int, int, list[str]]:
    correct = 0
    messages: list[str] = []
    for item in tests:
        retrieved = submission.retrieve_relevant_problems(
            item["problem"],
            problem_bank,
            embedding_model=None,
            tokenizer=None,
            top_k=3,
            get_embedding_func=mock_embedding,
        )
        wanted = expected[item["id"]]["expected_top_id"]
        got = retrieved[0]["id"] if retrieved else None
        user_message = submission.build_user_message(item["problem"], retrieved)
        if got == wanted and item["problem"] in user_message:
            correct += 1
        else:
            messages.append(f"{item['id']}: 期望 Top-1={wanted}，实际={got}")
    return correct, len(tests), messages


def main() -> int:
    parser = argparse.ArgumentParser(description="本地验证 T2 的 retrieval、RAG 消息与 JSON 输出")
    parser.add_argument("--exercise", type=Path, required=True, help="练习目录")
    parser.add_argument("--answers", type=Path, required=True, help="隐藏答案 JSONL")
    parser.add_argument("--submission", type=Path, default=Path("standard_solution/submission.py"))
    parser.add_argument("--outputs", type=Path, help="可选：模型原始输出 JSONL，字段 id、raw_output")
    args = parser.parse_args()

    bank_path = args.exercise / "data" / "problem_bank.json"
    tests_path = args.exercise / "data" / "test_data.jsonl"
    for path in (bank_path, tests_path, args.answers, args.submission):
        if not path.is_file():
            parser.error(f"找不到文件：{path}")

    problem_bank = json.loads(bank_path.read_text(encoding="utf-8"))
    tests = read_jsonl(tests_path)
    expected = {item["id"]: item for item in read_jsonl(args.answers)}
    submission = load_submission(args.submission)
    correct, total, retrieval_errors = evaluate_retrieval(submission, problem_bank, tests, expected)
    print(f"检索与消息组装：{correct}/{total}")
    for error in retrieval_errors:
        print(f"❌ {error}")

    if args.outputs is None:
        print("未提供 --outputs；已完成 retrieval 自测，跳过模型 JSON 输出评分。")
        return 0 if correct == total else 1
    if not args.outputs.is_file():
        parser.error(f"找不到文件：{args.outputs}")

    output_map = {item["id"]: item.get("raw_output") for item in read_jsonl(args.outputs)}
    output_ok = 0
    for item in tests:
        result = validate_raw_answer_output(
            output_map.get(item["id"]),
            expected_answer=expected[item["id"]]["answer"],
        )
        if result.valid:
            output_ok += 1
        else:
            print(f"❌ {item['id']}: {'；'.join(result.errors)}")
    print(f"严格 JSON + 答案：{output_ok}/{total}")
    return 0 if correct == total and output_ok == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
