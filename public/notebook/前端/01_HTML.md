## 归属

> [MDN](https://developer.mozilla.org/zh-CN)
>
> 归属于 [Mozilla 贡献者](https://developer.mozilla.org/zh-CN/docs/Learn/HTML)的[署名和版权许可协议](https://developer.mozilla.org/zh-CN/docs/MDN/Writing_guidelines/MDN/Writing_guidelines/Attrib_copyright_license)在[知识共享 署名 - 相同方式共享许可 2.5](https://creativecommons.org/licenses/by-sa/2.5/) 下提供。

上述的  [Mozilla 贡献者](https://developer.mozilla.org/zh-CN/docs/Learn/HTML) 地址为本笔记的学习内容。



## HTMl 简单说明

- HyperText Markup Language

- 超文本标记语言

  - 超文本：指连接单个网站内或多个网站间的网页的链接。
  - 使用“标记”（markup）来注明文本、图片和其他内容，以便于在 Web 浏览器中显示。
  - 不区分大小写。




### 语义

- 有些标签是有含义的，比如 `<h1>`、`<h2>` 被用来表示文章的标题，用来表示一个段落显然是奇怪的。
  - 一般情况下一个页面只存在一个 `<h1>` 表示层级明确。
  - 含有语义的标签一般会有特殊用途，如帮助视力障碍者阅读等。
- 不能忽略标签的语义而随意使用。

**无语义的标签分为两种**

- 不影响样式效果，如 `<div>`。
- 影响样式效果，如 `<i>` 表现为斜体，但无实意。被称为表象元素。

**无语义元素**

`<span>`

- 无语义
- 一般被用来处理一句话中的个别文字效果。

```html
<span style="color: tomato;">张航的笔记</span>
```

> <span>张航的笔记</span>

`<div>`

- 无语义
- 作为容器，方便布局

```html
<div>
	<p>是段落</p>
	<p>是段落</p>
<div>
```

> <div>
> 	<p>是段落</p>
> 	<p>是段落</p>
> <div>



## 文档结构

```html
<!DOCTYPE html>
<html lang="zh-CN">
    <head>
        <meta charset="utf-8">
        <title>张航的笔记</title>
    </head>
	<body></body>
</html>
```



### head

- 里面的内容不会在浏览器中显示；
- 用来保存网页的元数据；
- 一般情况下，至少包含 `<title>` 元素，用来表示该 Html 文档的标题；
- 大型网站拥有很多元数据。

```
<head>
    <title>张航的笔记</title>
</head>
```

#### 元数据 `<meta>`

- 元数据：用来描述数据的数据。

**指定文档的字符编码**

- 一些浏览器会纠正错误的编码。

```html
<meta charset="utf-8">
```

**添加作者和描述**

- `name` 指定了元素类型，说明该元素包含了什么类型的信息。
- `description` 指定了实际元数据内容。

```html
<meta name="author" content="张航">
<meta name="description" content="这是一份学习笔记，见证我的假装努力。">
```

当搜索 `description` 的元数据内容时，搜索引擎的结果会显示该 `content`。

> SEO（搜索引擎优化）：让我们的网站被搜索引擎结果中更加清晰，以便在首批搜索结果中显示。

#### 网页图标

```html
<link rel="icon" href="favicon.ico" type="image/x-icon">
```

更多图标类型

```html
<!-- third-generation iPad with high-resolution Retina display: -->
<link rel="apple-touch-icon-precomposed" sizes="144x144" href="https://developer.mozilla.org/static/img/favicon144.png">
<!-- iPhone with high-resolution Retina display: -->
<link rel="apple-touch-icon-precomposed" sizes="114x114" href="https://developer.mozilla.org/static/img/favicon114.png">
<!-- first- and second-generation iPad: -->
<link rel="apple-touch-icon-precomposed" sizes="72x72" href="https://developer.mozilla.org/static/img/favicon72.png">
<!-- non-Retina iPhone, iPod Touch, and Android 2.1+ devices: -->
<link rel="apple-touch-icon-precomposed" href="https://developer.mozilla.org/static/img/favicon57.png">
<!-- basic favicon -->
<link rel="icon" href="https://developer.mozilla.org/static/img/favicon32.png">
```

#### 样式

```html
<link rel="stylesheet" href="style.css">
```

#### JavaScript 文件

- 一般不放在 `<head>` 中

```html
<js scr="my-js.js"></js>
```



### body

除了个别外，包裹的内容会在浏览器中呈现出来。



## 文本基础

### 标题 `<h1>`

- 语义：标题

- 一般只用到 3 - 4 级标题

```html
<h1>一级标题</h1>
<h2>二级标题</h2>
<h3>三级标题</h3>
<h4>四级标题</h4>
<h5>五级标题</h5>
<h6>六级标题</h6>
```



### 段落 `<p>`

- 语义：段落

```html
<p>这是段落一。</p>
<p>这是段落二，字太少，难道就不像是段落吗？</p>
```

> <p>这是段落一。</p>
> <p>这是段落二，字太少，难道就不像是段落吗？</p>



### 无序列表 `<ul>`

- 表示顺序并不重要的列表

```html
<ul>
	<li>苹果</li>
    <li>香蕉</li>
    <li>樱桃</li>
</ul>
```

> <ul>
> 	<li>苹果</li>
>     <li>香蕉</li>
>     <li>樱桃</li>
> </ul>



### 有序列表 `<ol>`

- 表示需要按照一定顺序排列的列表

```html
<ol>
	<li>学 HTML</li>
	<li>学 CSS</li>
    <li>学 JavaScript</li>
</ol>
```

> <ol>
> 	<li>学 HTML</li>
> 	<li>学 CSS</li>
>     <li>学 JavaScript</li>
> </ol>



### 强调

**斜体** `<em>`

- `<em>` 语义：强调
  - 能够被阅读器识别，并改变音调。
- `<i>` 无语义，单纯的斜体效果。
- 如果是单纯实现斜体效果，使用 `<i>` 或者使用 Css 实现。

```html
<em>斜体</em>
```

> <em>斜体</em>

**重点** `<strong>`

- `<strong>` 语义：重点强调
  - 可以被阅读器识别。
- `<b>` 无语义，单纯是粗体效果

- 如果单纯是为了粗体效果，一般用 `<b>` 或者 css 来实现。

```html
<strong>重点</strong>
或者是
<b>重点</b>
```

> <strong>重点</strong> 或者是 <b>重点</b>



## 超链接

- `title` 链接的标题，一般为简单介绍。
- `href` 代表超文本引用 **h**ypertext **ref**erencetitle
  - `href` 属性如果省略 `http://` 或 `https://`，可能会得到一个错误的结果。
- 要慎重考虑标签内的文本
  - 一般不用 “链接”、“链接到” 等词；
  - 文字要简短；
  - 减少多个连接使用相同文本，如都使用 “单机此处”;
  - 考虑屏幕阅读器，优美简洁。
- 链接到非 HTML 资源，不会在浏览器中打开时要注明。

```html
<a title href="yustudy.cn">张航的主页</a>
```

><a href="yustudy.cn">张航的主页</a>



### **指向到 Url 的特定位置**

```html
<h2 id="title">标题二</h2>
	...
<a href="[URL]#title">阅读标题二</a>
```



### 属性 `download` 

- 保存一个文件

```html
<a href="[URL]" download="[FILE]">点击下载</a>
```



### 电子邮件 `mailto`

- `mailto` 当地址未指向时，只是打开邮件，收件人为空。

```html
<a href="mailto:[URL]">向我发送邮件</a>
```



**设置主题（subject）、抄送（cc）和主体（body）**

- `？` 分隔 URL 和参数值
- `&` 分隔多个参数
- **内容均为 URL 编码，非打印字符，需要先转换**

```html
<a href="mailto:【URL】?cc=【主题内容】&subject=【抄送内容】&body=【主题内容】">像我发送邮件</a>
```



## 高级文本格式

### 描述列表 `<dl>`

- description list
- 每项 `<dt>`：description term
- 每个描述 `<dd>`：description definition
- 一般用在需要描述项目时

```html
<dl>
  <dt>项目一</dt>
	<dd>描述一下</dd>
  <dt>项目二</dt>
    <dd>描述一下</dd>
</dl>
```

> <dl>
>     <dt>项目一</dt>
> 	    <dd>描述一下</dd>
>     <dt>项目二</dt>
>     	<dd>描述一下</dd>
> </dl>



### 块引用 `<blockquote>`

- `cite` 指向引用的资源
- 浏览器并未充分利用 `cite` 属性。如果需要相关功能，需要通过其他标签与样式来重写，如跳转到 URL `地址` ，需要在文档其他地方标注出来。
- 虽然 `cite` 并没有被浏览器充分识别，但还是不能忽略。

```html
<p>励志短语</p>
<blockquote cite="[URL]">
    <p>你只管努力，剩下的交给时间。</p>
</blockquote>
```

> <p>励志短语</p>
> <blockquote cite="[URL]">
>     <p>你只管努力，剩下的交给时间。</p>
> </blockquote>

### 行内引用 `<q>`

- `cite` 指向引用的资源
- 浏览器并未充分利用 `cite` 属性。如果需要相关功能，需要通过其他标签与样式来重写，如跳转到 URL `地址` ，需要在文档其他地方标注出来。
- 虽然 `cite` 并没有被浏览器充分识别，但还是不能忽略。

```html
<p>励志短语：<q cite="[URL]">你只管努力，剩下的交给时间。</q></p>
```

> <p>励志短语：<q cite="[URL]">你只管努力，剩下的交给时间。</q></p>



### 缩略语/缩写 `<abbr>`

- `title` 缩略语的相关描述
- 鼠标移动到缩略语上时，会显示 `title` 的值

```html
<p>推荐<abbr title="一边学习，一边摘录，方便后面复习。">张航的笔记</abbr></p>
```

> <p>推荐<abbr title="一边学习，一边摘录，方便后面复习。">张航的笔记</abbr></p>



### 标记联系方式 `<address>`

- 用于标记联系方式的元素

```html
<address>
	<p>张航 贵州</p>
    <ul>
        <li>电话：0123456789</li>
        <li>邮箱：lingyou.ly@outlook</li>
    </ul>
</address>
```

> <address>
> 	<p>张航 贵州</p>
>     <ul>
>         <li>电话：0123456789</li>
>         <li>邮箱：lingyou.ly@outlook</li>
>     </ul>
> </address>



### 上标和下标 `<sup>` `<sub>`

```
<p>如果 x<sup>2</sup> 的值为 9，那么 x 的值必为 3 或 -3。</p>
<p>咖啡因的化学方程式是C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>。</p>

```

> <p>如果 x<sup>2</sup> 的值为 9，那么 x 的值必为 3 或 -3。</p>
> <p>咖啡因的化学方程式是C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>。</p>



### 展示计算机代码 

- `<code>`：用于标记计算机的通用代码。

- `<pre>` ：保留内容的源代码格式。
- `<var>`：标记具体变量名。
- `<kbd>`：标记输入电脑的键盘（或其他类型）输入。
- `<samp>`：标记计算机程序的输出。

```
<pre><code># 该文件名为 test.py

def print_name_info(name, family_name_length=1):
    family_name = name[0: family_name_length]
    given_name = name[family_name_length: ]
    print(f'姓：{family_name}\n名：{given_name}')
    
name = '张航'
print_name_info(name)
</code></pre>

<p>在上述中，<var>name</var> 为变量名。</p>

<p>按 <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>A</kbd> 选择全部内容。</p>

<pre>$ <kbd>python test.py</kbd>
<samp>姓：张
名：航</samp></pre>
```

> ```python
> # 该文件名为 test.py
> 
> def print_name_info(name, family_name_length=1):
>     family_name = name[0: family_name_length]
>     given_name = name[family_name_length: ]
>     print(f'姓：{family_name}\n名：{given_name}')
>     
> name = '张航'
> print_name_info(name)
> 
> ```
>
> <p>在上述中，<var>name</var> 为变量名。</p>
>
> <p>按 <kbd>Ctrl</kbd>/<kbd>Cmd</kbd> + <kbd>A</kbd> 选择全部内容。</p>
>
> <pre>$ <kbd>python test.py</kbd>
> <samp>姓：张
> 名：航</samp></pre>



### 标记时间和日期

- 允许抓取事件的日期，并加入到日历中

```html
<time datetime="2023-02-06">2023 年 02 月 06 日</time>
```

> <time datetime="2023-02-06">2023 年 02 月 06 日</time>



## 文档与网站结构

- 正确使用标签，注意是布局使用还是要使用到语义。



### 文档基本部分


  | 文档基本部分 | 可用标签                                                     |
  | ------------ | ------------------------------------------------------------ |
  | 页眉         | `<header>`                                                   |
  | 导航栏       | `<nav>`                                                      |
  | 主内容       | `<main>` 著内容<br />`<article>` 独立结构<br />`<section>` 独立章节<br />`<div>` 通用布局 |
  | 侧边栏       | `<aside>`                                                    |
  | 页脚         | `<footer>`                                                   |



### 标签细节

- `<div>` 如果只是使用样式包装内容，多考虑 `<div>`
  - 但只有在没有其他语义标签可使用时才能够使用
  - 不能滥用
- `<nav>` 不该包含二级链接的内容。

- `<main>` 其父标签一般为`<body>`，嵌套在其他元素中是不合适的。

- `<article>` 独立的结构，比如包围的是一篇文章，而与其他部分无关。
  - 一般含有一个标题
  - 可包裹使用 `<adress>` 和 `<time>`
  - 但仍然可用在结构中嵌套结构，表示单独部分。比如嵌套一些信息，评论。
    - 这种嵌套下，再使用 `<address>` 表示信息，一般是不采取的
  - 包裹的内容是独立的，可使用
  - 无其它结构时，直接将内容放入 `<main>` 中
  - 如果只是单纯想作为样式包装，使用 `<div>`
- `<section>` 通用的独立章节，一个分节元素
  - 包含一个标题，没有标题没有意义
  - 一般只出现在文档大纲中
  - 表示主要内容的一部分
  - 在没有合适的其他语义元素使用时，才考虑该元素
  - 该元素包裹的内容是一个独立作品时，使用 `<article>`
  - 如果只是单纯想作为样式包装，使用 `<div>`
  - 如果全局导航已经使用了 `<nav>`，可以用 `<section>` 包裹二级导航





## HTML 调试

1. 在浏览器中打开 [Markup Validation Service](https://validator.w3.org/) 。
2. 选择 [Validate by Direct Input](https://validator.w3.org/#validate_by_input) 标签。
3. 将整个示例文档的代码（而不仅仅是`body`部分）复制粘贴到正中的文本框内。
4. *点击* **Check** *按钮。*



## 多媒体与嵌入

### 可附标题内容元素

- `<figure>` 代表独立的内容
- `<figcaption>` 描述或补充，简洁
- 可以是几张图片、一段代码、音视频、方程、表格或别的。

```html
<figure>
  <img src="favicon.ico" alt="这是网页图标。" />
  <figcaption>网页图标</figcaption>
</figure>
```



### 图像

- `src` 图片的地址
  - 图片名会被搜索引擎计入 SEO
  - 指向别的网站是违法的，称为“盗链”
- `title` 图片标题，鼠标移动到上面时，会显示
- `alt` 备选文本，其值被用于无法显示或不能被看到的情况
  - 图片如果只是装饰，不要写
  - 内容要简要，并且能够表达图片的信息
  - 本质是，图片无法被看见时，那是否可以被省略，需不需要用文字说明
- `width` 宽度
  - 如果是修改图片宽，不应该直接使用，而是对图片进行裁剪
- `height` 高度
  - 如果是修改图片高，不应该直接使用，而是对图片进行裁剪
- `size` 资源大小
  - `size=(max-width: 500px) 500px`
  - 表示视口宽不超过 500px，就使用 500px 的资源
  - 设置多个时，使用 `,` 隔开
- `srcset` 
  - `srcset="url 100w"`
  - `100w` 宽度描述符，也可以使用 `x` 语法。正整数除以 size 给出的大小计算得出有效的像素密度。
  - 设置多个时，使用 `,` 隔开
- 图片如果有意义，则使用该元素，否则，就使用 Css

```html
<img src="/favicon.ico" title="网页图标" alt="张航画的自画像">
```



### 视频

- `src` 视频源
- `controls` 视频控件
- `width` 与 `height`
- `autoplay` 立即播放
- `loop` 循环播放，不建议使用
- `muted` 默认关闭声音
- `poster` 指向图像 URL，播放前显示图片
- `preload` 缓冲较大的文件，其值为：
  - `none` 不缓冲
  - `auto` 页面加载后缓存文件
  - `metadata` 仅缓冲文件的元数据

```html
<video src="rabbit320.webm" controls>
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="rabbit320.mp4">此链接</a>观看</p>
</video>
```

**多源**

```html
<video controls>
  <source src="rabbit320.mp4" type="video/mp4">
  <source src="rabbit320.webm" type="video/webm">
  <p>你的浏览器不支持 HTML5 视频。可点击<a href="rabbit320.mp4">此链接</a>观看</p>
</video>
```



### 音频

- `src` 视频源
- `controls` 视频控件
- `autoplay` 立即播放
- `loop` 循环播放，不建议使用
- `muted` 默认关闭声音
- `preload` 缓冲较大的文件，其值为：
  - `none` 不缓冲
  - `auto` 页面加载后缓存文件
  - `metadata` 仅缓冲文件的元数据

```html
<audio controls>
  <source src="viper.mp3" type="audio/mp3">
  <source src="viper.ogg" type="audio/ogg">
  <p>你的浏览器不支持 HTML5 音频，可点击<a href="viper.mp3">此链接</a>收听。</p>
</audio>
```



### 视频和音频的字幕

[用法说明](https://developer.mozilla.org/zh-CN/docs/Web/HTML/Element/track)



### 其他嵌入技术

开始前再强调

- 版权问题
- 安全问题

**iframe**

- `width` 与 `height`
- `allowfullscreen` 全屏模式
- `frameborder` 绘制边框
  - 如果去除边框，推荐使用 Css 的 `border: noen;`
- `sandbox` 提高安全性

```html
<iframe src="[URL]"
        width="100%"
        height="500"
        frameborder="1"
        allowfullscreen
        sandbox>
  <p>您的浏览器不支持 iframe </p>
</iframe>
```



### 矢量图

```html
<img src="file.svg" alt="" />
```



## HTML 表格

```html
<table>
    <caption>表格标题</caption>
    <colgroup>
        <col>
    	<col style="background-color: skyblue;" span=1>
        <col>
        <col>
    </colgroup>
    <thead>
        <tr>
            <th></th>
    		<th scope="col">列标题a</th>
        	<th scope="col">列标题b</th>
        	<th scope="col">列标题c</th>
    	</tr>
    </thead>
    <tfoot>
        <tr>
        	<td colspan=4>页脚</td>
        </tr>
    </tfoot>
    <tbody>
        <tr>
            <th scope="row">行标题1</th>
    		<td rowspan=2>单元格a1</td>
        	<td colspan=2>单元格b1</td>
    	</tr>
        <tr>
            <th scope="row">行标题2</th>
            <td>单元格b2</td>
            <td>单元格c3</td>
        </tr>
    </tbody>
</table>
```

