---
title: 通义千问 (Qwen) Coding Plan 调研报告
date: 2026-02-23 12:00:00
tags:
  - AI
  - API
  - Qwen
  - 通义千问
  - Coding
  - 阿里云
categories:
  - 杂谈
  - 技术研究
cover: /img/qwen-coding-plan/cover.png
abbrlink: qwen-coding-plan-report
---

![封面 - 通义千问 Coding Plan 调研报告](/img/qwen-coding-plan/cover.png)

## 概述

本报告旨在对阿里云百炼平台推出的 **通义千问 (Qwen) Coding Plan** 进行全面调研，并总结其在 API 连接性、支持模型、视觉能力、语音功能、MCP 扩展、网页搜索及 GitHub 开源代码查找等方面的具体能力。通义千问作为国产大模型的代表，其 Coding Plan 旨在为开发者提供高效、高性价比的 AI 编码辅助服务。

![核心能力](/img/qwen-coding-plan/01-core.png)

## 一、 通义千问 (Qwen) Coding Plan 核心能力

### 1.1 基本信息

| 项目 | 描述 |
| :--- | :--- |
| **平台** | 阿里云百炼 (Model Studio) |
| **API 端点** | `https://coding.dashscope.aliyuncs.com/v1` (Coding Plan 专属) [1] |
| **认证方式** | Bearer Token (API Key 格式为 `sk-sp-xxxx`，与通用 `sk-xxxx` Key 不同) [1] |
| **格式** | OpenAI / Anthropic 双协议兼容 [1] |

### 1.2 支持模型

Coding Plan 主要支持以下模型，这些模型在文本生成和代码能力方面表现卓越，部分模型还具备视觉理解能力 [1]。

| 模型名称 | 类型 | 说明 |
| :--- | :--- | :--- |
| **qwen3.5-plus** | 文本/视觉 | 最新一代旗舰模型，效果、速度、成本均衡，支持思考模式和视觉理解 [1]。 |
| **qwen3-max-2026-01-23** | 文本/视觉 | 旗舰性能模型，适合处理极复杂的架构设计与逻辑推理 [1]。 |
| **qwen3-coder-next** | 文本 | 专为 Coding Agent 优化，具备极强的工具调用与环境交互能力 [1]。 |
| **qwen3-coder-plus** | 文本 | 高性能代码模型，适配大规模代码库重构与生成 [1]。 |
| **glm-4.7** | 文本 | 第三方模型，通过 Coding Plan 订阅支持 [1]。 |
| **kimi-k2.5** | 文本 | 第三方模型，通过 Coding Plan 订阅支持 [1]。 |

### 1.3 视觉能力

通义千问的视觉能力主要通过 `qwen3.5-plus` 等模型提供，这些模型能够处理图像输入，辅助理解代码相关的图表和文档 [2]。

| 项目 | 支持情况 | 备注 |
| :--- | :--- | :--- |
| **外部 URL 支持** | ✅ 支持 | 可通过 URL 引用图片进行分析 [2]。 |
| **本地图片 (base64) 支持** | ✅ 支持 | 可将本地图片编码为 Base64 格式后作为输入 [2]。 |
| **原生视觉支持** | ✅ 是 | 模型具备原生的视觉理解能力 [2]。 |
| **高分辨率图像处理** | ✅ 支持 | 可通过 `vl_high_resolution_images` 参数提升图像像素上限 [2]。 |

### 1.4 语音功能

**通义千问 Coding Plan 不直接包含语音功能**。Coding Plan 专注于代码场景，其套餐额度不适用于语音识别、语音合成等功能 [3]。

| 项目 | 支持情况 | 备注 |
| :--- | :--- | :--- |
| **语音输入/输出** | ❌ 不支持 | Coding Plan 套餐不覆盖语音功能 [3]。 |
| **Qwen-Audio 模型** | ❌ 不包含 | `Qwen-Audio` 是独立的语音模型，按量计费，不属于 Coding Plan [3]。 |
| **Qwen-Omni 模型** | ❌ 不包含 | `Qwen-Omni` 是全模态模型，按量计费，不属于 Coding Plan [3]。 |

### 1.5 MCP (Model Context Protocol) 扩展能力

通义千问的官方编程工具 **Qwen Code** 原生支持 MCP 协议，这使得 Coding Plan 具备强大的扩展性 [4]。

| 项目 | 描述 |
| :--- | :--- |
| **原生支持** | Qwen Code CLI 工具原生支持 MCP 协议 [4]。 |
| **功能扩展** | 通过配置 MCP 服务器，可连接外部工具、数据库和 API，实现文件处理、数据库查询、内部服务集成、工作流自动化等 [4]。 |
| **第三方工具适配** | Coding Plan 兼容 OpenAI/Anthropic 协议，可在支持 MCP 的第三方工具（如 Cline、Claude Code）中调用配置的 MCP 服务 [4]。 |

### 1.6 网页搜索与 GitHub 开源代码查找能力

Coding Plan 本身不直接内置网页搜索或 GitHub 搜索功能，但可以通过 MCP 机制进行扩展 [5]。

| 项目 | 支持情况 | 实现方式 |
| :--- | :--- | :--- |
| **网页搜索** | ✅ 可通过 MCP 扩展 | 配置支持联网搜索的 MCP 服务器（如 `brave-search` 或 `google-search`），或利用第三方工具内置的联网搜索插件 [5]。 |
| **GitHub 搜索** | ✅ 可通过 MCP 扩展 | 配置 GitHub MCP 服务器，使 Qwen Code 能够搜索、读取 GitHub 上的开源代码和项目信息 [5]。 |

![费用与订阅](/img/qwen-coding-plan/02-pricing.png)

## 二、 费用与订阅

Coding Plan 采用固定月费订阅模式，提供月度请求额度，旨在以可控成本满足高频次的编码需求 [1]。

| 套餐类型 | 月费 (原价) | 首月优惠 | 月度请求额度 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| **Lite 基础套餐** | ¥40 | ¥7.9 | 约 5,000 次 [a] | 适合轻量级个人开发者 [1]。 |
| **Pro 高级套餐** | ¥200 | ¥39.9 | 最多 90,000 次 [a] | 适合全职开发者或高频使用场景 [1]。 |

> [a] 一次复杂提问可能触发 10 到 20 次模型调用，每次模型调用均计入一次额度消耗。实际额度消耗取决于任务复杂度、上下文大小、工具调用次数等多种因素 [1]。

![注意事项](/img/qwen-coding-plan/03-notice.png)

## 三、 注意事项

- **认证与 Key 区分**：务必使用 `sk-sp-` 开头的 Coding Plan 专属 API Key，否则将按通用按量计费模式收费 [1]。
- **订阅限制**：Coding Plan 仅限在编程工具中交互式使用，严禁用于自动化脚本或非交互式批量调用，违规可能导致封号 [1]。
- **账号限制**：仅支持阿里云主账号订阅，不支持 RAM 子账号 [1]。
- **不可退款**：订阅后不支持退订与退款 [1]。

## 四、 代码示例

### 4.1 基本调用

```python
import httpx

API_KEY = "sk-sp-your_coding_plan_key"
ENDPOINT = "https://coding.dashscope.aliyuncs.com/v1/chat/completions"

payload = {
    "model": "qwen3.5-plus",
    "messages": [
        {"role": "user", "content": "帮我写一个 Python 函数计算斐波那契数列"}
    ]
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = httpx.post(ENDPOINT, headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
```

### 4.2 视觉调用

```python
import httpx
import base64

API_KEY = "sk-sp-your_coding_plan_key"
ENDPOINT = "https://coding.dashscope.aliyuncs.com/v1/chat/completions"

# 读取本地图片
with open("screenshot.png", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode()

payload = {
    "model": "qwen3.5-plus",
    "messages": [{
        "role": "user",
        "content": [
            {"type": "text", "text": "分析这张截图中的 UI 设计"},
            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}}
        ]
    }]
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = httpx.post(ENDPOINT, headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
```

### 4.3 外部图片 URL 调用

```python
import httpx

API_KEY = "sk-sp-your_coding_plan_key"
ENDPOINT = "https://coding.dashscope.aliyuncs.com/v1/chat/completions"

payload = {
    "model": "qwen3.5-plus",
    "messages": [{
        "role": "user",
        "content": [
            {"type": "text", "text": "描述这张图片的内容"},
            {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
        ]
    }]
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = httpx.post(ENDPOINT, headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
```

## 五、 与其他平台对比

| 能力 | Qwen | GLM | Kimi | MiniMax |
|------|------|-----|------|---------|
| 文本生成 | ✅ | ✅ | ✅ | ✅ |
| 原生视觉 | ✅ | ✅ | ✅ | ❌ |
| 外部图片 URL | ✅ | ✅ | ❌ | ✅ (VLM) |
| 本地图片 (base64) | ✅ | ✅ | ✅ | ✅ (VLM) |
| 双协议兼容 | ✅ | ❌ | ❌ | ❌ |
| MCP 支持 | ✅ | - | - | ✅ |
| 第三方模型 | ✅ | ❌ | ❌ | ❌ |

**Qwen 独特优势**：
- **双协议兼容**：同时支持 OpenAI 和 Anthropic 协议，适配性最广
- **第三方模型支持**：除自研模型外，还支持 GLM-4.7、Kimi-K2.5 等
- **官方编程工具**：Qwen Code CLI 原生支持 MCP 协议

## 六、 总结

通义千问 Coding Plan 作为阿里云百炼平台推出的开发者专属订阅服务，具有以下特点：

| 维度 | 评价 |
|------|------|
| **易用性** | 双协议兼容，迁移成本低 |
| **功能性** | 支持视觉理解，MCP 扩展性强 |
| **性价比** | Lite 套餐首月仅 ¥7.9，适合尝鲜 |
| **生态** | 支持第三方模型，选择丰富 |

**推荐使用场景**：
- 需要 OpenAI/Anthropic 双协议兼容的项目
- 需要调用多种国产大模型的场景
- 追求高性价比的个人开发者

## 参考文献

[1] 阿里云百炼. Coding Plan. [https://help.aliyun.com/zh/model-studio/coding-plan](https://help.aliyun.com/zh/model-studio/coding-plan)

[2] 阿里云百炼. 千问qwen-image和万相wan模型文生图使用方式. [https://help.aliyun.com/zh/model-studio/text-to-image](https://help.aliyun.com/zh/model-studio/text-to-image)

[3] 阿里云百炼. Qwen-Omni-大模型服务平台百炼(Model Studio). [https://help.aliyun.com/zh/model-studio/qwen-omni](https://help.aliyun.com/zh/model-studio/qwen-omni)

[4] Qwen Code Docs. 通过 MCP 将 Qwen Code 连接到工具. [https://qwenlm.github.io/qwen-code-docs/zh/users/features/mcp/](https://qwenlm.github.io/qwen-code-docs/zh/users/features/mcp/)

[5] 阿里云百炼. 官方和第三方插件. [https://help.aliyun.com/zh/model-studio/plugins](https://help.aliyun.com/zh/model-studio/plugins)
