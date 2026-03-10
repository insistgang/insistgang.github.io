# 📦 insistgang.top 博客项目信息

---

## 📋 项目基本信息

```
博客名称: Leo的笔记本
博客域名: insistgang.top
技术框架: Hexo 7.3.0
主题: Butterfly
作者: insistgang
语言: 简体中文 (zh-CN)
```

---

## 🏗️ 技术栈

### 核心框架
- **Hexo**: 7.3.0
- **Node.js**: >= 18.x

### 主题
- **Butterfly**: 官方主题
- **模板引擎**: Pug
- **样式**: Stylus

### 已安装插件

#### 基础功能
- `hexo-abbrlink`: 文章链接生成（使用 crc32 + hex）
- `hexo-browsersync`: 浏览器实时刷新
- `hexo-generator-index`: 首页生成
- `hexo-generator-archive`: 归档页生成
- `hexo-generator-category`: 分类页生成
- `hexo-generator-tag`: 标签页生成
- `hexo-renderer-marked`: Markdown 渲染
- `hexo-renderer-ejs`: EJS 渲染
- `hexo-renderer-pug`: Pug 渲染
- `hexo-renderer-stylus`: Stylus 样式渲染
- `hexo-server`: 本地服务器
- `hexo-util`: 工具函数

#### 搜索功能
- `hexo-generator-search`: 本地搜索
- `hexo-generator-sitemap`: Sitemap 生成
- `hexo-generator-feed`: RSS 订阅

#### 部署
- `hexo-deployer-git`: Git 部署

#### 主题增强插件
- `hexo-butterfly-article-double-row`: 双栏文章布局
- `hexo-butterfly-artitalk-pro`: 评论系统
- `hexo-butterfly-footer-beautify`: 页脚美化
- `hexo-butterfly-git-gitcalendar`: Git 日历
- `hexo-electric-clock`: 电子时钟
- `hexo-history-calendar`: 历史日历
- `hexo-swiper-bar`: Swiper 滚动条

#### 其他
- `hexo-wordcount`: 字数统计
- `hexo-helper-live2d`: Live2D 看板娘
- `live2d-widget-model-hibiki`: Live2D 模型
- `live2d-widget-model-tororo`: Live2D 模型
- `moment-timezone`: 时区处理

---

## 📁 项目结构

```
E:\000\Hexo\
├── .deploy_git/          # 部署缓存
├── .git/                 # Git 仓库
├── node_modules/         # 依赖包
├── public/               # 生成的静态文件
├── scaffolds/            # 文章模板
├── source/               # 源文件
│   ├── _posts/          # 文章目录
│   │   ├── c语言/
│   │   ├── database/
│   │   ├── datastruct/
│   │   ├── Linux/
│   │   └── python/
│   ├── _drafts/         # 草稿
│   ├── about/           # 关于页面
│   ├── categories/      # 分类页面
│   ├── tags/            # 标签页面
│   ├── music/           # 音乐页面
│   ├── Gallery/         # 照片页面
│   ├── movies/          # 电影页面
│   ├── link/            # 友链页面
│   └── archives/        # 归档页面
├── themes/               # 主题
│   └── butterfly/       # Butterfly 主题
│       ├── layout/      # 模板文件
│       │   ├── includes/
│       │   │   ├── header/
│       │   │   │   ├── nav.pug          # 导航栏
│       │   │   │   └── menu_item.pug    # 菜单项
│       │   │   ├── footer.pug           # 页脚
│       │   │   └── ...
│       │   ├── index.pug                # 首页
│       │   ├── post.pug                 # 文章页
│       │   ├── archive.pug              # 归档页
│       │   ├── category.pug             # 分类页
│       │   └── tag.pug                  # 标签页
│       ├── source/      # 静态资源
│       │   └── css/
│       │       ├── _layout/
│       │       │   └── head.styl        # 导航栏样式
│       │       └── ...
│       └── _config.yml  # 主题配置
├── _config.yml           # 站点配置
├── _config.butterfly.yml # Butterfly 主题配置
├── package.json          # 依赖管理
├── deploy.sh             # 部署脚本
└── vercel.json           # Vercel 配置
```

---

## ⚙️ 配置详情

### 站点配置 (_config.yml)

```yaml
# 基本信息
title: Leo的笔记本
author: insistgang
language: zh-CN
timezone: ''

# URL
url: https://insistgang.top
permalink: posts/:abbrlink.html  # 使用 abbrlink 生成短链接
abbrlink:
  alg: crc32
  rep: hex

# 目录
source_dir: source
public_dir: public

# 写作
new_post_name: :title.md
post_asset_folder: true  # 启用文章资源文件夹
highlight:
  enable: true
  line_number: true
  wrap: true

# 首页
index_generator:
  per_page: 10

# 主题
theme: butterfly

# 部署
deploy:
  type: git
  repo:
    github: https://github.com/insistgang/insistgang.github.io.git,master
  branch: hexo
```

### Butterfly 主题配置 (_config.butterfly.yml)

```yaml
# 导航菜单
menu:
  首页: / || fas fa-home
  时间轴: /archives/ || fas fa-archive
  标签: /tags/ || fas fa-tags
  分类: /categories/ || fas fa-folder-open
  清单:
    音乐: /music/ || fas fa-music
    照片: /Gallery/ || fas fa-images
    电影: /movies/ || fas fa-video
  友链: /link/ || fas fa-link
  关于: /about/ || fas fa-heart

# 代码高亮
highlight_theme: mac
highlight_copy: true
highlight_lang: true
highlight_shrink: false

# 搜索
local_search:
  enable: true

# 社交图标
social:
  fab fa-github: https://github.com/insistgang || Github
  fas fa-envelope: mailto:insistgang@163.com || Email

# 头像
avatar:
  img: /img/toux.jpg
  effect: false

# 封面图
cover:
  index_enable: true
  aside_enable: true
  archives_enable: true
  position: both

# 字数统计
wordcount:
  enable: true
  post_wordcount: true
  min2read: true
  total_wordcount: true

# 文章摘要
index_post_content:
  method: 3  # auto_excerpt
  length: 500

# 目录
toc:
  post: true
  number: true
  expand: false

# 赞赏
reward:
  enable: true
  QR_code:
    - img: /img/wechat.jpg
      text: 微信
    - img: /img/alipay.jpg
      text: 支付宝
```

---

## 📊 内容统计

根据网站抓取结果：
- **文章总数**: 146 篇
- **总字数**: 167.2k 字
- **标签数量**: 74 个
- **分类数量**: 15 个
- **活跃度**: 高（2026年2月单月51篇）

---

## 🎨 设计特点

### 视觉风格
- **极简主义**: 无图片封面，纯文字驱动
- **高信息密度**: 侧边栏聚合大量信息
- **Butterfly 主题**: 现代化设计，响应式布局

### 导航结构
```
顶部导航: 首页 | 时间轴 | 标签 | 分类 | 清单 | 友链 | 关于
侧边栏: 统计 | 最新文章 | 分类 | 标签云 | 归档 | 网站信息
功能模块: 音乐/照片/电影清单
```

### 特色功能
- ✅ **Live2D 看板娘**: Hibiki + Tororo 模型
- ✅ **电子时钟**: 页面显示实时时间
- ✅ **Git 日历**: 展示提交历史
- ✅ **双栏布局**: 文章页双栏显示
- ✅ **字数统计**: 每篇文章显示字数和阅读时间
- ✅ **赞赏功能**: 微信/支付宝二维码

---

## ⚠️ 当前问题

### 高优先级
1. **移动端导航体验**: 导航栏在移动端可能重复显示
2. **代码块优化**: 需要优化移动端显示和样式
3. **统计功能**: 页脚访客数/浏览量显示为 0
4. **SEO 优化**: 需要添加 meta description 和 Open Graph 标签

### 中优先级
5. **摘要截断**: 部分文章截断在代码处
6. **搜索功能**: 虽已安装插件，但需要优化体验
7. **RSS 订阅**: 已安装插件，需要确认是否正常工作

### 低优先级
8. **特色图**: 文章列表纯文字，可以添加缩略图
9. **标签云权重**: 未按使用频率调整字体大小
10. **相关推荐**: 文章页缺少相关内容推荐

---

## 🎯 优化建议

### 立即执行
1. **移动端导航优化**
   - 检查导航栏重复问题
   - 优化汉堡菜单体验

2. **代码块样式优化**
   - 添加语言标识
   - 优化移动端横向滚动
   - 调整高亮主题

3. **统计功能修复**
   - 接入不蒜子统计
   - 或使用 LeanCloud + Valine

### 1-2周内
4. **SEO 优化**
   - 添加 meta description
   - 添加 Open Graph 标签
   - 优化 sitemap

5. **搜索功能优化**
   - 优化搜索框位置
   - 改进搜索结果展示

### 长期迭代
6. **视觉增强**
   - 添加文章特色图
   - 优化标签云权重
   - 添加相关文章推荐

---

## 📝 给 Claude Code 的提示词

```
我有一个 Hexo 博客项目（insistgang.top），使用 Butterfly 主题。

项目信息：
- Hexo 版本: 7.3.0
- 主题: Butterfly
- 已安装插件: hexo-abbrlink, hexo-generator-search, hexo-wordcount 等
- 文章数量: 146篇
- 当前问题: 移动端导航、代码块样式、统计功能等

请帮我分析项目并提供优化方案。

我提供的文件：
1. _config.yml (站点配置)
2. _config.butterfly.yml (主题配置)
3. package.json (依赖列表)
4. nav.pug (导航栏模板)
5. menu_item.pug (菜单项模板)
6. footer.pug (页脚模板)
7. head.styl (导航栏样式)

请先分析现状，然后给出优化建议。
```

---

## 🚀 常用命令

```bash
# 本地预览
hexo server

# 生成静态文件
hexo generate

# 清理缓存
hexo clean

# 部署
hexo deploy

# 完整部署流程
hexo clean && hexo generate && hexo deploy
```

---

## 📞 下一步

现在我已经完整了解了你的项目：

✅ **项目识别完成**
- 框架: Hexo 7.3.0
- 主题: Butterfly
- 插件: 已安装 20+ 个插件
- 内容: 146篇文章，167k字

✅ **问题已识别**
- 移动端导航
- 代码块样式
- 统计功能
- SEO 优化

**你可以：**
1. 让我生成具体的优化提示词给 Claude Code
2. 让我直接提供优化代码
3. 让我分析特定文件并给出建议

告诉我你想先优化哪个功能？🚀
