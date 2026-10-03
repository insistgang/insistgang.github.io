# 2025 T2：RAG 数学解答助手

## 题目任务

实现“问题 → Embedding → 余弦相似度 → Top-K 相似题 → 组装上下文 → LLM JSON 回答”的最小 RAG 管线。

## 五个函数与拿分点

| 函数 | 直接能力 |
|---|---|
| `compute_similarity` | 张量点积、L2 范数、零向量边界、返回 Python float |
| `retrieve_relevant_problems` | 调用给定 embedding 函数、排序、Top-K |
| `build_user_message` | 清晰区分“当前题”和“参考题”，提供题干/解析/答案 |
| `build_system_prompt` | 约束模型参考检索内容、返回严格 JSON |
| `build_generation_parameters` | 确保输出空间充足且保持可复现 |

## 需要独立写出的最小公式

```python
similarity = (query @ doc) / (query.norm() * doc.norm())
```

等价实现：

```python
import torch.nn.functional as F
similarity = F.cosine_similarity(query, doc, dim=0).item()
```

## 最容易失分的位置

- 只算点积，没有除以两个向量范数。
- 排序方向写反，拿到最不相似的题。
- `top_k` 越界或不尊重传入参数。
- 把当前题和检索到的参考题混在一起，模型无法识别任务。
- `answer` 中带单位、公式、解释或 Markdown。
- 直接拿自测数据里的题号/答案做规则，隐藏集失效。

## 2026 价值判断

**S 级。** 这是 2025 第二轮最清晰的硬编码得分点。即使 2026 的素材从小学数学换成文本、知识库、代码或表格，Embedding 检索、余弦相似度、Top-K、上下文组装、严格输出仍是最高收益能力。

## 训练变式

1. 用 FAQ 题库做检索，输出答案与证据 ID。
2. 用文档片段做检索，输出包含引用编号的 JSON。
3. 加入零向量、重复相似度、`top_k > len(bank)`、空题库等边界测试。
