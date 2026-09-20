# T2 最小 RAG 实战包

这是 2025 LMCC 成人组第二轮 T2 的考试训练包。官方题的重点不是搭一个生产级 RAG 平台，而是在既有评测器里完成：

```text
Embedding → cosine similarity → Top-K → 参考题组装 → 严格 JSON
```

## 训练顺序

1. 读 [T2逐步拆解.md](T2逐步拆解.md)。
2. 不看答案填写 [starter/submission.py](starter/submission.py)。
3. 对照 [标准解法](standard_solution/submission.py)。
4. 依次完成 `exercises/01` 到 `05`。
5. 用 [batch_evaluate.py](batch_evaluate.py) 做检索、消息组装和 JSON 输出自测。

快捷入口也已提供：[T2标准解法.py](T2标准解法.py) 与 [T2_starter.py](T2_starter.py)。

## 重要环境说明

- 官方 2025 代码使用真实 PyTorch、Transformers、MindNLP 和模型环境。
- 当前本地运行时没有 PyTorch。因此批量评测器用一个最小 Tensor mock 执行同一套 `flatten → norm → @ → item` 逻辑，验证你的**算法和函数契约**。
- 这不能替代官方环境。获得 2026 环境后，务必在官方 `evaluate.py --mode demo` 上重跑。

## 快速验证

```bash
python batch_evaluate.py \
  --exercise exercises/01_折扣检索入门 \
  --answers answers/01_折扣检索入门_expected.jsonl \
  --outputs answers/01_demo_outputs.jsonl
```

预期输出：

```text
检索与消息组装：2/2
严格 JSON + 答案：2/2
```

运行所有参考练习：

```bash
python run_all_reference.py
```
