# -*- coding: utf-8 -*-
from typing import Dict, List
import torch


def compute_similarity(query_embedding: torch.Tensor, doc_embedding: torch.Tensor) -> float:
    # TODO：余弦相似度；注意零向量与 .item()。
    return 0.0


def retrieve_relevant_problems(query: str, problem_bank: List[Dict], embedding_model, tokenizer, top_k: int = 3, get_embedding_func=None) -> List[Dict]:
    # TODO：query embedding、逐项 cosine、降序 Top-K。
    return []


def build_user_message(problem: str, retrieved_problems: List[Dict]) -> str:
    # TODO：明确分隔当前问题和参考题。
    return problem


def build_system_prompt() -> str:
    # TODO：只输出 reasoning + answer 的 JSON；answer 仅数字字符串。
    return ""


def build_generation_parameters() -> dict:
    return {"max_new_tokens": 512, "do_sample": False, "enable_thinking": False}
