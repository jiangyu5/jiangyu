## 归属

> [MDN](https://developer.mozilla.org/zh-CN)
>
> 归属于 [Mozilla 贡献者](https://developer.mozilla.org/zh-CN/docs/Learn/CSS)的[署名和版权许可协议](https://developer.mozilla.org/zh-CN/docs/MDN/Writing_guidelines/MDN/Writing_guidelines/Attrib_copyright_license)在[知识共享 署名 - 相同方式共享许可 2.5](https://creativecommons.org/licenses/by-sa/2.5/) 下提供。

上述的  [Mozilla 贡献者](https://developer.mozilla.org/zh-CN/docs/Learn/CSS) 地址为本笔记的学习内容。



## 盒模型



## 文本方向

- `horizontal-tb` 默认，水平，文字流从上到下
- `vertical-rl` 垂直，文字流从右到左
- `vertical-lr` 垂直，文字流从左到右

```css
writing-mode: vertical-rl;
```



## Css 值和单位

| 单位   | 相对于                                                       |
| :----- | :----------------------------------------------------------- |
| `em`   | 在 font-size 中使用是相对于父元素的字体大小，在其他属性中使用是相对于自身的字体大小，如 width |
| `ex`   | 字符“x”的高度                                                |
| `ch`   | 数字“0”的宽度                                                |
| `rem`  | 根元素的字体大小                                             |
| `lh`   | 元素的 line-height                                           |
| `vw`   | 视窗宽度的 1%                                                |
| `vh`   | 视窗高度的 1%                                                |
| `vmin` | 视窗较小尺寸的 1%                                            |
| `vmax` | 视图大尺寸的 1%                                              |