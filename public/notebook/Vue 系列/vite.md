阅读前，需要了解

- npm
- npx

## [搭建项目](https://cn.vitejs.dev/guide/#scaffolding-your-first-vite-project)

```shell
$ npm create vite@latest
```

项目配置按照提示操作。

也可以设置参数快速生成项目模板，之后 `npm install`

```shell
# npm 7+, extra double-dash is needed:
$ npm create vite@latest my-vue-app -- --template vue
```



## [命令行](https://cn.vitejs.dev/guide/cli.html)

**开发服务器**

```shell
$ npx vite --host localhost --port 5500 --open
# 如果 host 为 0.0.0.0 或者 true，将监听所有地址，包括局域网和公网地址
# --open 为自动打开
```

> 这些参数也可以通过配置 `vite.config.js` 中的 `server` 项 配置。

**构建**

```shell
$ npx vite build --watch
# 当启用 --watch 标志时，对 vite.config.js 的改动，以及任何要打包的文件，都将触发重新构建。
```

**预览**

```shell
$ npx vite preview
```



## [配置](https://cn.vitejs.dev/config/)

### 配置文件

项目根目录下的 `vite.config.js`

```js
export default {}
```

为了获得只能提示，可以使用 `defineConfig`工具函数。

```js
export default defineConfig({})
```

另外，`defineConfig` 支持根据使用场景，使用不同的配置。这也支持导出异步函数。~~暂时未遇到该需求~~

```js
export default defineConfig(({ command, mode, ssrBuild }) => {
  if (command === 'serve') { // serve 为开发环境
    return {
      // dev 独有配置
    }
  } else {
    // command === 'build'
    return {
      // build 独有配置
    }
  }
})
```



### [共享选项](https://cn.vitejs.dev/config/shared-options.html)

#### root[¶](https://cn.vitejs.dev/config/shared-options.html#root)

- **类型：** `string`
- **默认：** `process.cwd()`

项目根目录（`index.html` 文件所在的位置）。可以是一个绝对路径，或者一个相对于该配置文件本身的相对路径。

#### base[¶](https://cn.vitejs.dev/config/shared-options.html#base)

- **类型：** `string`
- **默认：** `/`

开发或生产环境服务的公共基础路径。合法的值包括以下几种：

- 绝对 URL 路径名，例如 `/foo/`
- 完整的 URL，例如 `https://foo.com/`
- 空字符串或 `./`（用于嵌入形式的开发）

#### plugins[¶](https://cn.vitejs.dev/config/shared-options.html#plugins)

- **类型：** `(Plugin | Plugin[] | Promise<Plugin | Plugin[]>)[]`

需要用到的插件数组。Falsy 虚值的插件将被忽略，插件数组将被扁平化（flatten）。

#### publicDir[¶](https://cn.vitejs.dev/config/shared-options.html#publicdir)

- **类型：** `string | false`
- **默认：** `"public"`

作为静态资源服务的文件夹。该目录中的文件在开发期间在 `/` 处提供，并在构建期间复制到 `outDir` 的根目录，并且始终按原样提供或复制而无需进行转换。该值可以是文件系统的绝对路径，也可以是相对于项目根目录的相对路径。

将 `publicDir` 设定为 `false` 可以关闭此项功能。

#### resolve.extensions[¶](https://cn.vitejs.dev/config/shared-options.html#resolve-extensions)

- **类型：** `string[]`
- **默认：** `['.mjs', '.js', '.mts', '.ts', '.jsx', '.tsx', '.json']`

导入时想要省略的扩展名列表。注意，**不** 建议忽略自定义导入类型的扩展名（例如：`.vue`），因为它会影响 IDE 和类型支持。

#### json.stringify[¶](https://cn.vitejs.dev/config/shared-options.html#json-stringify)

- **类型：** `boolean`
- **默认：** `false`

若设置为 `true`，导入的 JSON 会被转换为 `export default JSON.parse("...")`，这样会比转译成对象字面量性能更好，尤其是当 JSON 文件较大的时候。

开启此项，则会禁用[按名导入](https://cn.vitejs.dev/config/shared-options.html#json-namedexports)。

#### assetsInclude[¶](https://cn.vitejs.dev/config/shared-options.html#assetsinclude)

- **类型：** `string | RegExp | (string | RegExp)[]`

指定额外的 [picomatch 模式](https://github.com/micromatch/picomatch#globbing-features) 作为静态资源处理，因此：

- 当从 HTML 引用它们或直接通过 `fetch` 或 XHR 请求它们时，它们将被插件转换管道排除在外。
- 从 JavaScript 导入它们将返回解析后的 URL 字符串（如果你设置了 `enforce: 'pre'` 插件来处理不同的资产类型，这可能会被覆盖）。

内建支持的资源类型列表可以在 [这里](https://github.com/vitejs/vite/blob/main/packages/vite/src/node/constants.ts) 找到。

```js
export default defineConfig({
  assetsInclude: ['**/*.gltf'],
})
```

#### appType[¶](https://cn.vitejs.dev/config/shared-options.html#apptype)

- **类型：** `'spa' | 'mpa' | 'custom'`
- **默认：** `'spa'`

无论你的应用是一个单页应用（SPA）还是一个 [多页应用（MPA）](https://cn.vitejs.dev/guide/build.html#multi-page-app)，亦或是一个定制化应用（SSR 和自定义 HTML 处理的框架）：

- `'spa'`：包含 HTML 中间件以及使用 SPA 回退。在预览中将 [sirv](https://github.com/lukeed/sirv) 配置为 `single: true`
- `'mpa'`：包含 HTML 中间件
- `'custom'`：不包含 HTML 中间件



### [服务器选项](https://cn.vitejs.dev/config/server-options.html)

#### server.host[¶](https://cn.vitejs.dev/config/server-options.html#server-host)

- **类型：** `string | boolean`
- **默认：** `'localhost'`

指定服务器应该监听哪个 IP 地址。 如果将此设置为 `0.0.0.0` 或者 `true` 将监听所有地址，包括局域网和公网地址。

#### server.https[¶](https://cn.vitejs.dev/config/server-options.html#server-https)

- **类型：** `boolean | https.ServerOptions`

启用 TLS + HTTP/2。注意：当 [`server.proxy` 选项](https://cn.vitejs.dev/config/server-options.html#server-proxy) 也被使用时，将会仅使用 TLS。

这个值也可以是一个传递给 `https.createServer()` 的 [选项对象](https://nodejs.org/api/https.html#https_https_createserver_options_requestlistener)。

需要一个合法可用的证书。对基本使用的配置需求来说，你可以添加 [@vitejs/plugin-basic-ssl](https://github.com/vitejs/vite-plugin-basic-ssl) 到项目插件中，它会自动创建和缓存一个自签名的证书。

#### server.proxy[¶](https://cn.vitejs.dev/config/server-options.html#server-proxy)

- **类型：** `Record<string, string | ProxyOptions>`

为开发服务器配置自定义代理规则。期望接收一个 `{ key: options }` 对象。任何请求路径以 key 值开头的请求将被代理到对应的目标。如果 key 值以 `^` 开头，将被识别为 `RegExp`。`configure` 选项可用于访问 proxy 实例。

请注意，如果使用了非相对的 [基础路径 `base`](https://cn.vitejs.dev/config/shared-options.html#base)，则必须在每个 key 值前加上该 `base`。

使用 [`http-proxy`](https://github.com/http-party/node-http-proxy)。完整选项详见 [此处](https://github.com/http-party/node-http-proxy#options).



### 构建选项

#### build.target[¶](https://cn.vitejs.dev/config/build-options.html#build-target)

- **类型：** `string | string[]`
- **默认：** `'modules'`
- **相关内容：** [浏览器兼容性](https://cn.vitejs.dev/guide/build.html#browser-compatibility)

设置最终构建的浏览器兼容目标。默认值是一个 Vite 特有的值：'modules'`，这是指 [支持原生 ES 模块](https://caniuse.com/es6-module)、[原生 ESM 动态导入](https://caniuse.com/es6-module-dynamic-import) 和 [`import.meta`](https://caniuse.com/mdn-javascript_operators_import_meta) 的浏览器。Vite 将替换 `modules`为`['es2020', 'edge88', 'firefox78', 'chrome87', 'safari14']`

另一个特殊值是 “esnext” —— 即假设有原生动态导入支持，并且将会转译得尽可能小：

- 如果 [`build.minify`](https://cn.vitejs.dev/config/build-options.html#build-minify) 选项为 `'terser'`，`'esnext'` 将会强制降级为 `'es2021'`。
- 其他情况下将完全不会执行转译。

转换过程将会由 esbuild 执行，并且此值应该是一个合法的 [esbuild 目标选项](https://esbuild.github.io/api/#target)。自定义目标也可以是一个 ES 版本（例如：`es2015`）、一个浏览器版本（例如：`chrome58`）或是多个目标组成的一个数组。

#### build.outDir[¶](https://cn.vitejs.dev/config/build-options.html#build-outdir)

- **类型：** `string`
- **默认：** `dist`

指定输出路径（相对于 [项目根目录](https://cn.vitejs.dev/guide/#index-html-and-project-root)).

#### build.assetsDir[¶](https://cn.vitejs.dev/config/build-options.html#build-assetsdir)

- **类型：** `string`
- **默认：** `assets`

指定生成静态资源的存放路径（相对于 `build.outDir`）。

#### build.assetsInlineLimit[¶](https://cn.vitejs.dev/config/build-options.html#build-assetsinlinelimit)

- **类型：** `number`
- **默认：** `4096` (4kb)

小于此阈值的导入或引用资源将内联为 base64 编码，以避免额外的 http 请求。设置为 `0` 可以完全禁用此项。

Git LFS 占位符会自动排除在内联之外，因为它们不包含它们所表示的文件的内容。

#### build.cssCodeSplit[¶](https://cn.vitejs.dev/config/build-options.html#build-csscodesplit)

- **类型：** `boolean`
- **默认：** `true`

启用/禁用 CSS 代码拆分。当启用时，在异步 chunk 中导入的 CSS 将内联到异步 chunk 本身，并在其被加载时插入。

如果禁用，整个项目中的所有 CSS 将被提取到一个 CSS 文件中。

#### build.cssTarget[¶](https://cn.vitejs.dev/config/build-options.html#build-csstarget)

- **类型：** `string | string[]`
- **默认值：** 与 [`build.target`](https://cn.vitejs.dev/config/#build-target) 一致

此选项允许用户为 CSS 的压缩设置一个不同的浏览器 target，此处的 target 并非是用于 JavaScript 转写目标。

应只在针对非主流浏览器时使用。 最直观的示例是当你要兼容的场景是安卓微信中的 webview 时，它支持大多数现代的 JavaScript 功能，但并不支持 [CSS 中的 `#RGBA` 十六进制颜色符号](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#rgb_colors)。 这种情况下，你需要将 `build.cssTarget` 设置为 `chrome61`，以防止 vite 将 `rgba()` 颜色转化为 `#RGBA` 十六进制符号的形式。

#### build.rollupOptions[¶](https://cn.vitejs.dev/config/build-options.html#build-rollupoptions)

- **类型：** [`RollupOptions`](https://rollupjs.org/configuration-options/)

自定义底层的 Rollup 打包配置。这与从 Rollup 配置文件导出的选项相同，并将与 Vite 的内部 Rollup 选项合并。查看 [Rollup 选项文档](https://rollupjs.org/configuration-options/) 获取更多细节。



## [预览选项](https://cn.vitejs.dev/config/preview-options.html)

> 类似 服务器选项

## [静态资源处理](https://cn.vitejs.dev/guide/assets.html)

### 将资源引入为 URL[¶](https://cn.vitejs.dev/guide/assets.html#importing-asset-as-url)

服务时引入一个静态资源会返回解析后的公共路径：

```js
import imgUrl from './img.png'
document.getElementById('hero-img').src = imgUrl
```

例如，`imgUrl` 在开发时会是 `/img.png`，在生产构建后会是 `/assets/img.2d8efhg.png`。

> 默认情况下，TypeScript 不会将静态资源导入视为有效的模块。要解决这个问题，需要添加 [`vite/client`](https://cn.vitejs.dev/guide/features.html#client-types)。

### 显式 URL 引入[¶](https://cn.vitejs.dev/guide/assets.html#explicit-url-imports)

未被包含在内部列表或 `assetsInclude` 中的资源，可以使用 `?url` 后缀显式导入为一个 URL。这十分有用，例如，要导入 [Houdini Paint Worklets](https://houdini.how/usage) 时：

```js
import workletURL from 'extra-scalloped-border/worklet.js?url'
CSS.paintWorklet.addModule(workletURL)
```

### 将资源引入为字符串[¶](https://cn.vitejs.dev/guide/assets.html#importing-asset-as-string)

资源可以使用 `?raw` 后缀声明作为字符串引入。

```js
import shaderString from './shader.glsl?raw'
```



### [导入脚本作为 Worker](https://cn.vitejs.dev/guide/assets.html#importing-script-as-a-worker)



## [构建生产版本](https://cn.vitejs.dev/guide/build.html#multi-page-app)

> 重点学习

