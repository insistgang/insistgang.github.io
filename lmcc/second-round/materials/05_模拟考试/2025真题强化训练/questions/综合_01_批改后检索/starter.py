# -*- coding: utf-8 -*-
"""综合题 starter：一份 submission 同时承担 T1 与 T2 能力。"""

from typing import Dict, List

import torch


def build_system_prompt() -> str:
    # TODO：覆盖批改/解答两种严格 JSON 契约。
    return ""


def build_generation_parameters() -> dict:
    return {
        "max_new_tokens": 1024,
        "do_sample": False,
        "enable_thinking": False,
    }


def compute_similarity(query_embedding: torch.Tensor, doc_embedding: torch.Tensor) -> float:
    # TODO：手写余弦相似度与零向量保护。
    return 0.0


def retrieve_relevant_problems(
    query: str,
    problem_bank: List[Dict],
    embedding_model,
    tokenizer,
    top_k: int = 3,
    get_embedding_func=None,
) -> List[Dict]:
    # TODO：完成 Top-K 检索。
    return []


def build_user_message(problem: str, retrieved_problems: List[Dict]) -> str:
    # TODO：组装当前问题和参考题。
    return problem
