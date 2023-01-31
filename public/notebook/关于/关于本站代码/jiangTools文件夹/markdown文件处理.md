## 文档路径

工具代码路径：`/jiangTools/get_json_and_md_of_notebooks.py`

要处理文件的目录：`/public/notebook`



## 获得的文件

### `index.md`

存储路径：所在文件夹下

要求：文件夹下，且没有 `index.md` 文件，则创建 `index.md`。

```text
notebook/
	|- Python
		|- 基础语法.md
		|- 爬虫.md
		|- index.md  <--
	|- Vue
		|- router/
			|- index.md  <--
		|- index.md  <--
	|- index.md  <--
```

`index.md` 内容

```markdown
> 该文档还未被编写
```



### `index.json`

存储路径：`/public/data/notebook`

```text
/public/
	|- data
		|- notebook
			|- Python
				|- index.json
			|- Vue
				|- index.json
			|- index.json
```



`index.json` 基本数据

```json
{
	'dir': '',
    'dir_path': [],
    'files': [],
    'files_path': [],
    'files_count': 0,
}
```

- `dir` 与 `files` 元素，为文件夹和文件名；
- `dir_path` 与 `files_path` 为项目打包后可访问的路径。



## 代码

```python
from pathlib import Path, WindowsPath
import os
import json

class GetDirJsonData():
    '''
        实例对象属性

        json 包含传入的dir的信息如下：

        {
            'dir': '',
            'dir_path': '',
            'files': [],
            'files_path': [],
            'files_count': 0,
        }

        实例方法 write_json() 将数据保存至 newPart 替换 dir 部分后的新路径
    '''
    def __init__(self, dir: str | WindowsPath, fixUrlPath={'oldPart': '', 'newPart': ''}, ignoreFiles: list[str] = [], write_json_name: str = 'index.json'):
        self.dir = Path(dir) if isinstance(dir, str) else dir
        self.fixUrlPath = fixUrlPath
        self.ignoreFiles = [self.dir / i for i in ignoreFiles]
        self.write_json_path = Path(self._fixUrlPath(self.dir) + '/' + write_json_name)
        self.json = self._getDirJson()

    def _fixUrlPath(self, path: str | WindowsPath) -> str:
        t_path = str if isinstance(path, str) else os.fspath(path)
        return t_path.replace('\\', '/').replace(self.fixUrlPath['oldPart'], self.fixUrlPath['newPart'])

    def _getDirJson(self) -> json:
        data = {
            'dir': self.dir.name,
            'dir_path': self._fixUrlPath(self.dir),
            'files': [],
            'files_path': [],
            'files_count': 0,
        }
        for i in self.dir.iterdir():
            if i in self.ignoreFiles:
                continue
            data['files'].append(i.stem)
            data['files_path'].append(self._fixUrlPath(i))
            data['files_count'] += 1
        return json.dumps(data, ensure_ascii=False)

    def write_json(self):
        self.write_json_path.parent.mkdir(parents=True, exist_ok=True)
        self.write_json_path.write_text(self.json, encoding='utf-8')
        print(f'文件夹【{self.dir }】的数据\n\t已存至：【{self.write_json_path}】')


def main():
    fixUrlPath = {
        'oldPart': 'public/notebook',
        'newPart': 'public/data/notebook'
    }
    ignoreFiles = ['assets']
    write_json_name = 'index.json'
    dir = Path('public/notebook')

    def deep_write_json(dir):
        temp = GetDirJsonData(dir, fixUrlPath, ignoreFiles, write_json_name)
        temp.write_json()
        ignores = [dir / i for i in ignoreFiles]
        for p in dir.iterdir():
            if p.is_dir() and p not in ignores:
                deep_write_json(p)

    deep_write_json(dir)

    
if __name__ == '__main__':
    main()

```

> 关于写成类而不直接简单写到 main 里或一个函数，是为了方便以后扩展。
>
> json 的信息，如考虑加入文件类型等，方便编写页面的判断。