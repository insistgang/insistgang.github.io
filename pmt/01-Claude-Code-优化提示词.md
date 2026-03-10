# Claude Code 优化提示词模板

## 📋 使用说明

将以下提示词复制给 Claude Code，让它帮你优化博客。根据需要选择对应的提示词。

---

## 🔍 提示词 1：项目分析（首次使用）

```
我有一个 Hexo 博客项目，域名是 insistgang.top。请帮我分析这个项目：

1. 项目结构分析
   - 查看 _config.yml 和主题配置
   - 识别当前使用的主题
   - 分析已安装的插件

2. 需要你检查的文件：
   - _config.yml（站点配置）
   - themes/[主题名]/_config.yml（主题配置）
   - package.json（依赖）
   - source/_posts/ 目录结构

3. 输出要求：
   - 列出当前技术栈
   - 指出潜在问题
   - 给出优化建议清单

请先帮我分析项目现状，然后我会告诉你具体要优化什么。
```

---

## 🔧 提示词 2：添加站内搜索功能

```
帮我为 Hexo 博客添加站内搜索功能。

需求：
1. 使用 hexo-generator-search 插件
2. 搜索框放在导航栏右侧
3. 支持实时搜索（输入即搜索）
4. 搜索结果高亮显示

具体步骤：
1. 安装插件：npm install hexo-generator-search --save
2. 在 _config.yml 添加配置
3. 在主题的 header.ejs 或 navigation.ejs 添加搜索框
4. 创建搜索页面（search/index.md）
5. 添加搜索样式（CSS）

请提供完整的代码实现，包括：
- _config.yml 配置
- 搜索框 HTML 代码
- 搜索页面模板
- CSS 样式代码
```

---

## 📱 提示词 3：移动端导航优化

```
帮我优化 Hexo 博客的移动端导航体验。

问题：
- 导航栏在移动端重复显示
- 导航项过多，占用空间
- 侧边栏在小屏幕显示不友好

需求：
1. 实现汉堡菜单（☰）切换
2. 移动端隐藏侧边栏，改为抽屉式
3. 导航栏固定在顶部
4. 响应式断点：768px

需要修改的文件：
- themes/[主题名]/layout/_partial/header.ejs
- themes/[主题名]/source/css/style.css 或 main.scss

请提供：
1. 汉堡菜单的 HTML + JavaScript 代码
2. 响应式 CSS 代码（@media query）
3. 移动端导航样式优化
4. 侧边栏抽屉式切换代码
```

---

## 🔍 提示词 4：SEO 优化

```
帮我为 Hexo 博客做全面的 SEO 优化。

需要实现：
1. 添加 meta description（每篇文章）
2. 添加 Open Graph 标签（社交分享）
3. 生成 sitemap.xml
4. 优化 URL 格式（去掉日期）
5. 添加 robots.txt
6. 结构化数据（Article Schema）

具体任务：
1. 安装插件：hexo-generator-sitemap, hexo-generator-robots
2. 修改主题的 head.ejs 添加 meta 标签
3. 配置 _config.yml 优化 URL
4. 为文章模板添加自动 description 生成

请提供：
- 插件安装命令
- _config.yml 配置代码
- head.ejs 修改代码
- 文章 front-matter 示例
```

---

## 📡 提示词 5：RSS 订阅功能

```
帮我为 Hexo 博客添加 RSS 订阅功能。

需求：
1. 生成 atom.xml 订阅源
2. 在页脚添加 RSS 图标链接
3. 支持全文输出

步骤：
1. 安装插件：npm install hexo-generator-feed --save
2. 配置 _config.yml
3. 在 footer.ejs 添加 RSS 图标和链接

请提供：
- 插件配置代码
- 页脚 HTML 代码（带 RSS 图标）
- 测试方法
```

---

## 💬 提示词 6：评论系统优化

```
帮我优化 Hexo 博客的评论系统。

现状：可能同时配置了 Valine 和 Disqus
需求：
1. 统一使用 Waline（Valine 改进版）
2. 添加评论数显示在文章列表
3. 优化评论区域样式

需要：
1. 安装 Waline
2. 修改主题的 comments.ejs
3. 在文章列表添加评论数显示
4. 配置 LeanCloud 后端

请提供：
- Waline 安装和配置步骤
- comments.ejs 代码
- 评论数显示代码
- LeanCloud 配置指南
```

---

## 🎨 提示词 7：代码块样式优化

```
帮我优化 Hexo 博客的代码块显示。

需求：
1. 添加语言标识（如 "Python"、"Shell"）
2. 显示行号
3. 移动端支持横向滚动
4. 优化高亮主题（推荐 One Dark）

需要修改：
1. _config.yml 中的 highlight 配置
2. 主题的代码块 CSS 样式
3. 可能需要自定义代码块模板

请提供：
- highlight 配置代码
- CSS 样式代码（包括移动端优化）
- 语言标识显示代码
```

---

## 📊 提示词 8：统计功能修复

```
帮我修复和优化 Hexo 博客的统计功能。

需求：
1. 接入不蒜子统计（busuanzi）
2. 显示：访客数、浏览量
3. 在页脚显示统计信息

需要：
1. 在 footer.ejs 添加不蒜子脚本
2. 添加统计信息显示代码
3. 样式优化

请提供：
- 不蒜子脚本代码
- 页脚统计显示 HTML
- CSS 样式优化
```

---

## 🖼️ 提示词 9：添加文章特色图

```
帮我为 Hexo 博客添加文章特色图功能。

需求：
1. 每篇文章可配置封面图
2. 首页文章列表显示缩略图
3. 自动从文章内容提取首图（备用方案）

需要：
1. 修改文章 front-matter 支持 cover 字段
2. 修改首页文章列表模板显示图片
3. 添加默认封面图（如果没有配置）

请提供：
- front-matter 示例
- 首页模板修改代码
- 默认封面图处理逻辑
- 响应式图片样式
```

---

## 📁 你需要提供给 Claude Code 的文件

为了让 Claude Code 更好地理解你的项目，建议提供以下文件：

### 必需文件
```
_config.yml                    # 站点配置
package.json                   # 依赖列表
themes/[主题名]/_config.yml    # 主题配置
```

### 可选文件（根据优化需求）
```
themes/[主题名]/layout/_partial/header.ejs    # 头部模板
themes/[主题名]/layout/_partial/footer.ejs    # 页脚模板
themes/[主题名]/layout/index.ejs              # 首页模板
themes/[主题名]/layout/post.ejs               # 文章页模板
themes/[主题名]/source/css/style.css          # 样式文件
source/_posts/某篇文章.md                     # 文章示例
```

---

## 🚀 使用流程

1. **第一步：项目分析**
   - 发送「提示词 1」给 Claude Code
   - 提供 _config.yml 和主题配置
   - 让它分析现状

2. **第二步：选择优化项**
   - 根据分析结果选择要优化的功能
   - 发送对应的提示词

3. **第三步：实施优化**
   - 让 Claude Code 提供具体代码
   - 你负责复制粘贴和测试

4. **第四步：测试验证**
   - 运行 hexo clean && hexo generate
   - 本地预览：hexo server
   - 确认无误后部署

---

## 💡 额外提示

### 给 Claude Code 的通用指令
```
你是一个专业的 Hexo 博客开发者，请帮我优化博客功能。

要求：
1. 代码要兼容 Hexo 最新版本
2. 提供完整的配置和代码
3. 注释清晰，便于我理解
4. 考虑移动端适配
5. 保持代码简洁高效

我的博客信息：
- 域名：insistgang.top
- 框架：Hexo
- 风格：极简技术博客
```

---

## 📞 需要我做什么？

如果你需要我：
1. **生成特定优化的详细提示词** → 告诉我具体需求
2. **分析你提供的配置文件** → 发给我 _config.yml 等文件
3. **提供优化优先级建议** → 告诉我你的目标（流量/体验/美观）

随时告诉我！🚀
