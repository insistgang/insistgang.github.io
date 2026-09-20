# LMCC 成人组第二轮模拟考试

三套模拟卷均按 **3 小时、100 分** 设计，评分结构严格复刻 2025 成人组第二轮的两题分配：

| 部分 | 分值 | 评分逻辑 |
|---|---:|---|
| T1 文本批改 | 50 | 5 名学生 × 5 个判断 × 2 分 |
| T2 相似度 | 20 | 20 个查询，每个 Top-1 正确得 1 分 |
| T2 RAG | 30 | 6 个问题，每题严格 JSON 与最终答案正确得 5 分 |

## 三套卷

- Mock_01_2025同难度：数学作业批改 + 最小数学 RAG，最接近 2025 首期风格。
- Mock_02_合理变式：应用题叙述变化，训练关系迁移而非背题。
- Mock_03_最终冲刺：综合文本噪声、隐藏数据与检索边界。

每套均包含：

```text
Mock_xx/
├── exam/
│   ├── README.md
│   ├── T1/submission.py
│   └── T2/submission.py
├── data/                       # 只含公开数据
├── evaluator/evaluate.py       # 独立评测入口
└── answers/
    ├── public/                 # 公开期望结果
    ├── hidden/                 # hidden 数据与期望结果
    ├── 标准答案.md
    └── 解析.md
```

默认只测公开集；只在完成后加 `--scope full` 运行隐藏集。隐藏数据位于 `answers/hidden/`，不要在做题前打开。

## 正式运行方式

以 Mock 01 为例：

```bash
cd Mock_01_2025同难度
python evaluator/evaluate.py \
  --t1 exam/T1/submission.py \
  --t2 exam/T2/submission.py \
  --outputs my_outputs.jsonl \
  --scope public
```

公开集通过后：

```bash
python evaluator/evaluate.py \
  --t1 exam/T1/submission.py \
  --t2 exam/T2/submission.py \
  --outputs my_outputs.jsonl \
  --scope full
```

输出 JSONL 的格式：

```json
{"section":"t1","id":"01-t1-1","raw_output":"{\"student_id\":\"student_001\",\"judgements\":[true,false,true,true,false]}"}
{"section":"t2","id":"01-rag-1","raw_output":"{\"reasoning\":\"简洁过程\",\"answer\":\"96\"}"}
```

T1 与 T2 的模型原始输出必须直接填入 `raw_output`；不要手动裁剪 JSON，否则会掩盖 Markdown、前缀或类型错误。

## 环境边界

本机没有 PyTorch，因此评测器以轻量 Tensor mock 实际验证 cosine、排序、Top-K、JSON 与隐藏集逻辑；starter 和参考代码保留 2025 官方式 PyTorch 接口。进入 2026 官方环境后，仍须使用官方评测器复验。
