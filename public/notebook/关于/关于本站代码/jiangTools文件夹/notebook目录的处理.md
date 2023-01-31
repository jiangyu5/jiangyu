## 文档路径

工具代码路径：`/jiangTools/get_index_and_md_of_notebooks.py`

要处理文件的目录：`/public/notebook`



## 工具目的

### 文件创建

`notebook/` 下目录如下：

```text
notebook/
	|- Python
		|- 基础语法.md
		|- 爬虫.md
		|- index.md  <--
		|- index.json  <--
	|- Vue
		|- router/
			|- index.md  <--
			|- index.json  <--
		|- index.md  <--
		|- index.json  <--
	|- index.md  <--
	|- index.json  <--
```

- 文件夹下，则创建 `index.js` 文件；
- 文件夹下，且没有 `index.md` 文件，则创建 `index.md`。
- `notebook/[dirName]/` 也遵循上述规则。



### 创建文件的内容

`index.json`

```json
{
	'dir': '',
    'dir_path': [],
    'files': [],
    'files_count': 0,
    'files_path': []
}
```

- `dir` 与 `files` 元素，为文件夹和文件名；
- `dir_path` 与 `files_path` 为项目打包后可访问的路径。



`index.md`

```markdown
> 该文档还未被编写
```

