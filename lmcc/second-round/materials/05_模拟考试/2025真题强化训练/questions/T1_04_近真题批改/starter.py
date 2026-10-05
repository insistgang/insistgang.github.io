# -*- coding: utf-8 -*-
"""T1 风格 starter：只填写 Prompt 与生成参数。"""


def build_system_prompt() -> str:
    # TODO：写清任务、标准答案、干扰信息处理规则、严格 JSON 契约。
    return ""


def build_generation_parameters() -> dict:
    # TODO：为严格输出配置稳定的生成参数。
    return {
        "max_new_tokens": 512,
        "do_sample": False,
        "enable_thinking": False,
    }
