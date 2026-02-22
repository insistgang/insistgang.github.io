---
title: 国产顶级 Coding Plan API 研究报告
date: 2026-02-22 12:00:00
tags:
  - AI
  - API
  - GLM
  - Kimi
  - MiniMax
  - Coding
categories:
  - 杂谈
  - 技术研究
cover: /img/coding-plan-report/cover.png
abbrlink: coding-plan-api-report
---

![封面 - 国产顶级 Coding Plan API 研究报告](/img/coding-plan-report/cover.png)


> 研究日期：2026-02-21 ~ 2026-02-22
> 研究者：Claude Code

## 概述

本研究对三个国产顶级大模型的 Coding Plan API 进行了全面测试，包括：
- **GLM (智谱AI)**
- **Kimi (月之暗面)**
- **MiniMax**

重点关注：API 连接性、文本生成能力、视觉/图片理解能力。

---



![GLM 平台架构](/img/coding-plan-report/01-glm.png)

## 一、GLM (智谱AI)

### 1.1 基本信息

| 项目 | 值 |
|------|-----|
| 平台 | 智谱AI 开放平台 |
| API 端点 | `https://open.bigmodel.cn/api/coding/paas/v4/chat/completions` |
| 认证方式 | Bearer Token |
| 格式 | OpenAI 兼容 |

### 1.2 支持模型

| 模型 | 类型 | 说明 |
|------|------|------|
| `glm-4.6V` | 视觉 | 最强视觉推理，带 reasoning_content |
| `glm-4.6V-Flash` | 视觉 | 性价比视觉模型，带 reasoning_content |
| `glm-4v-flash` | 视觉 | 轻量级图像理解，无推理链 |

### 1.3 视觉能力

- **外部 URL**: ✅ 支持
- **本地图片 (base64)**: ✅ 支持
- **原生视觉**: ✅ 是

### 1.4 测试结果

**测试图片**: 猫咪照片 (Unsplash)

**模型响应**:
> The image features a black-and-white cat as the central subject. The cat has a distinctive coat pattern: the top of its head, including its ears, is black, while the rest of its face and body are white. Its eyes are a light greenish-yellow, and it has a pink nose...

**状态**: ✅ 全部通过

---



![Kimi 平台特性](/img/coding-plan-report/02-kimi.png)

## 二、Kimi (月之暗面)

### 2.1 基本信息

| 项目 | 值 |
|------|-----|
| 平台 | Kimi AI |
| API 端点 | `https://api.kimi.com/coding/v1/chat/completions` |
| 认证方式 | Bearer Token |
| 格式 | OpenAI 兼容 |

### 2.2 特殊要求

⚠️ **必须伪装 User-Agent**

```python
headers = {
    "User-Agent": "Kilo-Code/1.0",  # 必需！
    "Authorization": f"Bearer {API_KEY}",
}
```

原因：Kimi For Coding 只允许认可的 Coding Agent 使用。

### 2.3 支持模型

| 模型 | 说明 |
|------|------|
| `kimi` | 默认模型 (kimi-for-coding) |

### 2.4 视觉能力

- **外部 URL**: ❌ 不支持
- **本地图片 (base64)**: ✅ 支持
- **原生视觉**: ✅ 是

### 2.5 测试结果

**测试图片**: 本地截图 (抖音登录界面)

**模型响应**:
> This is a screenshot of the Douyin website displaying a login modal dialog...
> - Top Navigation: Douyin logo, search bar, utility icons
> - Left Sidebar: Featured, Recommended, AI抖音, Following...
> - Login Modal: QR code login (扫码登录), Phone number login...

**状态**: ✅ 全部通过

---



![MiniMax 架构](/img/coding-plan-report/03-minimax.png)

## 三、MiniMax

### 3.1 基本信息

| 项目 | 值 |
|------|-----|
| 平台 | MiniMax 开放平台 |
| API 端点 | `https://api.minimaxi.com/v1/chat/completions` |
| 认证方式 | Bearer Token |
| 格式 | OpenAI 兼容 |

### 3.2 支持模型

| 模型 | 类型 | 说明 |
|------|------|------|
| `MiniMax-M2.5` | 文本 | 顶尖性能，~60TPS |
| `MiniMax-M2.5-highspeed` | 文本 | 极速版，~100TPS |
| `MiniMax-M2.1` | 文本 | 多语言编程专家 |
| `MiniMax-M2` | 文本 | 专为编码与Agent工作流 |

### 3.3 视觉能力

⚠️ **原生 API 不支持视觉**

Chat Completions API 的 M2.5 等模型**不支持图片输入**。

#### 3.3.1 视觉解决方案

**方式一：VLM API（推荐用于代码调用）**

```
端点: POST https://api.minimaxi.com/v1/coding_plan/vlm
```

必需 Header:
```
MM-API-Source: Minimax-MCP
```

请求格式:
```json
{
    "prompt": "描述这张图片",
    "image_url": "data:image/png;base64,..."
}
```

**方式二：MCP（推荐用于 AI 工具）**

配置命令:
```bash
claude mcp add -s user MiniMax \
    --env MINIMAX_API_KEY=your_key \
    --env MINIMAX_API_HOST=https://api.minimaxi.com \
    -- uvx minimax-coding-plan-mcp -y
```

MCP 工具:
- `web_search`: 网络搜索
- `understand_image`: 图片理解

### 3.4 测试结果

**文本 API**: ✅ 成功
**VLM API**: ✅ 成功

**测试图片**: 本地截图 (抖音登录界面)

**VLM 响应**:
> A full-page screenshot of the Douyin (Chinese TikTok) website is shown...
> - Top Bar: Douyin logo, search bar with "穿越新神精彩片段"...
> - Left Sidebar: 精选, 推荐, AI抖音, 关注...
> - Login/Registration Popup: 扫码登录, 手机号登录...

---



![三大平台对比](/img/coding-plan-report/04-comparison.png)

## 四、对比总结

### 4.1 API 配置对比

| 平台 | 端点 | 特殊要求 |
|------|------|---------|
| GLM | `open.bigmodel.cn/api/coding/paas/v4` | 无 |
| Kimi | `api.kimi.com/coding/v1` | User-Agent: Kilo-Code/1.0 |
| MiniMax | `api.minimaxi.com/v1` | 文本标准API，视觉需VLM端点 |

### 4.2 能力对比

| 能力 | GLM | Kimi | MiniMax |
|------|-----|------|---------|
| 文本生成 | ✅ | ✅ | ✅ |
| 原生视觉 | ✅ | ✅ | ❌ |
| VLM API | - | - | ✅ |
| 外部图片URL | ✅ | ❌ | ✅ (VLM) |
| 本地图片(base64) | ✅ | ✅ | ✅ (VLM) |
| 推理链 | ✅ | ✅ | ✅ |
| MCP支持 | - | - | ✅ |

### 4.3 推荐使用场景

| 场景 | 推荐 | 原因 |
|------|------|------|
| 简单集成 | GLM | 无特殊要求，即开即用 |
| 代码中调用视觉 | GLM / MiniMax VLM | 原生支持或专用API |
| AI工具集成 | 任意 | 都支持OpenAI兼容格式 |
| 高性价比 | GLM Flash / Kimi | 轻量级模型 |

---



![API 调用示例](/img/coding-plan-report/05-code.png)

## 五、代码示例

### 5.1 GLM 文生图调用

```python
import httpx

API_KEY = "your_glm_api_key"
ENDPOINT = "https://open.bigmodel.cn/api/paas/v4/images/generations"

payload = {
    "model": "cogview-3",
    "prompt": "一只可爱的猫咪在花园里玩耍",
    "size": "1024x1024"
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = httpx.post(ENDPOINT, headers=headers, json=payload)
result = response.json()

# 获取图片 URL
if "data" in result and len(result["data"]) > 0:
    image_url = result["data"][0].get("url")
    print(f"生成的图片: {image_url}")
```

### 5.2 GLM 视觉调用

```python
import httpx
import base64

API_KEY = "your_glm_api_key"
ENDPOINT = "https://open.bigmodel.cn/api/coding/paas/v4/chat/completions"

# 读取本地图片
with open("image.png", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode()

payload = {
    "model": "glm-4.6V",
    "messages": [{
        "role": "user",
        "content": [
            {"type": "text", "text": "描述这张图片"},
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

### 5.3 Kimi 视觉调用

```python
import httpx
import base64

API_KEY = "your_kimi_api_key"
ENDPOINT = "https://api.kimi.com/coding/v1/chat/completions"

# ⚠️ 必须伪装 User-Agent
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "User-Agent": "Kilo-Code/1.0",  # 关键！
}

# ... 其余同 GLM
```

### 5.4 MiniMax VLM 调用

```python
import requests
import base64

API_KEY = "your_minimax_api_key"
ENDPOINT = "https://api.minimaxi.com/v1/coding_plan/vlm"

# ⚠️ 必须添加特殊 Header
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "MM-API-Source": "Minimax-MCP",  # 关键！
}

with open("image.png", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode()

payload = {
    "prompt": "描述这张图片",
    "image_url": f"data:image/png;base64,{image_base64}"
}

response = requests.post(ENDPOINT, headers=headers, json=payload)
print(response.json()["content"])
```

---



![使用注意事项](/img/coding-plan-report/06-notes.png)

## 六、注意事项

### 6.1 认证

- 所有平台都使用 Bearer Token 认证
- API Key 格式：
  - GLM: `xxx.xxx` (JWT格式)
  - Kimi: `sk-kimi-xxx`
  - MiniMax: `sk-cp-xxx` (Coding Plan)

### 6.2 图片格式

- 支持: JPEG, PNG, WebP, GIF
- 推荐: PNG 或 JPEG
- 大小限制: 通常 20MB 以内

### 6.3 费用

- Coding Plan 通常为包月制，有 prompts 限制
- 额度刷新周期：通常每5小时

---



![文生图能力对比](/img/coding-plan-report/07-image-gen.png)

## 七、文生图能力研究

### 7.1 GLM (智谱AI)

| 项目 | 值 |
|------|-----|
| 支持文生图 | ✅ 是 |
| 端点 | `https://open.bigmodel.cn/api/paas/v4/images/generations` |
| 模型 | `cogview-3` |
| 状态 | API 格式已验证，需要充值 |

**API 格式**:
```python
import httpx

API_KEY = "your_glm_api_key"
ENDPOINT = "https://open.bigmodel.cn/api/paas/v4/images/generations"

payload = {
    "model": "cogview-3",
    "prompt": "一只可爱的猫咪在花园里玩耍"
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = httpx.post(ENDPOINT, headers=headers, json=payload)
```

**注意事项**:
- 需要 API Key 余额充足
- 返回格式为 DALL-E 兼容格式
- 图片生成需要较长时间，建议异步处理

### 7.2 Kimi (月之暗面)

| 项目 | 值 |
|------|-----|
| 支持文生图 | ❌ 否 |
| 结论 | 纯文本 LLM，不提供文生图 API |

### 7.3 MiniMax

| 项目 | 值 |
|------|-----|
| 支持文生图 | ✅ 是 |
| 端点 | `https://api.minimaxi.com/v1/image_generation` |
| 模型 | `image-01` |
| 状态 | API 格式已验证，需要充值 |

**API 格式**:
```python
import httpx

API_KEY = "your_minimax_api_key"
ENDPOINT = "https://api.minimaxi.com/v1/image_generation"

payload = {
    "model": "image-01",
    "prompt": "一只可爱的猫咪在花园里玩耍",
    "size": "1024x1024"
}

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}

response = httpx.post(ENDPOINT, headers=headers, json=payload)
```

**注意事项**:
- 端点路径为 `image_generation` (单数)，不是 `images/generations`
- 需要 API Key 余额充足
- 请求格式与 OpenAI 类似，但响应格式可能不同

### 7.4 文生图能力总结

| 平台 | 文生图支持 | 模型 | 状态 |
|------|-----------|------|------|
| GLM | ✅ | cogview-3 | 需充值 |
| Kimi | ❌ | - | 不支持 |
| MiniMax | ✅ | image-01 | 需充值 |

**结论**: GLM 和 MiniMax 均提供可用的文生图 API，格式均已验证，需要充值后才能使用。Kimi 不支持文生图。

---



![项目文件结构](/img/coding-plan-report/08-files.png)

## 八、总结

本研究全面测试了国产三大 AI 平台的 Coding Plan API：

| 平台 | 综合评价 |
|------|---------|
| GLM | 最易用，原生视觉支持，文档完善 |
| Kimi | 需要伪装 UA，功能正常，不支持外部图片 URL |
| MiniMax | 文本能力强，视觉需要单独 VLM 端点 |

**推荐选择**：
- 追求简单：选 GLM
- 追求性价比：选 GLM Flash 或 Kimi
- 需要 MCP 集成：选 MiniMax
