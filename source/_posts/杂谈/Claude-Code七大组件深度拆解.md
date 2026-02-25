---
title: Claude Code 七大组件深度拆解：从入门到真正会用
date: 2026-02-25 10:00:00
tags:
  - Claude Code
  - AI工具
  - 开发工具
categories:
  - 杂谈
  - 技术研究
cover: /img/claude-code-seven-components-deep-dive/00_cover.png
abbrlink: claude-code-components
---

![封面](/img/claude-code-seven-components-deep-dive/00_cover.png)

> 先用一个类比搞懂全局，再逐个击破，最后串联成完整工作流

---

## 为什么写这篇

![为什么写这篇](/img/claude-code-seven-components-deep-dive/01_why_write_this.png)

Claude Code 的功能越来越多，但大多数人只会用最基础的对话。问题不是工具不强，而是**组件太多、关系不清楚、不知道该从哪个开始**。

这篇文章把 Claude Code 的七大核心组件一次性讲透：它们分别是什么、怎么配、什么时候该用哪个。文末附完整的协同工作流图和推荐上手顺序。

---

## 全局类比：Claude Code 是一个什么结构？

![全局类比](/img/claude-code-seven-components-deep-dive/02_global_analogy.png)

把 Claude Code 想象成一个**新员工入职系统**：

| 组件 | 类比 | 一句话说明 |
|------|------|----------|
| **CLAUDE.md** | 项目交接文档 | 告诉AI"这个项目是什么、怎么做" |
| **Commands/Skills** | 标准操作手册 | 把高频操作固化成一键命令 |
| **MCP** | 办公软件账号 | 让AI连接GitHub、数据库等外部工具 |
| **Hooks** | 自动化规则 | "每次提交前必须跑lint"这种强制规则 |
| **Subagents** | 专项小组 | 把任务委派给专家，结果汇总给你 |
| **Plugins** | 入职大礼包 | 一键安装别人配好的全套工具 |

> 注：2026年2月起，Claude Code 已将 **Skills 和 Slash Commands 合并为同一套系统**。`.claude/commands/` 目录仍然兼容，但官方推荐统一使用 Skills。本文将两者合并讲解。

---

## 1. CLAUDE.md — 项目记忆

![CLAUDE.md](/img/claude-code-seven-components-deep-dive/03_claude_md.png)

### 是什么

项目根目录下的 Markdown 文件，Claude Code **每次启动自动读取**。相当于给AI的"项目说明书"，是所有其他组件的基础。

### 三层加载机制

```
~/.claude/CLAUDE.md          → 全局（所有项目生效，写你个人的编码偏好）
项目根目录/CLAUDE.md          → 项目级（最重要，写项目架构和规范）
子目录/CLAUDE.md              → 模块级（比如 frontend/CLAUDE.md）
```

三层**累加生效**，不会互相覆盖。

### 快速创建

```bash
cd your-project
claude        # 启动 Claude Code
/init         # 自动扫描项目，生成 CLAUDE.md
```

`/init` 会分析项目结构自动生成，但通常需要你手动补充。

### 该写什么

一份好的 CLAUDE.md 应该包含以下内容：

```markdown
# 项目名称

## 项目概述
一句话说清楚这个项目做什么、用什么技术栈

## 目录结构
src/、tests/、docs/ 各放什么，关键文件在哪

## 技术栈
语言版本、框架、数据库、依赖管理工具

## 编码规范
命名风格、注释要求、Git commit 格式

## 常用命令
构建: npm run build
测试: npm test
部署: npm run deploy

## 注意事项
哪些文件不能改、哪些目录有特殊用途、已知的坑
```

### 进阶玩法

- **自动维护**：安装 `claude-code-auto-memory` 插件，Claude 会在每次会话后自动更新 CLAUDE.md
- **自我进化**：在 CLAUDE.md 底部加一段"当你发现新的项目模式时，建议更新此文件"，让AI主动维护

### 投入产出比

**10分钟配置，之后每次对话质量直接翻倍。** 没有 CLAUDE.md 的 Claude Code 就像没看过项目文档的新人——每次都要重新解释一遍上下文。

---

## 2. Skills（含 Commands）— 工作流模板

![Skills](/img/claude-code-seven-components-deep-dive/04_skills.png)

### 是什么

Skills 是可复用的指令模板，有两种触发方式：
- **你手动调用**：输入 `/skill-name` 触发
- **Claude 自动匹配**：根据任务描述自动加载相关 Skill

2026年起，Skills 和原来的 Slash Commands **已合并为同一套系统**。

### 存放位置

```
.claude/skills/<skill-name>/SKILL.md    → 项目级
~/.claude/skills/<skill-name>/SKILL.md  → 全局
```

每个 Skill 就是一个文件夹 + 一个 SKILL.md 文件。

### 核心格式

```markdown
---
name: code-review
description: '代码审查，检查质量、安全性和可维护性。当用户提到代码审查、review时自动激活。'
---

# 代码审查工作流

## 审查清单
1. 检查是否有明显的 bug 或逻辑错误
2. 检查安全漏洞（SQL注入、XSS等）
3. 检查性能问题（N+1查询、内存泄漏）
4. 检查代码风格是否符合项目规范
5. 检查测试覆盖率

## 输出格式
- 严重程度：🔴 严重 / 🟡 警告 / 🟢 建议
- 每个问题附上修复建议
```

### 控制谁能调用

两个关键字段：

```markdown
---
description: '生产环境部署'
disable-model-invocation: true    # 只有你能调用，Claude不能自动触发
---
```

```markdown
---
description: '遗留系统架构说明'
user-invocable: false             # 只有Claude自动调用，你不需要手动触发
---
```

- `disable-model-invocation: true` → 适合有副作用的操作（部署、发消息）
- `user-invocable: false` → 适合背景知识（系统架构说明、编码规范）

### 高效加载机制

Skills 采用**渐进式加载**——启动时只加载 frontmatter（约100 tokens），完整内容在实际激活时才读取。所以不用担心 Skill 太多会拖慢启动。

### 实用 Skill 示例

**Git 提交规范：**
```markdown
---
name: git-commit
description: 'Git提交规范。当用户要提交代码、写commit message时自动激活。'
---
# Git Commit 规范
格式: <type>(<scope>): <subject>
type: feat|fix|docs|style|refactor|test|chore
scope: 影响的模块名
subject: 50字以内，中文描述
示例: feat(auth): 添加OAuth2.0登录支持
```

**API 接口开发：**
```markdown
---
name: api-development
description: 'RESTful API开发规范。当涉及接口设计、路由配置、请求处理时自动激活。'
---
# API 开发规范
- 统一使用 RESTful 风格
- 响应格式: { code: 0, data: {}, message: "success" }
- 错误处理: 统一通过中间件捕获
- 必须编写对应的 API 测试
```

### 与旧版 Commands 的关系

旧版 `.claude/commands/*.md` 文件仍然兼容，但官方推荐迁移到 Skills。Skills 比 Commands 多了自动匹配、控制调用权限、渐进加载等能力。

---

## 3. MCP — 外部工具接口

![MCP](/img/claude-code-seven-components-deep-dive/05_mcp.png)

### 是什么

**Model Context Protocol**，一个开放协议，让 Claude Code 能调用外部工具和服务。比如让它直接操作 GitHub、查数据库、控制浏览器。

Claude Code 内置了文件读写、Shell 命令等基础工具，MCP 让你可以无限扩展。

### 添加 MCP Server

```bash
# 添加 GitHub（管理仓库、创建PR）
claude mcp add github -- npx -y @anthropic-ai/mcp-github

# 添加文件系统（访问指定目录）
claude mcp add filesystem -- npx -y @anthropic-ai/mcp-filesystem ~/data

# 添加 Puppeteer（网页自动化）
claude mcp add puppeteer -- npx -y @anthropic-ai/mcp-puppeteer

# 查看已安装
claude mcp list
```

### 配置文件

MCP 配置存储在 `~/.claude.json`：

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@anthropic-ai/mcp-github"],
      "env": {
        "GITHUB_TOKEN": "your-token"
      }
    }
  }
}
```

### 2026年重要更新：MCP Tool Search

**这是大多数指南没提到的关键特性。**

以前每装一个 MCP Server，它的所有工具定义都会加载到上下文窗口中。装十个 MCP Server 可能吃掉几千 tokens，还没开始干活就浪费了上下文。

现在 Claude Code 支持 **MCP Tool Search**——工具定义按需加载。当 Claude 需要操作 GitHub 时，它才去搜索 GitHub 相关的工具，而不是一开始就加载所有工具。上下文占用最多减少 95%。

### 装多少合适

官方建议：**2-3个 MCP Server 就够了**。一个用于版本控制（GitHub），一个用于你的主要外部服务，按需加一个领域特定的。贪多不如精。

---

## 4. Hooks — 事件钩子

![Hooks](/img/claude-code-seven-components-deep-dive/06_hooks.png)

### 是什么

在 Claude Code 的特定生命周期事件发生时，**自动执行的 shell 命令**。

关键区别：**Prompt 是建议，Hook 是保证。** 你在提示词里说"每次改完代码都跑一下lint"，Claude 有时候会忘。但 Hook 设定了就一定执行，没有例外。

### 支持的事件

| 事件 | 触发时机 | 典型用途 |
|------|---------|---------|
| `PreToolUse` | 工具调用**之前** | 拦截危险操作、安全检查 |
| `PostToolUse` | 工具调用**之后** | 自动格式化、自动lint |
| `Stop` | Claude 完成响应时 | 发送桌面通知 |
| `SubagentStop` | 子代理完成时 | 记录子代理结果 |
| `Notification` | 通知事件 | 自定义通知 |

### 配置位置

`.claude/settings.json` 或 `.claude/settings.local.json`

### 人人都该配的第一个 Hook：任务完成通知

当 Claude 完成一个耗时任务时，你可能已经切到别的窗口了。这个 Hook 让你收到桌面通知：

**macOS：**
```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code 任务完成！\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

**Linux：**
```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "notify-send 'Claude Code' '任务完成！'"
          }
        ]
      }
    ]
  }
}
```

### 代码修改后自动 lint

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '.tool_input.file_path' | xargs npx eslint --fix"
          }
        ]
      }
    ]
  }
}
```

每次 Claude 写入或编辑文件后，自动对该文件跑 ESLint 修复。`matcher` 用正则匹配工具名，`Write|Edit` 表示匹配写入和编辑操作。

### 安全拦截

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "./scripts/security-check.sh"
          }
        ]
      }
    ]
  }
}
```

Hook 命令通过 stdin 接收 JSON 格式的输入，包含即将执行的命令信息。脚本返回**退出码2**可以阻止操作执行。

### 2026年新增

最新版本新增了 `last_assistant_message` 字段，Stop 和 SubagentStop 事件现在可以直接获取 Claude 的最终响应文本，不再需要解析 transcript 文件。

---

## 5. Subagents — 分身术

![Subagents](/img/claude-code-seven-components-deep-dive/07_subagents.png)

### 是什么

独立的 Claude 实例，拥有**独立的上下文窗口**。主 Agent 把任务委派给它们，只拿回最终结果。

### 为什么需要

这是 Subagent 最大的价值：**上下文隔离**。

当你让 Claude 浏览50个文件去找一个 Bug，这50个文件会留在对话上下文中，持续占用空间。如果交给 Subagent 去做，只有最终的定位结果返回到你的主对话，那50个文件留在 Subagent 自己的工作区。

### 三个内置 Subagent

Claude Code 自带三个子代理，不需要额外配置：

| 子代理 | 模型 | 权限 | 适用场景 |
|--------|------|------|---------|
| **通用子代理** | Sonnet | 读+写 | 复杂任务（既要查又要改） |
| **Plan 子代理** | Sonnet | 只读 | 进入Plan模式时自动激活，研究代码库后出方案 |
| **Explore 子代理** | Haiku | 只读 | 快速查找文件和代码片段 |

### 自定义 Subagent

```bash
mkdir -p .claude/agents
```

```markdown
<!-- .claude/agents/code-reviewer.md -->
---
name: code-reviewer
description: 审查代码的质量、安全性和可维护性。在代码修改后主动进行审查。
tools: [Read, Grep, Glob, Bash]
model: sonnet
---

你是一个资深代码审查专家。

## 审查重点
1. 安全漏洞（注入、XSS、权限绕过）
2. 性能问题（N+1查询、内存泄漏、不必要的计算）
3. 代码质量（可读性、DRY原则、单一职责）
4. 边界情况处理（空值、异常、并发）

## 输出格式
每个问题包含：文件路径 → 行号 → 问题描述 → 修复建议 → 严重程度
```

```markdown
<!-- .claude/agents/researcher.md -->
---
name: researcher
description: 研究代码库结构和实现细节，为主Agent提供精简的分析报告。
tools: [Read, Grep, Glob]
model: haiku
---

你是一个代码库探索专家。你的任务是快速定位相关文件和代码模式，
返回精简的摘要报告，不要返回大段代码原文。
```

### 创建方式

除了手动创建文件，也可以在 Claude Code 中输入 `/agents`，通过交互式向导创建。

### 调用方式

```
# Claude自动判断使用哪个子代理（推荐）
帮我审查一下最近的代码变更

# 显式指定
使用 code-reviewer 子代理审查 src/auth/ 目录的代码

# 后台运行（独有能力）
# 按 Ctrl+B 可以把当前任务送到后台，继续做别的事
```

### 什么时候用 Skill，什么时候用 Subagent

- **Skill**：改变当前对话中 Claude 的工作方式（代码风格、审查标准、输出格式）
- **Subagent**：把任务委派给另一个独立的工作者（代码研究、深度审查、文档生成）

简单说：**Skill 改变规则，Subagent 分担工作。**

---

## 6. Plugins — 预制技能包

![Plugins](/img/claude-code-seven-components-deep-dive/08_plugins.png)

### 是什么

把 Skills + Subagents + Hooks + MCP 配置**打包成一个可安装单元**的分发机制。

### 一组数字

截至 2026 年 2 月：
- **9,000+** 个可用插件
- 社区最活跃的插件 `claude-workflow-v2` 有 **1.2K Stars**
- 安全审计插件 `claude-code-safety-net` 有 **920 Stars**

### 基本操作

```bash
# 添加社区市场
/plugin marketplace add affaan-m/everything-claude-code

# 安装插件
/plugin install everything-claude-code@everything-claude-code

# 查看已安装
/plugin list

# 禁用/启用
/plugin disable <plugin-name>
/plugin enable <plugin-name>

# 本地测试开发中的插件
claude --plugin-dir ./my-plugin
```

### 推荐安装

| 插件 | Stars | 功能 |
|------|-------|------|
| `everything-claude-code` | 50K+ | 13个子代理 + 40+ Skills + Hooks，最全面的配置集 |
| `claude-code-safety-net` | 920 | 安全网，拦截危险的git和文件系统命令 |
| `claude-workflow-v2` | 1.2K | 通用工作流，含代理、Skills、Hooks、Commands |
| `cartographer` | 420 | 用并行子代理扫描和文档化整个代码库 |
| `design-plugin` | 440 | UI设计决策辅助，快速迭代 |

### 插件结构

如果你想自己做插件：

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json      # 元数据（名称、版本、描述）
├── skills/              # Skills
│   └── my-skill/
│       └── SKILL.md
├── agents/              # 子代理
│   └── reviewer.md
├── hooks/               # Hooks
│   └── hooks.json
├── commands/            # 命令（兼容旧格式）
│   └── deploy.md
└── .mcp.json            # MCP 配置
```

**重要：** `commands/`、`agents/`、`skills/`、`hooks/` 这些目录放在插件根目录，**不要**放进 `.claude-plugin/` 里面。`.claude-plugin/` 里面只放 `plugin.json`。

---

## 7. 全局串联：七大组件的协同工作流

![协同工作流](/img/claude-code-seven-components-deep-dive/09_workflow.png)

一个真实的开发场景——"实现一个新功能并提交PR"：

```
CLAUDE.md
│  提供项目上下文：技术栈、目录结构、编码规范
│
├─→ 你输入 /plan-feature 用户通知系统
│   （Skills 触发，进入Plan模式）
│
├─→ Plan Subagent 启动
│   用只读权限扫描代码库，返回现有架构分析
│
├─→ Claude 制定实现方案
│
├─→ 开始编码
│   ├─ PostToolUse Hook：每次写文件自动跑 ESLint
│   ├─ code-reviewer Subagent：后台审查已写的代码
│   └─ MCP (GitHub)：获取团队的PR模板和Issue描述
│
├─→ /commit 触发提交
│   ├─ git-commit Skill 自动匹配，生成规范的commit message
│   └─ PreToolUse Hook：提交前自动跑测试
│
├─→ Stop Hook：任务完成，桌面弹出通知
│
└─→ 这整套流程来自一个 Plugin，团队成员一键安装即可共享
```

---

## 八、推荐上手路径

![推荐上手路径](/img/claude-code-seven-components-deep-dive/10_learning_path.png)

不要试图一次性配好所有组件。按这个顺序来：

### 第一天：打好基础（15分钟）

| 步骤 | 操作 | 效果 |
|------|------|------|
| 1 | 在项目根目录运行 `/init` 生成 CLAUDE.md | 每次对话质量翻倍 |
| 2 | 手动补充项目特定信息 | Claude 真正理解你的项目 |

### 第一周：建立工作流（30分钟）

| 步骤 | 操作 | 效果 |
|------|------|------|
| 3 | 创建 2-3 个高频 Skills | 重复操作一键化 |
| 4 | 配置「任务完成通知」Hook | 不用再盯着终端 |
| 5 | 添加 1 个最需要的 MCP | 连接外部工具 |

### 第二周：进阶配置（30分钟）

| 步骤 | 操作 | 效果 |
|------|------|------|
| 6 | 创建 1-2 个自定义 Subagent | 代码审查、文档研究自动化 |
| 7 | 配置 PostToolUse Hook 自动 lint | 代码质量自动保障 |
| 8 | 安装 1-2 个社区插件 | 站在巨人肩膀上 |

### 长期：持续优化

- 根据使用情况持续丰富 Skills
- CLAUDE.md 定期更新（或用插件自动维护）
- 团队协作：把配置做成 Plugin 分发给队友

---

## 九、常见误区

![常见误区](/img/claude-code-seven-components-deep-dive/11_misconceptions.png)

**❌ "Skills 越多越好"**
→ Skills 只在激活时加载完整内容，数量多不影响启动速度。但描述写得太模糊会导致误匹配。每个 Skill 的 description 要精准。

**❌ "MCP 装得越多越强"**
→ 每个 MCP Server 都有上下文开销。官方建议 2-3 个就够。MCP Tool Search 缓解了这个问题，但精简仍是好习惯。

**❌ "Hook 和提示词效果一样"**
→ 提示词是建议，Hook 是强制。需要100%执行的规则（lint、测试、安全检查）必须用 Hook。

**❌ "Subagent 什么任务都该用"**
→ 简单任务直接让主 Agent 做就行。Subagent 的优势是上下文隔离，适合需要读大量文件的任务（研究代码库、深度审查、文档生成）。顺序任务比并行任务更省 token。

**❌ "CLAUDE.md 写一次就不用管了"**
→ 项目在演进，CLAUDE.md 也要跟着更新。推荐装 `claude-code-auto-memory` 插件让 Claude 自动维护。

---

## 参考资源

![参考资源](/img/claude-code-seven-components-deep-dive/12_references.png)

| 资源 | 链接 |
|------|------|
| Claude Code 官方文档 | https://code.claude.com/docs/en/ |
| 插件创建指南 | https://code.claude.com/docs/en/plugins |
| Subagents 文档 | https://code.claude.com/docs/en/sub-agents |
| Skills vs MCP vs Plugins 指南 | https://www.morphllm.com/claude-code-skills-mcp-plugins |
| everything-claude-code（最全插件） | https://github.com/affaan-m/everything-claude-code |
| awesome-claude-code（社区精选） | https://github.com/hesreallyhim/awesome-claude-code |
| 2026最新资源合集 | https://www.scriptbyai.com/claude-code-resource-list/ |
| Claude Code 完全指南（中文） | https://www.cnblogs.com/knqiufan/p/19449849 |

---

*本文基于 Claude Code 2026年2月最新版本撰写。Skills/Commands合并、MCP Tool Search、9000+插件市场等均为最新特性。*
