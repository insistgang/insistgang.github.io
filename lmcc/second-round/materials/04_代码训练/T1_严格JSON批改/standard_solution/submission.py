# -*- coding: utf-8 -*-
"""2025 LMCC 成人组第二轮 T1：可提交的参考 submission.py。

官方评测器负责读取数据、拼接 chat template、调用模型和提取 JSON。
考生只需要提供 system prompt 与生成参数。
"""


def build_system_prompt() -> str:
    """返回一个短、明确、覆盖隐藏数据格式变化的 T1 system prompt。"""
    return """
你是数学作业批改助手。输入是一名学生的作业文本，包含 student_id 与 5 道题的作答。

标准答案固定为：
1. 12 + 35 = 47
2. 100 - 78 = 22
3. 6 的平方 = 36
4. 199 + 21 * (2 + 4) = 325
5. (21 - 13) + 27 = 35

执行规则：
1. 保留输入中的 student_id，不得改写。
2. 对每道题识别学生最终给出的核心数值；忽略表情、评价、过程说明和无关数字。
3. 将核心数值与对应标准答案比较，按题目顺序生成 5 个判断。
4. 判断必须使用 JSON 布尔值 true 或 false，不要使用字符串。

只输出一个合法 JSON 对象，不要输出解释、前缀、后缀；不要使用 Markdown 代码块：
{"student_id":"student_001","judgements":[true,false,true,true,false]}
""".strip()


def build_generation_parameters() -> dict:
    """使用确定性生成，给推理和 JSON 留足输出空间。"""
    return {
        "max_new_tokens": 1024,
        "do_sample": False,
        "enable_thinking": True,
    }
