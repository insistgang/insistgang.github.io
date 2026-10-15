# -*- coding: utf-8 -*-
"""T2 风格 starter：保持官方函数签名，填写 TODO。"""

from typing import Dict, List

import torch


def compute_similarity(query_embedding: torch.Tensor, doc_embedding: torch.Tensor) -> float:
    # TODO：余弦相似度 = 点积 / (两个 L2 范数之积)。
    return 0.0


def retrieve_relevant_problems(
    query: str,
    problem_bank: List[Dict],
    embedding_model,
    tokenizer,
    top_k: int = 3,
    get_embedding_func=None,
) -> List[Dict]:
    # TODO：取 query embedding，遍历题库，按降序返回 Top-K。
    return []


def build_user_message(problem: str, retrieved_problems: List[Dict]) -> str:
    # TODO：清楚分隔当前问题与参考题；每道参考题写 ID、题目、解析、答案。
    return problem


def build_system_prompt() -> str:
    # TODO：要求模型独立解当前题，并只返回 reasoning + answer JSON。
    return ""


def build_generation_parameters() -> dict:
    return {
        "max_new_tokens": 512,
        "do_sample": False,
        "enable_thinking": False,
    }
