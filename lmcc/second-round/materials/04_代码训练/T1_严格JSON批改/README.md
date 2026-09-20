# T1 严格 JSON 批改训练包

这是一套围绕 2025 LMCC 成人组第二轮 T1 的训练包。目标不是离线训练模型，而是训练你在考试中看懂评测器后，写出短、稳、可验证的 `submission.py`。

## 先做什么

1. 阅读 [T1_逐步拆解.md](T1_逐步拆解.md)。
2. 不看答案，完成 [starter/submission.py](starter/submission.py)。
3. 对照 [standard_solution/submission.py](standard_solution/submission.py) 复盘 Prompt 的信息层次。
4. 依次完成 `exercises/01` 到 `05`，答案只在 `answers/`。
5. 用 `tools/t1_scorer.py` 批量检查格式和判断结果。

## 目录

```text
T1_严格JSON批改/
├── standard_solution/      # 官方 T1 风格的参考 submission.py
├── starter/                # 你自己填写的两个函数
├── exercises/              # 5 道变式题；只含题目与输入数据
├── answers/                # 预期判断结果，做完再打开
├── tools/
│   ├── t1_validator.py     # 严格 JSON 契约检查
│   └── t1_scorer.py        # 批量检查格式并逐项计分
└── tests/                  # 本地回归测试
```

## 自测文件格式

你的 `my_outputs.jsonl` 每行是一位学生的**原始模型输出**：

```json
{"student_id":"student_101","raw_output":"{\"student_id\":\"student_101\",\"judgements\":[true,true,true]}"}
```

注意：`raw_output` 必须保存模型完整返回文本。不要先手动从中截取 JSON；否则你无法发现“模型夹带解释”这种考试风险。

## 批量自测

在某道练习目录中运行：

```bash
python ../../tools/t1_scorer.py \
  --outputs my_outputs.jsonl \
  --answers ../../answers/01_数字提取入门_expected.jsonl
```

仓库也附了一个可直接运行的批量样例：

```bash
python tools/t1_scorer.py \
  --outputs answers/demo_outputs_01.jsonl \
  --answers answers/01_数字提取入门_expected.jsonl
```

评分器会检查：

- 原始输出能否整体解析为 JSON。
- 是否有 JSON 外的多余文本。
- `student_id` 是否原样回传。
- `judgements` 是否存在、是否数组、长度是否正确。
- 每项是否是 `true/false`，而不是 `1/0` 或字符串。
- 判断结果逐项得分。

## 运行包内测试

```bash
python -m unittest discover -s tests -v
```

本训练包只使用 Python 标准库；无需 API Key、GPU 或下载模型。要接入官方评测器，请将参考或 starter 的 `submission.py` 放到官方 T1 目录中，再在官方环境运行 `evaluate.py --mode demo`。
