# 🎯 给 Claude Code 的完整提示词（针对你的 Butterfly 博客）

---

## 📋 核心提示词

```
你是一个专业的 Hexo 博客开发者和 Butterfly 主题专家，请帮我分析和优化我的博客项目。

## 📊 项目信息

### 基本信息
- 博客名称: Leo的笔记本
- 博客域名: insistgang.top
- 技术框架: Hexo 7.3.0
- 主题: Butterfly
- 作者: insistgang
- 语言: 简体中文 (zh-CN)

### 技术栈
- **核心框架**: Hexo 7.3.0 + Node.js >= 18.x
- **主题**: Butterfly (Pug 模板 + Stylus 样式)
- **已安装插件**:
  - 基础: hexo-abbrlink, hexo-generator-index, hexo-renderer-marked
  - 搜索: hexo-generator-search, hexo-generator-sitemap, hexo-generator-feed
  - 部署: hexo-deployer-git
  - Butterfly 增强: hexo-butterfly-article-double-row, hexo-butterfly-artitalk-pro, hexo-electric-clock, hexo-history-calendar
  - 其他: hexo-wordcount, hexo-helper-live2d

### 内容规模
- 文章总数: 146 篇
- 总字数: 167.2k 字
- 标签数量: 74 个
- 分类数量: 15 个
- 活跃度: 高（2026年2月单月51篇）

### 当前配置
- **URL 格式**: `posts/:abbrlink.html` (使用 crc32 + hex 生成短链接)
- **代码高亮**: mac 主题，显示行号，支持复制
- **搜索功能**: 本地搜索已启用
- **字数统计**: 已启用（文章字数 + 阅读时间）
- **特色功能**: Live2D 看板娘、电子时钟、Git 日历、双栏布局、赞赏功能

## ⚠️ 当前问题（按优先级排序）

### 🔴 高优先级
1. **移动端导航体验**
   - 问题: 导航栏在移动端可能重复显示或布局不合理
   - 影响: 移动端用户体验差，空间浪费
   - 位置: `themes/butterfly/layout/includes/header/nav.pug` + `head.styl`

2. **代码块样式优化**
   - 问题: 移动端代码块可能溢出，样式不够美观
   - 影响: 技术文章阅读体验不佳
   - 位置: `themes/butterfly/source/css/_highlight/` 相关样式

3. **统计功能异常**
   - 问题: 页脚访客数/浏览量显示为 0
   - 影响: 缺少网站数据展示
   - 位置: `themes/butterfly/layout/includes/footer.pug`

4. **SEO 基础优化**
   - 问题: 缺少 meta description、Open Graph 标签
   - 影响: 搜索引擎收录和社交分享效果差
   - 位置: `themes/butterfly/layout/includes/head.pug`

### 🟠 中优先级
5. **摘要截断问题**
   - 问题: 部分文章摘要截断在代码块中间
   - 影响: 首页文章列表显示不完整
   - 配置: `index_post_content.method: 3` (auto_excerpt)

6. **搜索功能优化**
   - 问题: 搜索框位置和搜索结果展示可以优化
   - 影响: 用户查找内容效率低
   - 位置: `themes/butterfly/layout/includes/header/nav.pug`

7. **RSS 订阅确认**
   - 问题: 已安装 hexo-generator-feed，需要确认是否正常工作
   - 影响: 订阅用户可能无法获取更新

### 🟢 低优先级
8. **文章特色图**
   - 问题: 文章列表纯文字，缺少视觉吸引力
   - 影响: 列表页单调
   - 配置: `cover.index_enable: true`

9. **标签云权重**
   - 问题: 标签云未按使用频率调整字体大小
   - 影响: 无法直观看出热门标签

10. **相关文章推荐**
    - 问题: 文章页缺少相关内容推荐
    - 影响: 用户停留时间短

## 📁 我提供的文件内容

### 1. 站点配置 (_config.yml)
```yaml
# Hexo Configuration
title: Leo的笔记本
subtitle: ''
description: ''
keywords: ''
author: insistgang
language: zh-CN
timezone: ''

# URL
url: https://insistgang.top
permalink: posts/:abbrlink.html
abbrlink:
    alg: crc32
    rep: hex

# Writing
highlight:
  enable: true
  line_number: true
  wrap: true

# Home page
index_generator:
  per_page: 10

# Theme
theme: butterfly

# Deployment
deploy:
  type: git
  repo:
    github: https://github.com/insistgang/insistgang.github.io.git,master
  branch: hexo
```

### 2. Butterfly 主题配置 (_config.butterfly.yml)
```yaml
# Menu
menu:
  首页: / || fas fa-home
  时间轴: /archives/ || fas fa-archive
  标签: /tags/ || fas fa-tags
  分类: /categories/ || fas fa-folder-open
  清单||fa fa-heartbeat:
    音乐: /music/ || fas fa-music
    照片: /Gallery/ || fas fa-images
    电影: /movies/ || fas fa-video
  友链: /link/ || fas fa-link
  关于: /about/ || fas fa-heart

# Code Blocks
highlight_theme: mac
highlight_copy: true
highlight_lang: true
highlight_shrink: false
code_word_wrap: true

# Search
local_search:
  enable: true

# Social
social:
    fab fa-github: https://github.com/insistgang || Github
    fas fa-envelope: mailto:insistgang@163.com || Email

# Avatar
avatar:
  img: /img/toux.jpg
  effect: false

# Cover
cover:
  index_enable: true
  aside_enable: true
  archives_enable: true
  position: both

# Wordcount
wordcount:
  enable: true
  post_wordcount: true
  min2read: true
  total_wordcount: true

# Post excerpt
index_post_content:
  method: 3
  length: 500

# TOC
toc:
  post: true
  number: true
  expand: false

# Reward
reward:
  enable: true
  QR_code:
    - img: /img/wechat.jpg
      text: 微信
    - img: /img/alipay.jpg
      text: 支付宝
```

### 3. 依赖列表 (package.json)
```json
{
  "hexo": {
    "version": "7.3.0"
  },
  "dependencies": {
    "hexo": "^7.3.0",
    "hexo-abbrlink": "^2.2.1",
    "hexo-browsersync": "^0.3.0",
    "hexo-butterfly-article-double-row": "^1.0.2",
    "hexo-butterfly-artitalk-pro": "^1.0.5",
    "hexo-butterfly-footer-beautify": "^1.0.6",
    "hexo-butterfly-git-gitcalendar": "^1.1.0",
    "hexo-deployer-git": "^3.0.0",
    "hexo-electric-clock": "^1.1.0",
    "hexo-generator-archive": "^1.0.0",
    "hexo-generator-category": "^1.0.0",
    "hexo-generator-feed": "^3.0.0",
    "hexo-generator-index": "^2.0.0",
    "hexo-generator-search": "^2.4.3",
    "hexo-generator-sitemap": "^2.2.0",
    "hexo-generator-tag": "^1.0.0",
    "hexo-helper-live2d": "^3.1.1",
    "hexo-history-calendar": "^1.0.3",
    "hexo-renderer-marked": "^4.0.0",
    "hexo-renderer-pug": "^3.0.0",
    "hexo-renderer-stylus": "^3.0.1",
    "hexo-server": "^2.0.0",
    "hexo-swiper-bar": "^1.1.1",
    "hexo-wordcount": "^6.0.1",
    "live2d-widget-model-hibiki": "^1.0.5",
    "live2d-widget-model-tororo": "^1.0.5"
  }
}
```

### 4. 导航栏模板 (nav.pug)
```pug
nav#nav
  span#blog-info
    a.nav-site-title(href=url_for('/'))
      if theme.nav.logo
        img.site-icon(src=url_for(theme.nav.logo) alt='Logo')
      if theme.nav.display_title
        span.site-name=config.title
    if globalPageType === 'post' && theme.nav.display_post_title
      a.nav-page-title(href=url_for('/'))
        span.site-name=(page.title || config.title)
        span.site-name
          i.fa-solid.fa-circle-arrow-left
          span= '  ' + _p('post.back_to_home')

  #menus
    if theme.search.use
      #search-button
        span.site-page.social-icon.search
          i.fas.fa-search.fa-fw
          span= ' ' + _p('search.title')
    if theme.menu
      != partial('includes/header/menu_item', {}, {cache: true})

      #toggle-menu
        span.site-page
          i.fas.fa-bars.fa-fw
```

### 5. 菜单项模板 (menu_item.pug)
```pug
if theme.menu
  .menus_items
    each value, label in theme.menu
      if typeof value !== 'object'
        .menus_item
          - const [link, icon] = value.split('||').map(part => trim(part))
          a.site-page(href=url_for(link))
            if icon
              i.fa-fw(class=icon)
            span= ' ' + label
      else
        .menus_item
          - const [groupLabel, groupIcon, groupClass] = label.split('||').map(part => trim(part))
          - const hideClass = groupClass === 'hide' ? 'hide' : ''
          span.site-page.group(class=hideClass)
            if groupIcon
              i.fa-fw(class=groupIcon)
            span= ' ' + groupLabel
            i.fas.fa-chevron-down
          ul.menus_item_child
            each val, lab in value
              - const [childLink, childIcon] = val.split('||').map(part => trim(part))
              li
                a.site-page.child(href=url_for(childLink))
                  if childIcon
                    i.fa-fw(class=childIcon)
                  span= ' ' + lab
```

### 6. 页脚模板 (footer.pug)
```pug
- const { nav, owner, copyright, custom_text } = theme.footer

if nav
  .footer-flex
    for block in nav
      .footer-flex-items(style=`${ block.width ? 'flex-grow:' + block.width : '' }`)
        for blockItem in block.content
          .footer-flex-item
            .footer-flex-title= blockItem.title
            .footer-flex-content
              for subitem in blockItem.item
                if subitem.html
                  div!= subitem.html
                else if subitem.url
                  a(href=url_for(subitem.url), target='_blank' title=subitem.title)= subitem.title
                else if subitem.title
                  div!= subitem.title
.footer-other
  .footer-copyright
    if owner.enable
      - const currentYear = new Date().getFullYear()
      - const sinceYear = owner.since
      span.copyright
        if sinceYear && sinceYear != currentYear
          != `&copy;&nbsp;${sinceYear} - ${currentYear} By ${config.author}`
        else
          != `&copy;&nbsp;${currentYear} By ${config.author}`
    if copyright.enable
      - const v = copyright.version ? getVersion() : false
      span.framework-info
        if owner.enable && nav
          span.footer-separator |
        span= _p('footer.framework') + ' '
        a(href='https://hexo.io')= `Hexo${ v ? ' ' + v.hexo : '' }`
        span.footer-separator |
        span= _p('footer.theme') + ' '
        a(href='https://github.com/jerryc127/hexo-theme-butterfly')= `Butterfly${ v ? ' ' + v.theme : '' }`
  if theme.footer.custom_text
    .footer_custom_text!= theme.footer.custom_text
```

### 7. 导航栏样式 (head.styl)
```stylus
#nav
  position: absolute
  top: 0
  z-index: 90
  display: flex
  align-items: center
  padding: 0 36px
  width: 100%
  height: 60px
  font-size: 1.3em
  opacity: 0
  transition: all .5s

  +maxWidth768()
    padding: 0 16px

  &.show
    opacity: 1

  #blog-info
    flex: 1
    color: var(--light-grey)
    @extend .limit-one-line

  #toggle-menu
    display: none
    padding: 2px 0 0 6px
    vertical-align: top

  &.hide-menu
    #toggle-menu
      display: inline-block !important

    .menus_items
      display: none

  .site-page
    position: relative
    padding-bottom: 6px
    text-shadow: 1px 1px 2px rgba($dark-black, .3)
    font-size: .78em
    cursor: pointer
```

## 🎯 你的任务

### 第一次回复：全面分析报告

请帮我分析以下内容：

1. **项目结构分析**
   - 评估 Butterfly 主题的可定制性
   - 分析已安装插件的合理性和冲突
   - 检查配置文件的最佳实践

2. **问题诊断**
   - 详细分析我列出的每个问题
   - 指出可能的根因（基于提供的文件内容）
   - 评估影响范围和优先级

3. **优化建议清单**
   - 按优先级排序（高/中/低）
   - 说明每个优化的预期效果
   - 估算实施难度（简单/中等/复杂）
   - 提供实施步骤概览

4. **技术方案推荐**
   - 移动端导航：推荐的技术方案（响应式断点、汉堡菜单优化）
   - 代码高亮：推荐的样式优化方案
   - 统计功能：推荐使用不蒜子还是 LeanCloud
   - SEO 优化：推荐的 meta 标签配置

### 后续回复：具体代码实现

当我提出具体优化需求时，请提供：

1. **完整的代码实现**
   - 配置文件修改（YAML/JSON）
   - 模板文件修改（Pug）
   - 样式文件修改（Stylus/CSS）
   - JavaScript 脚本（如果需要）

2. **详细的配置说明**
   - 每个配置项的作用
   - 可选参数说明
   - 注意事项

3. **完整的实施步骤**
   - 文件修改步骤
   - 配置调整步骤
   - 测试验证步骤

4. **测试验证方法**
   - 本地测试命令
   - 预期效果说明
   - 常见问题排查

## 📝 代码要求

- ✅ 兼容 Hexo 7.3.0 和 Butterfly 主题
- ✅ 提供完整可执行的代码（不要省略）
- ✅ 注释清晰易懂（说明每段代码的作用）
- ✅ 考虑移动端适配（响应式设计）
- ✅ 保持 Butterfly 主题风格（不要过度修改）
- ✅ 性能优化（减少加载时间，懒加载等）
- ✅ 无障碍友好（ARIA 标签，键盘导航）

## 📤 输出格式

### 分析报告格式
```markdown
## 一、项目概况
- 主题版本: Butterfly
- Hexo 版本: 7.3.0
- 已安装插件: xxx
- 主要问题: xxx

## 二、问题分析
### 1. 移动端导航体验
- 根因: [分析]
- 影响: [说明]
- 解决方案: [建议]

[继续分析其他问题...]

## 三、优化建议
### 🔴 高优先级
1. 移动端导航优化
   - 预期效果: 移动端体验 +100%
   - 实施难度: 中等
   - 实施步骤: [简要说明]

[继续列出其他优化...]

## 四、技术方案推荐
### 移动端导航
推荐: [具体方案]
理由: [说明]
```

### 代码实现格式
```yaml
# 1. _config.butterfly.yml 配置
mobile_nav:
  enable: true
  breakpoint: 768
```

```pug
// 2. nav.pug 修改
#toggle-menu.mobile-only
  i.fas.fa-bars
```

```stylus
/* 3. head.styl 样式 */
+maxWidth768()
  #nav
    padding: 0 16px
    
  #toggle-menu
    display: block
```

```javascript
// 4. mobile-nav.js 脚本
document.getElementById('toggle-menu').addEventListener('click', () => {
  // 切换逻辑
});
```

## 🚀 开始吧！

请先分析我的项目，然后给出详细的优化建议。

我会根据你的建议，逐项要求你提供具体的代码实现。

---

## 💡 额外说明

- 我的博客内容价值很高（167k字深度技术内容），优化重点是"让用户更容易找到和消费优质内容"
- 我希望保持 Butterfly 主题的现代风格，不要过度修改
- 我会逐项实施优化，所以请提供可独立执行的代码
- 如果某些优化需要权衡（如功能 vs 性能），请说明利弊

**请开始分析！** 🎯
```

---

## 📋 使用说明

### 步骤 1：复制完整提示词
1. 复制上面的完整提示词
2. 发送给 Claude Code

### 步骤 2：等待分析报告
Claude Code 会给你：
- ✅ 项目结构分析
- ✅ 问题诊断
- ✅ 优化建议清单
- ✅ 技术方案推荐

### 步骤 3：逐项优化
根据分析报告，选择要优化的功能：

#### 优化 1：移动端导航
```
根据你的分析，我想先优化移动端导航体验。

请提供完整的实现方案，包括：
1. nav.pug 修改
2. menu_item.pug 修改
3. head.styl 样式优化
4. 可能需要的 JavaScript 脚本
5. 测试方法

要求：
- 导航栏固定顶部
- 响应式断点 768px
- 汉堡菜单流畅切换
- 保持 Butterfly 风格
```

#### 优化 2：代码块样式
```
帮我优化代码块显示。

请提供完整的实现方案，包括：
1. _config.butterfly.yml 配置
2. 代码高亮样式优化（Stylus）
3. 移动端横向滚动优化
4. 语言标识显示优化

要求：
- 使用 mac 主题
- 显示语言标识
- 移动端支持横向滚动
- 保持代码可读性
```

#### 优化 3：统计功能
```
帮我接入不蒜子统计。

请提供完整的实现方案，包括：
1. footer.pug 修改
2. 不蒜子脚本集成
3. 样式优化
4. 配置说明

要求：
- 显示访客数和浏览量
- 样式美观
- 不影响页面加载速度
```

#### 优化 4：SEO 优化
```
帮我做全面的 SEO 优化。

请提供完整的实现方案，包括：
1. head.pug 添加 meta 标签
2. Open Graph 标签
3. sitemap.xml 配置
4. robots.txt
5. URL 优化建议

要求：
- 提升搜索引擎排名
- 优化社交分享效果
- 符合 SEO 最佳实践
```

---

## ✅ 检查清单

在发送给 Claude Code 之前：

- [x] 已复制完整的提示词
- [x] 已包含所有配置文件内容
- [x] 已明确优化需求
- [x] 已说明特殊要求（保持 Butterfly 风格）

---

## 🎉 祝你优化顺利！

你的博客内容价值极高，优化后一定会吸引更多读者！🚀
