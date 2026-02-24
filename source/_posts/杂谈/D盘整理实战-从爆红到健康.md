---
title: D盘整理实战：从"爆红"到"健康"
date: 2026-02-05 22:30:00
tags:
  - Windows
  - 磁盘清理
  - D盘整理
  - 存储优化
categories:
  - 杂谈
  - 技术分享
cover: /img/linux.png
abbrlink: d-disk-cleanup
---

## 前言

继C盘整理之后，我的D盘也亮起了红灯——使用率一度高达70%，剩余空间仅80GB。作为一个存放了大量开发环境、虚拟机和项目文件的磁盘，D盘的混乱程度比C盘更甚。本文记录了D盘整理的全过程，包括如何识别大文件、判断文件去留，以及最终释放出45GB空间的过程。

<!-- more -->

## 一、D盘的危急状态

### 1.1 初始诊断

打开D盘属性，情况不容乐观：

```
总容量：277 GB
已用：196 GB (70.9%)
剩余：81 GB
状态：🟡 较满
```

**根目录下的"巨头"们：**

| 排名 | 文件夹 | 大小 | 类型 |
|------|--------|------|------|
| 🥇 | Documents | 65.85 GB | 文档/虚拟机 |
| 🥈 | anaconda | 52.46 GB | Python环境 |
| 🥉 | Adobe | 11.68 GB | 设计软件 |
| 4 | Downloads | 11.39 GB | 下载目录 |
| 5 | Program Files | 8.52 GB | 安装软件 |

光是前两项就占了**118GB**，超过D盘总容量的40%！

### 1.2 混乱的征兆

- **Adobe文件夹**：After Effects、Premiere Pro、Photoshop全套安装，但221天未使用
- **arcgis**：GIS软件，689天（近2年）未碰
- **尹纪元创建的很有用文件**：名字很有趣，但264天未动
- **Downloads**：111个安装包散落各处，有些已经安装过
- **神秘视频文件**：4.4GB的.ts文件，文件名长达100+字符

## 二、深度扫描：找出真正的"空间杀手"

### 2.1 Documents文件夹揭秘（65.85GB）

**Virtual Machines（31.76GB）**
```
Ubuntu 64位虚拟机
├── .vmem（内存快照）: 12.12 GB
├── .vmdk（虚拟磁盘）×6: 19.63 GB
└── 配置文件: 极小
```
**状态**：7天前还在更新，正在使用中 ✅保留

**Tencent Files（12.71GB）**
```
4个QQ号的聊天文件
├── 1808009002: 12.7 GB（主账号）
└── 其他3个小号: ~0.9 GB
```
**状态**：聊天记录，虽然大但必须保留 ✅保留

**计算机类电子书（7.42GB）**
- PDF技术书籍合集
- 242天未打开
- **决策**：可归档到移动硬盘 🟡待处理

### 2.2 anaconda环境分析（52.46GB）

**目录结构：**
```
anaconda/
├── envs（虚拟环境）: 24.68 GB
│   ├── myPytorch: 8.69 GB 🔥
│   ├── yolo_env: 7.68 GB 🔥
│   ├── illegal_building_det: 5.23 GB
│   ├── use_labelimg: 1.57 GB
│   ├── ChatGPT: 0.82 GB
│   ├── paddle310: 0.14 GB
│   └── temp: 0.41 GB
└── pkgs（包缓存）: 18.76 GB 🗑️
```

**关键发现**：
- `pkgs`是包缓存，不是环境！类似npm的node_modules缓存
- 8个虚拟环境中，4个超过1年未用
- `illegal_building_det`环境对应C盘已删除的项目

### 2.3 散落的大文件

| 文件 | 大小 | 位置 | 决策 |
|------|------|------|------|
| Windows.iso | 4.64 GB | Documents\ | 🗑️ 可删 |
| 视频文件.ts | 4.40 GB | Downloads\ | 🗑️ 可删 |
| Origin2025b.zipx | 2.17 GB | Documents\Origin 2025b\ | 🗑️ 可删 |

## 三、整理过程：艰难的取舍

### 3.1 第一轮：清理明显废弃的项目

**删除清单：**
- ✅ Adobe After Effects (3.76GB) - 8个月未用
- ✅ Adobe Premiere Pro (4.29GB) - 8个月未用  
- ✅ Adobe Photoshop (4.49GB) - 8个月未用
- ✅ ArcGIS (3.22GB) - 近2年未用
- ✅ conda包缓存 (4.7GB) - `conda clean --all`
- ✅ illegal_building_det环境 (5.23GB) - 项目已删
- ✅ temp环境 (0.41GB) - 临时环境

**释放：~26GB**

### 3.2 第二轮：清理安装包和冗余文件

**Downloads大扫除：**
- 发现111个安装包(.exe/.msi/.zip)
- 包括：Chrome、Claude、Cursor、爱奇艺、MathType等
- 大部分是已安装软件的安装包

**删除清单：**
- ✅ 111个安装包 (~3.5GB)
- ✅ PythonProject (2.39GB) - 7个月未动
- ✅ 豆包APP (0.6GB) - 近1年未用
- ✅ idea_workspace (0.38GB) - Java项目，1.4年未动

**释放：~7GB**

### 3.3 第三轮：清理大文件

**删除清单：**
- ✅ Windows.iso (4.64GB) - 可从官网下载
- ✅ 尹纪元创建的很有用文件 (1.32GB) - 名字有趣但无用
- ✅ Origin2025b.zipx (2.17GB) - 安装包已解压
- ✅ 视频文件.ts (4.4GB) - 不需要了

**释放：~12GB**

## 四、遇到的坑和解决方案

### 坑1：conda pkgs vs envs 的误解

**问题**：以为pkgs(18.76GB)是虚拟环境的一部分，不敢删。

**真相**：
- `pkgs` = 包缓存（下载的安装包）
- `envs` = 真正的虚拟环境

**解决**：`conda clean --all` 安全清理，不影响现有环境。

### 坑2：VMware和Git的"伪废弃"

**问题**：文件夹显示470天、504天未修改，差点误删。

**真相**：
- VMware进程正在运行！确实在用
- Git在系统PATH中，每天都在用

**教训**：不能只看修改时间，要检查进程和PATH。

### 坑3：重复文件扫描的误导

**问题**：扫描发现大量含"copy"、"backup"、"old"的文件。

**真相**：
- 大部分是软件正常文件（如copy-webpack-plugin）
- 真正的用户备份文件很少

**教训**：关键词匹配会产生大量误报，需要人工甄别。

## 五、最终成果

### 5.1 数据对比

| 指标 | 整理前 | 整理后 | 变化 |
|------|--------|--------|------|
| 已用空间 | 196 GB | 151 GB | -45 GB ✅ |
| 剩余空间 | 81 GB | 126 GB | +45 GB ✅ |
| 使用率 | 70.9% | 54% | -16.9% ✅ |
| 状态 | 🟡 较满 | 🟢 健康 | 质变 ✅ |

### 5.2 保留的项目

**必须保留的"巨头"：**
- Virtual Machines (31.76GB) - Ubuntu开发环境
- anaconda环境 (48GB) - 6个Python环境近期会用
- Tencent Files (12.71GB) - 聊天记录
- SPSS (1.23GB) - 统计分析软件
- 滴答清单 - 确实在用

**用户数据：**
- Downloads剩余文件夹 (~7GB) - 项目数据，自己管理
- 百度网盘 - 正在运行

## 六、经验与建议

### 6.1 D盘管理原则

1. **开发环境隔离**
   - 使用conda/venv隔离项目
   - 定期`conda clean --all`清理缓存
   - 删除环境时记得清理对应pkgs

2. **虚拟机管理**
   - 关闭虚拟机时`.vmem`文件会自动删除
   - 不用的虚拟机及时删除，磁盘快照很占空间
   - 考虑将虚拟机迁移到移动硬盘

3. **下载目录定期清理**
   - 安装包用完即删
   - 大文件及时归档
   - 每月检查一次Downloads

### 6.2 判断文件去留的准则

| 条件 | 操作 |
|------|------|
| 进程正在运行 | ✅ 保留 |
| 在系统PATH中 | ✅ 保留 |
| 1年内未用且可重新下载 | 🗑️ 删除 |
| 项目已结束 | 🗑️ 删除 |
| 安装包已解压 | 🗑️ 删除 |
| 聊天记录/个人数据 | ✅ 保留 |

### 6.3 实用命令

```powershell
# 查看文件夹大小
Get-ChildItem D:\ -Directory | ForEach-Object {
    $size = (Get-ChildItem $_.FullName -Recurse -ErrorAction SilentlyContinue | 
            Measure-Object -Property Length -Sum).Sum
    [PSCustomObject]@{ Name=$_.Name; SizeGB=[math]::Round($size/1GB,2) }
} | Sort-Object SizeGB -Descending

# 查找大文件
Get-ChildItem D:\ -Recurse -File -ErrorAction SilentlyContinue | 
    Where-Object { $_.Length -gt 1GB } | 
    Select-Object Name, @{N='SizeGB';E={[math]::Round($_.Length/1GB,2)}}, FullName

# 检查进程
Get-Process | Where-Object { $_.ProcessName -match "vmware|git|baidu" }
```

## 七、结语

D盘整理历时较长，因为涉及大量开发环境和个人数据的取舍。相比C盘的"系统+缓存"，D盘的"项目+环境"更复杂，需要更多人工判断。

**最大的收获：**
- 理清了conda的pkgs和envs区别
- 建立了"进程检查"的习惯，避免误删正在使用的软件
- D盘从"较满"恢复到"健康"状态

**下一步：**
E盘还有196GB的微信文件和其他数据等待整理...

---

**附录：删除明细清单**

| 序号 | 项目 | 大小 | 删除原因 |
|------|------|------|----------|
| 1 | Adobe Ae/Pr/Ps | 11.7 GB | 8个月未用 |
| 2 | ArcGIS | 3.2 GB | 近2年未用 |
| 3 | conda pkgs缓存 | 4.7 GB | 可重建 |
| 4 | illegal_building_det环境 | 5.2 GB | 项目已删 |
| 5 | temp环境 | 0.4 GB | 临时环境 |
| 6 | 111个安装包 | 3.5 GB | 已安装 |
| 7 | PythonProject | 2.4 GB | 7个月未动 |
| 8 | 豆包 | 0.6 GB | 近1年未用 |
| 9 | idea_workspace | 0.4 GB | 1.4年未动 |
| 10 | Windows.iso | 4.6 GB | 可下载 |
| 11 | 尹纪元文件 | 1.3 GB | 无用 |
| 12 | Origin安装包 | 2.2 GB | 已解压 |
| 13 | 视频文件 | 4.4 GB | 不需要 |
| **合计** | | **~45 GB** | |

---

*本文作者：Administrator*  
*整理时间：2026-02-05*  
*系统环境：Windows 11 + D盘277GB*
