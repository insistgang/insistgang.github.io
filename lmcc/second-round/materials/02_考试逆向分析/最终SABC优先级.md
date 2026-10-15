# 第二轮最终 S / A / B / C 优先级

排序依据：2025 成人组第二轮官方 T1/T2 的实际 100 分结构 > 官方评测器 > 2026 成人组大纲。目标是通过第二轮，不是覆盖全部大模型课程。

## S：考试现场必须闭卷完成

1. 先读 README、允许修改位置和 evaluator 的计分逻辑。
2. Python 的函数、列表、字典、枚举、排序、JSON/JSONL、路径。
3. T1 Prompt：任务、标准答案、噪声提取规则、纯 JSON 布尔数组。
4. T1 JSON：student_id 原样回传、judgements 长度正确、元素是 true/false。
5. PyTorch Tensor 基础：flatten、float、norm、点积、item。
6. cosine similarity：点积除两个 L2 范数，零向量保护。
7. Top-K：逐项得分、降序排序、稳定切片。
8. 最小 RAG：当前题与参考题清晰分隔；参考题只学方法。
9. T2 JSON：reasoning 字符串，answer 只含数字字符串。
10. 公开集调试、隐藏变式自测、提交前格式检查。

## A：高概率使用，应能独立改模板

- AutoTokenizer / AutoModel 的加载、eval、no_grad、生成后切片。
- Embedding 的 attention-mask 平均池化。
- 生成参数：max_new_tokens、do_sample、temperature、top-p、thinking。
- 数据、模型、路径、编码与输出解析失败的定位。

## B：理解即可，能借模板完成

- Dataset / DataLoader 与最小训练循环。
- LoRA / PEFT 的 target_modules、可训练参数、保存加载。
- Accuracy、Precision、Recall、F1 的计算与用途。

## C：考前不投入大量时间

- 完整 RLHF / DPO / GRPO 训练。
- 复杂多智能体、Function Calling 平台、向量数据库部署。
- 分布式训练、量化、并行、完整微调工程。

这些项目在大纲中存在，但 2025 第二轮真题没有直接要求。只有官方 2026 代码包或考场说明明确出现时，才上调优先级。
