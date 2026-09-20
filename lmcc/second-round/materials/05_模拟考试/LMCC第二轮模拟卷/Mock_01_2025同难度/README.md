# Mock_01_2025同难度

接近 2025 官方真题：数学作业批改 + 最小数学 RAG

- 正式限时：3 小时。
- 满分：100 分。
- T1：5 名学生 × 5 判断 × 2 分 = 50 分。
- T2：20 个相似度检索 × 1 分 + 6 个 RAG 输出 × 5 分 = 50 分。

只修改 exam/T1/submission.py 和 exam/T2/submission.py。默认评测公开数据；加 --scope full 才会运行隐藏数据。

运行：python evaluator/evaluate.py --outputs answers/reference_outputs.jsonl --scope full
