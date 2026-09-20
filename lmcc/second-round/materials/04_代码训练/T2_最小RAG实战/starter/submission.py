# -*- coding: utf-8 -*-
"""T2 练习 starter：保留官方函数签名，只填写 TODO 区。"""

from typing import Dict, List

import torch


def compute_similarity(
    query_embedding: torch.Tensor, doc_embedding: torch.Tensor
) -> float:
    # TODO：展平向量，计算点积 / (两个 L2 范数之积)。
    # TODO：考虑零向量，返回 Python float。
    return 0.0


def retrieve_relevant_problems(
    query: str,
    problem_bank: List[Dict],
    embedding_model,
    tokenizer,
    top_k: int = 3,
    get_embedding_func=None,
) -> List[Dict]:
    # TODO：调用 get_embedding_func 得到 query embedding。
    # TODO：遍历题库，使用 compute_similarity 计算得分。
    # TODO：按降序排序，返回前 top_k 道题。
    return []


def build_user_message(problem: str, retrieved_problems: List[Dict]) -> str:
    # TODO：明确区分“当前问题”和“参考题”。
    # TODO：每道参考题应包含 id、problem、explanation、answer。
    return problem


def build_system_prompt() -> str:
    # TODO：要求模型参考检索内容，但独立计算当前题。
    # TODO：只输出 {"reasoning":"...", "answer":"数字"}。
    return ""


def build_generation_parameters() -> dict:
    # TODO：设定确定性生成与足够的新 token。
    return {
        "max_new_tokens": 256,
        "do_sample": False,
        "enable_thinking": False,
    }
