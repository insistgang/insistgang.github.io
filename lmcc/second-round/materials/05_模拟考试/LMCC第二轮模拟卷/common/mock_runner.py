#!/usr/bin/env python3
"""Strict 100-point evaluator for 2025-style LMCC second-round mocks."""

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


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def mock_embedding(text: str, _model=None, _tokenizer=None, *, dimensions: int = 128) -> TinyTensor:
    """Deterministic offline embedding used only to verify the candidate pipeline."""
    vector = [0.0] * dimensions
    for token in re.findall(r"[A-Za-z]+|\d+|[\u4e00-\u9fff]", text.lower()):
        index = int(hashlib.sha256(token.encode("utf-8")).hexdigest()[:8], 16) % dimensions
        vector[index] += 1.0
    return TinyTensor(vector)


def load_submission(path: Path, name: str):
    try:
        import torch  # noqa: F401
    except ModuleNotFoundError:
        install_torch_shim()
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ValueError(f"无法加载：{path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def output_map(records: list[dict[str, Any]], section: str) -> dict[str, Any]:
    return {
        record["id"]: record.get("raw_output")
        for record in records
        if record.get("section", section) == section and "id" in record
    }


def load_scope(mock_dir: Path, name: str, scope: str):
    public_data = read_jsonl(mock_dir / "data" / f"{name}_public.jsonl")
    public_expected = read_jsonl(mock_dir / "answers" / "public" / f"{name}_expected.jsonl")
    if scope == "public":
        return public_data, public_expected
    hidden_data = read_jsonl(mock_dir / "answers" / "hidden" / f"{name}_data.jsonl")
    hidden_expected = read_jsonl(mock_dir / "answers" / "hidden" / f"{name}_expected.jsonl")
    return public_data + hidden_data, public_expected + hidden_expected


def check_t1(submission, cases, expected, outputs) -> tuple[int, int, list[str]]:
    errors = []
    if not callable(getattr(submission, "build_system_prompt", None)):
        return 0, 50, ["T1 缺少 build_system_prompt"]
    if not callable(getattr(submission, "build_generation_parameters", None)):
        return 0, 50, ["T1 缺少 build_generation_parameters"]
    if not str(submission.build_system_prompt()).strip():
        errors.append("T1 system prompt 为空")
    if submission.build_generation_parameters().get("do_sample") is not False:
        errors.append("T1 必须显式设置 do_sample=False")

    expected_map = {item["id"]: item for item in expected}
    correct = 0
    for case in cases:
        answer = expected_map[case["id"]]
        result = validate_t1_output(
            outputs.get(case["id"]),
            student_id=case["student_id"],
            expected_count=len(answer["judgements"]),
        )
        if not result.valid:
            errors.append(f"T1 {case['id']}: {'；'.join(result.errors)}")
            continue
        correct += sum(
            got == want
            for got, want in zip(result.parsed["judgements"], answer["judgements"])
        )
    return correct * 2, len(expected_map) * 5 * 2, errors


def check_t2(submission, problem_bank, similarity_cases, rag_cases, rag_expected, outputs):
    errors = []
    required = (
        "compute_similarity",
        "retrieve_relevant_problems",
        "build_user_message",
        "build_system_prompt",
        "build_generation_parameters",
    )
    missing = [name for name in required if not callable(getattr(submission, name, None))]
    if missing:
        return 0, 0, [f"T2 缺少函数：{', '.join(missing)}"]
    if submission.build_generation_parameters().get("do_sample") is not False:
        errors.append("T2 必须显式设置 do_sample=False")

    bank_embeddings = [
        mock_embedding(item["problem"]) for item in problem_bank
    ]
    similarity_score = 0
    for case in similarity_cases:
        query_embedding = mock_embedding(case["query"])
        scores = [
            (submission.compute_similarity(query_embedding, embedding), index)
            for index, embedding in enumerate(bank_embeddings)
        ]
        scores.sort(key=lambda pair: (-pair[0], pair[1]))
        actual = problem_bank[scores[0][1]]["id"]
        if actual == case["expected_top_id"]:
            similarity_score += 1
        else:
            errors.append(
                f"相似度 {case['id']}: 期望 {case['expected_top_id']}，实际 {actual}"
            )

    expected_map = {item["id"]: item for item in rag_expected}
    rag_score = 0
    for case in rag_cases:
        expected = expected_map[case["id"]]
        try:
            retrieved = submission.retrieve_relevant_problems(
                case["problem"],
                problem_bank,
                embedding_model=None,
                tokenizer=None,
                top_k=3,
                get_embedding_func=mock_embedding,
            )
            actual = retrieved[0]["id"] if retrieved else None
            message = submission.build_user_message(case["problem"], retrieved)
            if actual != expected["expected_top_id"] or case["problem"] not in message:
                errors.append(f"RAG {case['id']}: Top-K 或消息组装错误")
        except Exception as exc:
            errors.append(f"RAG {case['id']}: 检索异常：{exc}")
            continue
        result = validate_t2_output(outputs.get(case["id"]), expected_answer=expected["answer"])
        if result.valid:
            rag_score += 5
        else:
            errors.append(f"RAG {case['id']}: {'；'.join(result.errors)}")
    return similarity_score, rag_score, errors


def run_mock(mock_dir: Path, *, t1_path: Path, t2_path: Path, outputs_path: Path, scope: str) -> int:
    t1_submission = load_submission(t1_path, "mock_t1_submission")
    t2_submission = load_submission(t2_path, "mock_t2_submission")
    outputs = read_jsonl(outputs_path)
    t1_cases, t1_expected = load_scope(mock_dir, "t1", scope)
    sim_cases, _ = load_scope(mock_dir, "t2_similarity", scope)
    rag_cases, rag_expected = load_scope(mock_dir, "t2_rag", scope)
    problem_bank = json.loads((mock_dir / "data" / "problem_bank.json").read_text(encoding="utf-8"))

    t1_score, t1_total, t1_errors = check_t1(
        t1_submission, t1_cases, t1_expected, output_map(outputs, "t1")
    )
    sim_score, rag_score, t2_errors = check_t2(
        t2_submission,
        problem_bank,
        sim_cases,
        rag_cases,
        rag_expected,
        output_map(outputs, "t2"),
    )
    total = t1_score + sim_score + rag_score
    print(f"T1：{t1_score}/{t1_total}")
    print(f"T2 相似度：{sim_score}/20")
    print(f"T2 RAG：{rag_score}/30")
    print(f"总分：{total}/100")
    errors = t1_errors + t2_errors
    if errors:
        print("\n失败详情：")
        for error in errors:
            print(f"- {error}")
        return 1
    print("\n✅ 当前 scope 全部通过。")
    return 0


def main_for_mock(mock_dir: Path) -> int:
    parser = argparse.ArgumentParser(description=f"评测 {mock_dir.name}")
    parser.add_argument("--t1", type=Path, default=mock_dir / "answers" / "reference_T1_submission.py")
    parser.add_argument("--t2", type=Path, default=mock_dir / "answers" / "reference_T2_submission.py")
    parser.add_argument("--outputs", type=Path, required=True)
    parser.add_argument("--scope", choices=("public", "full"), default="public")
    args = parser.parse_args()
    for path in (args.t1, args.t2, args.outputs):
        if not path.is_file():
            parser.error(f"找不到文件：{path}")
    return run_mock(mock_dir, t1_path=args.t1, t2_path=args.t2, outputs_path=args.outputs, scope=args.scope)
