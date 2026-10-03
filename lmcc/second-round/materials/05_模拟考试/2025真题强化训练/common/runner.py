#!/usr/bin/env python3
"""Generic local evaluator for T1, T2 and combined reinforcement drills."""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any

from common.contracts import validate_t1_output, validate_t2_output
from common.tiny_torch import TinyTensor, install_torch_shim


TRAINING_ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def mock_embedding(text: str, _model=None, _tokenizer=None, *, dimensions: int = 96) -> TinyTensor:
    """Deterministic offline embedding for pipeline tests, not semantic evaluation."""
    vector = [0.0] * dimensions
    for token in re.findall(r"[A-Za-z]+|\d+|[\u4e00-\u9fff]", text.lower()):
        index = int(hashlib.sha256(token.encode("utf-8")).hexdigest()[:8], 16) % dimensions
        vector[index] += 1.0
    return TinyTensor(vector)


def load_submission(path: Path):
    try:
        import torch  # noqa: F401
    except ModuleNotFoundError:
        install_torch_shim()
    spec = importlib.util.spec_from_file_location("reinforcement_submission", path)
    if spec is None or spec.loader is None:
        raise ValueError(f"无法加载 submission：{path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def output_map(records: list[dict[str, Any]], section: str) -> dict[str, Any]:
    result = {}
    for record in records:
        if record.get("section", section) == section and "id" in record:
            result[record["id"]] = record.get("raw_output")
    return result


def _require_functions(submission, names: tuple[str, ...]) -> list[str]:
    return [name for name in names if not callable(getattr(submission, name, None))]


def evaluate_t1(
    submission,
    cases: list[dict[str, Any]],
    expected: list[dict[str, Any]],
    raw_outputs: dict[str, Any],
) -> tuple[int, int, list[str]]:
    errors: list[str] = []
    missing = _require_functions(submission, ("build_system_prompt", "build_generation_parameters"))
    if missing:
        return 0, sum(len(item["judgements"]) for item in expected), [f"缺少函数：{', '.join(missing)}"]
    prompt = submission.build_system_prompt()
    params = submission.build_generation_parameters()
    if not isinstance(prompt, str) or not prompt.strip():
        errors.append("build_system_prompt 必须返回非空字符串")
    if not isinstance(params, dict) or params.get("do_sample") is not False:
        errors.append("生成参数应显式设置 do_sample=False")

    expected_map = {item["id"]: item for item in expected}
    correct = 0
    total = 0
    for case in cases:
        answer = expected_map[case["id"]]
        judgements = answer["judgements"]
        total += len(judgements)
        result = validate_t1_output(
            raw_outputs.get(case["id"]),
            student_id=case["student_id"],
            expected_count=len(judgements),
        )
        if not result.valid:
            errors.append(f"{case['id']}: {'；'.join(result.errors)}")
            continue
        correct += sum(
            got == wanted
            for got, wanted in zip(result.parsed["judgements"], judgements)
        )
    return correct, total, errors


def evaluate_t2(
    submission,
    problem_bank: list[dict[str, Any]],
    cases: list[dict[str, Any]],
    expected: list[dict[str, Any]],
    raw_outputs: dict[str, Any],
) -> tuple[int, int, list[str], int, int]:
    errors: list[str] = []
    required = (
        "compute_similarity",
        "retrieve_relevant_problems",
        "build_user_message",
        "build_system_prompt",
        "build_generation_parameters",
    )
    missing = _require_functions(submission, required)
    if missing:
        return 0, len(cases), [f"缺少函数：{', '.join(missing)}"], 0, len(cases)
    params = submission.build_generation_parameters()
    if not isinstance(params, dict) or params.get("do_sample") is not False:
        errors.append("生成参数应显式设置 do_sample=False")

    expected_map = {item["id"]: item for item in expected}
    retrieval_correct = 0
    answer_correct = 0
    for case in cases:
        answer = expected_map[case["id"]]
        try:
            retrieved = submission.retrieve_relevant_problems(
                case["problem"],
                problem_bank,
                embedding_model=None,
                tokenizer=None,
                top_k=3,
                get_embedding_func=mock_embedding,
            )
            got = retrieved[0]["id"] if retrieved else None
            message = submission.build_user_message(case["problem"], retrieved)
            if got == answer["expected_top_id"] and case["problem"] in message:
                retrieval_correct += 1
            else:
                errors.append(
                    f"{case['id']}: 期望 Top-1={answer['expected_top_id']}，实际={got}"
                )
        except Exception as exc:
            errors.append(f"{case['id']}: 检索执行错误：{exc}")
            continue
        result = validate_t2_output(raw_outputs.get(case["id"]), expected_answer=answer["answer"])
        if result.valid:
            answer_correct += 1
        else:
            errors.append(f"{case['id']}: {'；'.join(result.errors)}")
    return retrieval_correct, len(cases), errors, answer_correct, len(cases)


def _load_scope(question_dir: Path, name: str, scope: str) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    answer_dir = TRAINING_ROOT / "answers" / question_dir.name
    public_cases = read_jsonl(question_dir / "data" / f"{name}_public.jsonl")
    public_expected = read_jsonl(answer_dir / f"{name}_public_expected.jsonl")
    if scope == "public":
        return public_cases, public_expected
    hidden_cases = read_jsonl(answer_dir / f"{name}_hidden_data.jsonl")
    hidden_expected = read_jsonl(answer_dir / f"{name}_hidden_expected.jsonl")
    return public_cases + hidden_cases, public_expected + hidden_expected


def run_question(question_dir: Path, *, submission_path: Path, outputs_path: Path, scope: str) -> int:
    spec = json.loads((question_dir / "spec.json").read_text(encoding="utf-8"))
    submission = load_submission(submission_path)
    outputs = read_jsonl(outputs_path)
    overall_errors: list[str] = []

    if spec["kind"] in {"t1", "mixed"}:
        t1_cases, t1_expected = _load_scope(question_dir, "t1", scope)
        correct, total, errors = evaluate_t1(submission, t1_cases, t1_expected, output_map(outputs, "t1"))
        overall_errors.extend(errors)
        print(f"T1 判断得分：{correct}/{total}")

    if spec["kind"] in {"t2", "mixed"}:
        bank = json.loads((question_dir / "data" / "problem_bank.json").read_text(encoding="utf-8"))
        t2_cases, t2_expected = _load_scope(question_dir, "t2", scope)
        r_ok, r_total, errors, a_ok, a_total = evaluate_t2(
            submission, bank, t2_cases, t2_expected, output_map(outputs, "t2")
        )
        overall_errors.extend(errors)
        print(f"T2 Top-K/消息：{r_ok}/{r_total}")
        print(f"T2 严格 JSON/答案：{a_ok}/{a_total}")

    if overall_errors:
        print("\n失败详情：")
        for error in overall_errors:
            print(f"- {error}")
        return 1
    print("\n✅ 本题通过：公开/隐藏数据、格式与核心逻辑均合格。")
    return 0


def main_for_question(question_dir: Path) -> int:
    parser = argparse.ArgumentParser(description=f"评测 {question_dir.name}")
    parser.add_argument(
        "--submission",
        type=Path,
        default=TRAINING_ROOT / "common" / "reference_submission.py",
        help="待测 submission.py",
    )
    parser.add_argument("--outputs", type=Path, required=True, help="模型原始输出 JSONL")
    parser.add_argument("--scope", choices=("public", "full"), default="public")
    args = parser.parse_args()
    for path in (args.submission, args.outputs):
        if not path.is_file():
            parser.error(f"找不到文件：{path}")
    return run_question(
        question_dir,
        submission_path=args.submission,
        outputs_path=args.outputs,
        scope=args.scope,
    )
