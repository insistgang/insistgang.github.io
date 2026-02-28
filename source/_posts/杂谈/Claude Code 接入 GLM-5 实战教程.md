---
title: Claude Code 接入 GLM-5 实战教程
date: 2026-02-28 10:00:00
tags:
  - Claude Code
  - GLM-5
  - 智谱AI
  - 配置教程
categories:
  - 杂谈
  - 技术研究
cover: /img/claude-code-glm5-tutorial/claude-code-glm5_00_cover.png
abbrlink: claude-code-glm5-tutorial
---

![封面](/img/claude-code-glm5-tutorial/claude-code-glm5_00_cover.png)

这篇是我实测可用的一套配置，目标是：让 `claude` 命令走 GLM-5 的 Anthropic 兼容接口，稳定可用、少踩坑。

---

## 一、准备条件

![第一章配图](/img/claude-code-glm5-tutorial/claude-code-glm5_01_preparation.png)

1. 已安装 Node.js（建议 18+）
2. 已安装 Claude Code CLI
3. 已有智谱（BigModel）可用 Token
4. 你的网络能访问：`https://open.bigmodel.cn`

安装 Claude Code（如未安装）：

```bash
npm i -g @anthropic-ai/claude-code
claude --version
```

---

## 二、核心配置（推荐）

![第二章配图](/img/claude-code-glm5-tutorial/claude-code-glm5_02_config.png)

编辑 `~/.claude/settings.json`：

```json
{
  "env": {
    "ANTHROPIC_AUTH_TOKEN": "你的BigModelToken",
    "ANTHROPIC_BASE_URL": "https://open.bigmodel.cn/api/anthropic",

    "ANTHROPIC_DEFAULT_SONNET_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_OPUS_MODEL": "glm-5",
    "ANTHROPIC_DEFAULT_HAIKU_MODEL": "glm-4.5-air",

    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "CLAUDE_CODE_DISABLE_FAST_MODE": "1",
    "API_TIMEOUT_MS": "3000000"
  }
}
```

> 重点：优先用 `ANTHROPIC_AUTH_TOKEN`。
> 如果你之前配的是 `ANTHROPIC_API_KEY`，建议清掉，避免冲突。

---

## 三、Shell 环境避免冲突（可选但强烈建议）

![第三章配图](/img/claude-code-glm5-tutorial/claude-code-glm5_03_shell_config.png)

在 `~/.bashrc` 里加：

```bash
unset ANTHROPIC_API_KEY
export ANTHROPIC_AUTH_TOKEN="你的BigModelToken"
export ANTHROPIC_BASE_URL="https://open.bigmodel.cn/api/anthropic"
export CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC="1"
export CLAUDE_CODE_DISABLE_FAST_MODE="1"
```

生效：

```bash
source ~/.bashrc
```

---

## 四、验证是否成功

![第四章配图](/img/claude-code-glm5-tutorial/claude-code-glm5_04_verification.png)

```bash
claude auth status
claude -p "你好，做个自我介绍"
```

如果能正常返回内容，说明配置成功。

---

## 五、常见报错与解决

![第五章配图](/img/claude-code-glm5-tutorial/claude-code-glm5_05_troubleshooting.png)

### 1) `Unable to connect to Anthropic services` / `ERR_BAD_REQUEST`

- 检查是否还在用 `ANTHROPIC_API_KEY`
- 改为 `ANTHROPIC_AUTH_TOKEN`
- 加上：
  - `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`
  - `CLAUDE_CODE_DISABLE_FAST_MODE=1`

### 2) `getaddrinfo EAI_AGAIN` / 域名解析失败

先查 DNS/网络：

```bash
getent hosts open.bigmodel.cn
curl -I https://open.bigmodel.cn
```

这两条不通，先修网络（不是 Claude 配置问题）。

### 3) 首次启动卡在 onboarding/trust

可在 `~/.claude.json` 增加：

```json
{
  "hasCompletedOnboarding": true
}
```

---

## 六、安全建议（公众号可直接放）

![第六章配图](/img/claude-code-glm5-tutorial/claude-code-glm5_06_security.png)

- Token 不要截图、不要提交到 Git
- 建议定期轮换 Token
- 团队环境用环境变量注入，不要写死在仓库

---

## 参考

- 智谱 Claude Code 配置说明（含 `ANTHROPIC_AUTH_TOKEN` / `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`）：https://docs.bigmodel.cn/cn/guide/develop/claude
- `hasCompletedOnboarding` 相关讨论：https://github.com/anthropics/claude-code/issues/2256
