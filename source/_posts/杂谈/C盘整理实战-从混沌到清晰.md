---
title: C盘整理实战：从混沌到清晰
date: 2026-02-05 21:00:00
tags:
  - Windows
  - 系统优化
  - 磁盘清理
  - 经验分享
categories:
  - 杂谈
  - 技术分享
cover: /img/riji.png
abbrlink: c-disk-cleanup
---

## 前言

作为一名开发者，我的C盘就像一个工作了多年的工坊——工具堆积、材料乱放、角落里还藏着不知道何时留下的"神秘文件"。某天打开文件资源管理器，发现C盘根目录杂乱无章，Desktop居然占用了35.9GB，这让我决定进行一次彻底的整理。本文记录了整个过程，包括遇到的问题、解决方案，以及对Windows文件系统的深度认知。

<!-- more -->

## 一、混乱的现状

### 1.1 初始诊断

打开C盘根目录，映入眼帘的是一片"狼藉"：

```
C:\
├── $WINDOWS.~BT          ← 不知何年何月的系统升级残留
├── app                    ← 空文件夹，名字莫名其妙
├── tmp                    ← 里面还有claude、kimi子文件夹
├── FFOutput               ← 格式工厂输出，躺着162MB的直播回放
├── Python312              ← 7.88GB的Python环境
├── 图吧工具箱              ← 512天未更新的老工具
├── ...还有各种零散文件
```

**Desktop更夸张**——35.9GB！里面躺着：
- `学习空间`（18.5GB）：开学项目、考研复试、六级考试...
- `code`（17.2GB）：suo_50、illegal build、test...

### 1.2 第一次震撼：AppData的庞然大物

在分析过程中，我发现了两个"隐形巨兽"：

```powershell
AppData\Local    : 47 GB
AppData\Roaming  : 39 GB
```

**合计86GB！** 占了我C盘已用空间的40%以上。

这让我意识到：**原来我的C盘不是因为系统大，而是因为"缓存"和"数据"在疯狂膨胀。**

## 二、整理过程中遇到的坑

### 2.1 坑一：删除时遇到"Incorrect function"

当尝试删除`学习空间\开学项目\比赛`文件夹时，PowerShell报错了：

```powershell
Remove-Item : Cannot remove item ...\nul: Incorrect function.
```

**问题原因**：某些文件或目录名包含Windows保留字（如`NUL`、`CON`、`AUX`等），或者文件系统出现了特殊状态。

**解决方案**：使用CMD的`rmdir`命令，它对这些边缘情况兼容性更好：

```batch
cmd /c "rmdir /s /q \"C:\Users\...\比赛\""
```

### 2.2 坑二：路径不存在——幽灵文件夹

在分析过程中，我发现有些文件夹"时有时无"：
- `Desktop\学习空间\六级考试` - 扫描显示3.71GB，实际路径不存在
- `Desktop\code\illegal build` - 同样找不到

**问题原因**：这些文件夹在我扫描后、执行前，已经被手动清理，或者是之前残留的扫描缓存数据。

**教训**：在执行删除前，务必**二次确认路径存在性**，避免误删或空操作。

### 2.3 坑三：AppData里的"无名英雄"

在分析AppData\Roaming时，发现了一个神秘的`TDAppDesktop`文件夹，占用5.9GB。

**排查过程**：
1. 看名字猜不出是什么
2. 查看子目录，有`WebApp`、`Cache`、`Code Cache`等
3. 结合`users`子目录和文件结构，推测是**腾讯文档桌面版**

**启示**：很多应用的数据文件夹命名不规范（不是`Tencent Docs`而是`TDAppDesktop`），需要靠经验和技术手段识别。

### 2.4 坑四：大小计算时的异常

在使用PowerShell计算文件夹大小时，经常遇到：

```powershell
Measure-Object : The property "Length" cannot be found in the input for any objects.
```

**问题原因**：某些特殊文件或系统文件没有`Length`属性（如系统卷信息、符号链接等）。

**解决方案**：使用`-ErrorAction SilentlyContinue`跳过异常，或者使用`try-catch`处理。

## 三、核心发现：Local vs Roaming 的真相

在整理过程中，我对Windows的用户数据存储机制有了深度认知。

### 3.1 两大分区的本质区别

```
AppData\
├── Local      (本地)    → "换台电脑就不需要的东西"
└── Roaming    (漫游)    → "换台电脑还要带着走的东西"
```

**Local的典型内容**：
- 应用缓存（Chrome的11GB缓存）
- 临时文件（npm-cache 2.4GB）
- 大型数据（WSL Ubuntu 15GB）
- 机器特定配置（GPU缓存）

**Roaming的典型内容**：
- 应用配置（VSCode设置）
- 聊天记录（微信/QQ 14GB）
- 用户数据（WPS云文档5GB）
- 登录凭证（加密存储）

### 3.2 记忆口诀

> **Local = Local (本地) = 大、临时、可删**
> 
> **Roaming = Roam (漫游) = 配置、记录、保留**

**简单三步判断**：
1. **是缓存吗？** → Local → 可删
2. **是配置吗？** → Roaming → 保留
3. **是聊天记录吗？** → Roaming → 谨慎删

### 3.3 为什么我的Roaming比Local还大？

正常用户Roaming只有几GB，我的却有39GB。原因在于：

| 因素 | 说明 |
|------|------|
| 聊天重度用户 | 微信/QQ/飞书多年积累 |
| 多开发工具 | VSCode、Trae、Cursor、JetBrains各自一套配置 |
| 办公云同步 | WPS 5GB云文档数据 |
| 没有清理习惯 | 从未主动清理过聊天记录 |

## 四、实战清理过程

### 4.1 第一轮：Desktop大瘦身

**清理清单**：
- `学习空间\开学项目\比赛`（6.67GB）→ 竞赛已结束
- `学习空间\六级考试`（3.71GB）→ 已过级，资料不再需要
- `学习空间\开学项目\考研复试`（2.12GB）→ 已上岸
- `code\illegal build`（3.86GB）→ 项目已完成

**释放空间**：~18GB

**经验**：Desktop是"工作区"，不是"仓库"。完成的文件应该归档到D盘或云盘，不要长期占据桌面。

### 4.2 第二轮：根目录杂项清理

**清理清单**：
- `$WINDOWS.~BT`（6KB）→ 系统升级残留
- `tmp`（2.15MB）→ Kimi/Claude临时文件
- `app`（空）→ 不明空文件夹
- `FFOutput`（162MB）→ 格式工厂输出

**释放空间**：~164MB（虽小，但清爽）

### 4.3 决策：哪些不动？

**保留的项目**：
- **Python312（7.88GB）**：PyTorch 4.3GB + Paddle 0.4GB，AI开发必需
- **WSL虚拟机（22.2GB）**：ext4.vhdx文件，Linux开发环境
- **Chrome缓存（11GB）**：用户决定保留，不清理
- **聊天记录（14GB）**：情感价值，保留

## 五、最终成果

### 5.1 数据对比

| 指标 | 清理前 | 清理后 | 变化 |
|------|--------|--------|------|
| Desktop | 35.9 GB | 17.6 GB | -18.3 GB ✅ |
| 根目录杂乱文件夹 | 4个 | 0个 | -164 MB ✅ |
| C盘使用率 | ~57% | ~51% | -6% ✅ |
| 剩余空间 | ~163 GB | ~186 GB | +23 GB ✅ |

### 5.2 结构优化

**清理后的C盘结构**：

```
C:\
├── 🔴 Windows/               ~20GB (系统，不动)
├── 🔴 Program Files/         ~18GB (软件，不动)  
├── 🔴 Program Files (x86)/   ~11GB (软件，不动)
├── 🟡 Python312/             7.9GB (开发环境，保留)
├── 🟡 Users/Administrator/   ~130GB (用户数据)
│   ├── Desktop/              17.6GB (精简后)
│   ├── AppData/Local/        47GB (WSL+缓存)
│   ├── AppData/Roaming/      39GB (配置+聊天记录)
│   └── ...
└── 🟢 剩余可用空间           ~186GB
```

### 5.3 健康度评估

- **使用率**：51% 🟢 健康
- **文件组织**：清晰 ✅
- **可清理潜力**：~15GB（Chrome缓存等，可选）

## 六、经验与建议

### 6.1 给开发者的建议

1. **WSL和Docker是空间杀手**
   - WSL的ext4.vhdx文件会不断增长
   - 建议定期`wsl --shutdown`并压缩，或迁移到D盘

2. **Python环境管理**
   - 使用conda/venv隔离项目，避免在base环境乱装包
   - PyTorch+CUDA动辄4-5GB，不用的版本及时卸载

3. **缓存管理意识**
   - npm/pip缓存可以定期清理：`npm cache clean`、`pip cache purge`
   - IDE缓存（VSCode、JetBrains）可以设置自动清理

### 6.2 给普通用户的建议

1. **Desktop不是仓库**
   - 正在处理的文件放桌面
   - 完成的文件移到Documents或D盘
   - 定期归档"已完成"文件夹

2. **了解AppData**
   - Local里的缓存可以大胆清理
   - Roaming里的聊天记录谨慎删除
   - 卸载软件后，手动检查残留数据

3. **工具推荐**
   - **WinDirStat**：可视化磁盘占用，一眼看出大文件
   - **TreeSize**：快速扫描，比Windows资源管理器快10倍
   - **PowerShell**：`Get-ChildItem | Measure-Object`，精准分析

### 6.3 清理checklist

**可以安全删除的**：
- [ ] `$WINDOWS.~BT` - 系统升级残留
- [ ] `Windows\Temp` - 系统临时文件
- [ ] `C:\tmp` - 自定义临时文件夹
- [ ] `%TEMP%` - 用户临时文件
- [ ] Chrome/Edge缓存
- [ ] npm/pip缓存
- [ ] 应用崩溃转储（CrashDumps）
- [ ] 缩略图缓存

**不建议删除的**：
- [ ] `C:\Windows` - 系统核心
- [ ] `C:\Program Files` - 已安装软件
- [ ] `AppData\Roaming`里的聊天记录
- [ ] `.git`目录（版本控制）
- [ ] `venv`/`node_modules`（项目依赖）

## 七、结语

这次C盘整理历时数小时，释放了18GB+空间，更重要的是建立了对Windows文件系统的深度认知。

**最大的收获不是空间，而是"知道什么东西在哪里，能不能删"的掌控感。**

从最初的"根目录好乱"，到最后的"结构清晰"，这个过程不仅是技术操作，更是一次数字生活的断舍离。

**下一步**：D盘使用率已达88.8%，仅剩30GB...新的挑战开始了。

---

**附录：实用命令**

```powershell
# 快速扫描大文件夹
Get-ChildItem C:\Users\$env:USERNAME -Recurse -ErrorAction SilentlyContinue | 
    Group-Object Directory | 
    Select-Object Name, @{N='SizeGB';E={[math]::Round((($_.Group | Measure-Object Length -Sum).Sum/1GB),2)}} | 
    Sort-Object SizeGB -Descending | 
    Select-Object -First 20

# 查看AppData大小
(Get-ChildItem $env:LOCALAPPDATA -Recurse -ErrorAction SilentlyContinue | 
    Measure-Object -Property Length -Sum).Sum / 1GB

(Get-ChildItem $env:APPDATA -Recurse -ErrorAction SilentlyContinue | 
    Measure-Object -Property Length -Sum).Sum / 1GB
```

---

*本文作者：Administrator*  
*整理时间：2026-02-05*  
*系统环境：Windows 11 + WSL2 + Python 3.12*
