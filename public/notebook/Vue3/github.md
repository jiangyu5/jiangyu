



> https://cn.vitejs.dev/guide/static-deploy.html#github-pages

## vite.config.js

```javascript
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import { resolve } from "path";
import legacy from "@vitejs/plugin-legacy"; // 传统浏览器的支持插件 npm add -D @vitejs/plugin-legacy

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue({ reactivityTransform: true }),

    legacy({
      targets: ["defaults", "not IE 11"],
    }),

  ],

  build: {
    rollupOptions: {
      input: {
        main: resolve(__dirname, "index.html"),
        // main2: resolve(__dirname, "index2/index.html")
      },
      output: { // github无法读取 文件名.hash.后缀 ，
        chunkFileNames: "assets/js/[hash].js",
        entryFileNames: "assets/js/[hash].js",
        assetFileNames: "assets/[ext]/[hash].[ext]",
      },
    },
  },
});
```



## 创建 deploy.sh

```sh
#!/usr/bin/env sh

# 发生错误时终止
set -e

# 构建
npm run build

# 进入构建文件夹
cd dist

# 如果你要部署到自定义域名
# echo 'www.example.com' > CNAME

git init
git checkout -b main
git add -A
git commit -m 'deploy'

# 如果你要部署在 https://<USERNAME>.github.io
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git main

# 如果你要部署在 https://<USERNAME>.github.io/<REPO>
# git push -f git@github.com:<USERNAME>/<REPO>.git main:gh-pages

cd -

```

