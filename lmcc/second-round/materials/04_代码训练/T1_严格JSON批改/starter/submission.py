# -*- coding: utf-8 -*-
"""T1 练习 starter：只修改两个函数体。"""


def build_system_prompt() -> str:
    """TODO：写出任务、标准答案、提取规则和严格 JSON 输出契约。"""
    # TODO 1：说明输入含 student_id 和 5 道数学作业。
    # TODO 2：给出 5 道题的标准答案。
    # TODO 3：要求忽略评论/表情/无关数字，提取每题最终核心答案。
    # TODO 4：要求仅输出 {"student_id": "...", "judgements": [true, ...]}。
    return ""


def build_generation_parameters() -> dict:
    """TODO：配置稳定、可复现的生成参数。"""
    return {
        "max_new_tokens": 512,
        "do_sample": False,
        "enable_thinking": False,
    }
