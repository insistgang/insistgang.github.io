"""Reference implementation shared by local reinforcement evaluators.

It mirrors the official 2025 function names.  Local fake embeddings are only
used by the training runner; official evaluation provides the real function.
"""

from typing import Dict, List

import torch


def build_system_prompt() -> str:
    return (
        "先理解输入任务与参考信息，严格按指定 JSON 字段输出；"
        "不要输出 Markdown、解释前缀或无关文字。"
    )


def build_generation_parameters() -> dict:
    return {"max_new_tokens": 1024, "do_sample": False, "enable_thinking": True}


def compute_similarity(query_embedding: torch.Tensor, doc_embedding: torch.Tensor) -> float:
    query = query_embedding.flatten().float()
    document = doc_embedding.flatten().float()
    denominator = query.norm() * document.norm()
    if denominator.item() == 0:
        return 0.0
    return ((query @ document) / denominator).item()


def retrieve_relevant_problems(
    query: str,
    problem_bank: List[Dict],
    embedding_model,
    tokenizer,
    top_k: int = 3,
    get_embedding_func=None,
) -> List[Dict]:
    if not problem_bank or top_k <= 0:
        return []
    if get_embedding_func is None:
        raise ValueError("缺少 get_embedding_func")
    query_embedding = get_embedding_func(query, embedding_model, tokenizer)
    scored = []
    for index, item in enumerate(problem_bank):
        embedding = get_embedding_func(item["problem"], embedding_model, tokenizer)
        scored.append((compute_similarity(query_embedding, embedding), index))
    scored.sort(key=lambda pair: (-pair[0], pair[1]))
    return [problem_bank[index] for _, index in scored[:top_k]]


def build_user_message(problem: str, retrieved_problems: List[Dict]) -> str:
    lines = [f"【当前问题】\n{problem}", "", "【参考题】"]
    for rank, item in enumerate(retrieved_problems, 1):
        lines += [
            f"参考题 {rank}（ID={item['id']}）",
            f"题目：{item['problem']}",
            f"解析：{item['explanation']}",
            f"答案：{item['answer']}",
        ]
    lines.append("参考题只用于学习方法；请独立解决当前问题。")
    return "\n".join(lines)
