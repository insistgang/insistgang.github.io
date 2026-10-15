# T1 标准解法使用说明

这份 `submission.py` 只使用官方允许改动的两个函数。

它的策略是：

1. 在 system prompt 里明确给出 5 个标准答案。
2. 规定“提取每题最终核心数值”，避免把评论、表情或过程里的数字误当答案。
3. 规定只输出一个 JSON 对象，避免 Markdown 和解释污染输出。
4. 用 `do_sample=False` 保持稳定；使用 `enable_thinking=True`，2025 官方评测器会移除 thinking 标签后再提取 JSON。

它不是一个可离线批改的完整程序：官方评测器负责模型调用。没有官方模型和环境时，用 `../tools/t1_validator.py` 训练 JSON 输出契约。
