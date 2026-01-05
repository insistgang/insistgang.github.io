#!/bin/bash
# Hexo 部署脚本 - 自动添加 .nojekyll 文件

# 1. 清理并生成
hexo clean
hexo generate

# 2. 添加 .nojekyll 文件
touch public/.nojekyll

# 3. 部署
hexo deploy

echo "✅ 部署完成！包含 .nojekyll 文件"
