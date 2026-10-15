# -*- coding: utf-8 -*-
"""2025 LMCC 成人组第二轮 T2：参考 submission.py。

保持官方函数签名；评测器负责模型、tokenizer、Embedding 获取和生成调用。
"""

from typing import Dict, List

import torch


def compute_similarity(
    query_embedding: torch.Tensor, doc_embedding: torch.Tensor
) -> float:
    """计算一维向量余弦相似度；零向量按 0.0 处理，避免 NaN。"""
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
    """按余弦相似度降序返回最多 top_k 道参考题。"""
    if not problem_bank or top_k <= 0:
        return []
    if get_embedding_func is None:
        raise ValueError("评测器必须提供 get_embedding_func")

    query_embedding = get_embedding_func(query, embedding_model, tokenizer)
    scored: list[tuple[float, int]] = []
    for index, problem_item in enumerate(problem_bank):
        problem_embedding = get_embedding_func(
            problem_item["problem"], embedding_model, tokenizer
        )
        score = compute_similarity(query_embedding, problem_embedding)
        scored.append((score, index))

    # 分数高优先；并列时按原题库顺序，确保结果稳定。
    scored.sort(key=lambda item: (-item[0], item[1]))
    return [problem_bank[index] for _, index in scored[:top_k]]


def build_user_message(problem: str, retrieved_problems: List[Dict]) -> str:
    """清晰分隔当前题与参考题，避免模型把参考答案当作当前答案。"""
    lines = [
        "你将解答【当前问题】。参考题仅用于学习方法，不能直接照抄答案。",
        f"【当前问题】\n{problem}",
        "",
        "【检索到的参考题】",
    ]
    for rank, item in enumerate(retrieved_problems, 1):
        lines.extend(
            [
                f"参考题 {rank}（ID={item['id']}）",
                f"题目：{item['problem']}",
                f"解析：{item['explanation']}",
                f"答案：{item['answer']}",
                "",
            ]
        )
    lines.append("请只回答当前问题，并按 system prompt 的 JSON 格式输出。")
    return "\n".join(lines)


def build_system_prompt() -> str:
    """约束 RAG 解题模型输出可被官方评测器稳定解析的 JSON。"""
    return """
你是数学解题助手。用户消息会包含一个当前问题和若干检索到的参考题。

执行规则：
1. 参考题只用于学习解法；必须独立计算当前问题，不要直接复制参考答案。
2. reasoning 用简洁中文说明关键计算。
3. answer 只能是最终数字字符串，不要单位、公式、解释或额外空格。

只输出一个合法 JSON 对象；不要输出解释、前缀、后缀或 Markdown：
{"reasoning":"计算过程","answer":"63"}
""".strip()


def build_generation_parameters() -> dict:
    """保持确定性输出，并为思考和 JSON 返回预留空间。"""
    return {
        "max_new_tokens": 1024,
        "do_sample": False,
        "enable_thinking": True,
    }
