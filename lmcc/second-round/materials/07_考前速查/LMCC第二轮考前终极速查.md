# LMCC 第二轮考前终极速查

## 先记住评分链

```text
T1：文本噪声 → 最终答案 → true/false JSON
T2：Embedding → cosine → Top-K → RAG → reasoning/answer JSON
```

## T1 Prompt 模板

```text
你是[任务]助手。输入含 student_id 和 N 道作答。
标准答案/规则：1...；2...；...
逐题提取学生最终核心答案；忽略过程、评论、表情和无关数字。
原样保留 student_id，按题目顺序输出 N 个 true/false。
只输出一个 JSON 对象；不要 Markdown、前后缀或解释。
```

输出：

```json
{"student_id":"student_001","judgements":[true,false,true,true,false]}
```

## T2 核心模板

```python
q = query_embedding.flatten().float()
d = doc_embedding.flatten().float()
denom = q.norm() * d.norm()
if denom.item() == 0:
    return 0.0
return ((q @ d) / denom).item()
```

```python
scored = []
for index, item in enumerate(problem_bank):
    emb = get_embedding_func(item["problem"], embedding_model, tokenizer)
    scored.append((compute_similarity(query_emb, emb), index))
scored.sort(key=lambda pair: (-pair[0], pair[1]))
retrieved = [problem_bank[index] for _, index in scored[:top_k]]
```

RAG 消息必须有两个区块：

```text
【当前问题】...
【参考题】题目、解析、答案
参考题只用于学习方法；独立解当前题。
```

输出：

```json
{"reasoning":"简洁过程","answer":"63"}
```

answer 只能是数字字符串。

## Prompt / API / Embedding

- `do_sample=False`：严格判定和 JSON 题优先确定性。
- `max_new_tokens`：给足输出空间，避免 JSON 被截断。
- Embedding：官方 2025 评测器负责模型与获取函数；submission 重点是使用它。
- API 调用：2025 真题未要求外部 API。若 2026 明确给 OpenAI-compatible 接口，只记：system + user + JSON 输出约束；不要把 API 学成新主线。

## JSON / JSONL

- 一行一个 JSONL 对象。
- T1：student_id、judgements，布尔值必须是 JSON true/false。
- T2：reasoning、answer；answer 无单位、无空格、无公式。
- 原始模型输出不要人工裁剪后再检查；否则会藏住多余文本问题。

## 官方评测器常见要求

1. 只修改指定 submission.py。
2. 自测与最终数据不同。
3. 先看 evaluator 如何读取、解析和计分。
4. 公共数据通过不等于最终数据通过。
5. 最终提交前运行 demo / grading，检查每条原始输出。

## 高频报错

| 现象 | 第一检查点 |
|---|---|
| JSON 无法解析 | Markdown、前缀、后缀、引号 |
| T1 分数低 | ID、数组长度、最终答案而非中间数字 |
| Top-1 错 | 是否真的除 norm、是否降序 |
| Tensor 报错 | shape、flatten、设备、float、item |
| T2 答案错 | 当前题与参考题是否混淆、是否照抄答案 |
| 隐藏集崩 | 题号/公开答案/固定格式硬编码 |

## 最后 60 秒

- T1：题目数 = judgements 长度；每项是 bool。
- T2：cosine 除 norm；排序用负分数；answer 只有数字。
- 两题：只输出 JSON；路径正确；没改 evaluator；没硬编码公开样例。
