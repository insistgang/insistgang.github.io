# Mock_03_最终冲刺

最终冲刺：覆盖文本噪声、关系检索与严格输出的合理新考法

- 正式限时：3 小时。
- 满分：100 分。
- T1：5 名学生 × 5 判断 × 2 分 = 50 分。
- T2：20 个相似度检索 × 1 分 + 6 个 RAG 输出 × 5 分 = 50 分。

只修改 exam/T1/submission.py 和 exam/T2/submission.py。默认评测公开数据；加 --scope full 才会运行隐藏数据。

运行：python evaluator/evaluate.py --outputs answers/reference_outputs.jsonl --scope full
