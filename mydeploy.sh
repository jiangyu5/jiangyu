#!/usr/bin/env sh

# 发生错误时终止
set -e

# 删除之前的打包
# npm run clean

# 构建
npm run build

# 进入构建文件夹
cd dist
# git init

# 如果你要部署到自定义域名
echo 'yustudy.cn' > CNAME

# git checkout -b main
git add -A
git commit -m 'deploy'

# 如果你要部署在 https://<USERNAME>.github.io
# git push -f https://github.com/jiangyu5/jiangyu5.github.io.git main
git push -f

# 如果你要部署在 https://<USERNAME>.github.io/<REPO>
# git push -f git@github.com:<USERNAME>/<REPO>.git main:gh-pages

# 以上运行成功就停下
echo 【成功】
read -n 1
echo 继续结束