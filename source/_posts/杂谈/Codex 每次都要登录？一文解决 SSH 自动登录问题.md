---
title: Codex 每次都要登录？一文解决 SSH 自动登录问题
date: 2026-02-28 10:00:00
tags:
  - Codex
  - OpenAI
  - SSH
  - 配置技巧
categories:
  - 杂谈
  - 技术研究
cover: /img/codex-ssh-auto-login-fix/codex-login_00_cover_codex.png
abbrlink: codex-ssh-auto-login-fix
---

![封面](/img/codex-ssh-auto-login-fix/codex-login_00_cover_codex.png)

> 明明配置好了 API Key，为什么每次 SSH 连接后 Codex 还是弹出登录界面？

---

## 😫 问题现象

![第一章配图](/img/codex-ssh-auto-login-fix/codex-login_01_problem_codex.png)

SSH 登录服务器后启动 Codex，每次都弹出这个界面：

```
Welcome to Codex, OpenAI's command-line coding agent

> 1. Sign in with ChatGPT
  2. Sign in with Device Code
  3. Provide your own API key

Press Enter to continue
```

按 Esc 能跳过，但下次登录又来了...

---

## 🔍 问题根因

![第二章配图](/img/codex-ssh-auto-login-fix/codex-login_02_root_cause_codex.png)

Codex 的配置分为两层：

| 层级 | 文件 | 作用 |
|------|------|------|
| 应用配置 | `~/.codex/config.toml` | 存储 API Key、模型、接口地址 |
| **认证状态** | `~/.codex/auth.json` | 标记是否完成登录 |

**关键点**：`config.toml` 里写了 API Key ≠ 完成登录！

执行 `codex login status` 会显示 `Not logged in`，这就是问题所在。

---

## ✅ 三步解决

![第三章配图](/img/codex-ssh-auto-login-fix/codex-login_03_solution_codex.png)

### 第 1 步：检查登录状态

```bash
codex login status
```

如果显示 `Not logged in`，说明需要执行登录。

### 第 2 步：执行登录命令

```bash
echo "你的API-Key" | codex login --with-api-key
```

看到 `Successfully logged in` 就成功了！

### 第 3 步：验证结果

```bash
codex login status
```

现在应该显示：
```
Logged in using an API key - sk-xx***xx
```

---

## 📁 修复后发生了什么？

![第四章配图](/img/codex-ssh-auto-login-fix/codex-login_04_result_codex.png)

Codex 创建了核心认证文件 `~/.codex/auth.json`：

```json
{
  "auth_mode": "apikey",
  "OPENAI_API_KEY": "sk-..."
}
```

同时更新了 `config.toml` 权限（从 644 改为 600），保护你的 API Key 安全。

---

## 💡 迁移到新服务器

![第五章配图](/img/codex-ssh-auto-login-fix/codex-login_05_migration_codex.png)

如果换了服务器，最简单的方式：

```bash
# 1. 复制配置文件
cp ~/.codex/config.toml 新服务器:~/.codex/

# 2. 重新登录一次（推荐）
echo "你的API-Key" | codex login --with-api-key
```

⚠️ 不建议直接复制 `auth.json`，重新登录更安全。

---

## 📝 总结

![第六章配图](/img/codex-ssh-auto-login-fix/codex-login_06_summary_codex.png)

| 问题 | 解决方案 |
|------|----------|
| 每次都要登录 | 执行 `codex login --with-api-key` |
| 配置不生效 | 检查 `auth.json` 是否存在 |

下次 SSH 登录，Codex 直接进入交互界面，无需再登录！

---

**环境信息**：Codex CLI 0.106.0 / Ubuntu 22.04
