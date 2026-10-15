# -*- coding: utf-8 -*-
"""仅修改这两个函数；其余评测文件不可修改。"""


def build_system_prompt() -> str:
    # TODO：写明题目标准、噪声处理规则与严格 JSON 输出。
    return ""


def build_generation_parameters() -> dict:
    return {"max_new_tokens": 512, "do_sample": False, "enable_thinking": False}
