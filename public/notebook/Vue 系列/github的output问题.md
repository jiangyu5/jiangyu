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



