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

    def __init__(self, dir: str | WindowsPath, fixUrlPath={'oldPart': '', 'newPart': ''}, ignoreFiles: list[str] = [], write_root_path: str = '', write_json_name: str = 'index.json') -> None:
        self.dir = Path(dir) if isinstance(dir, str) else dir
        self.fixUrlPath = fixUrlPath
        self.ignoreFiles = [self.dir / i for i in ignoreFiles]
        self.write_json_path = Path(
            write_root_path + self._fixUrlPath(self.dir) + '/' + write_json_name)
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
        # return json.dumps(data, ensure_ascii=False, indent=4) # 测试的时候设置
        return json.dumps(data, ensure_ascii=False)

    def write_json(self):
        self.write_json_path.parent.mkdir(parents=True, exist_ok=True)
        self.write_json_path.write_text(self.json, encoding='utf-8')

        print(
            f'文件夹【{self.dir }】的数据\n\t已存至：【{self.write_json_path}】')


def main():
    fixUrlPath = {
        'oldPart': 'public/notebook',
        'newPart': 'notebook'
    }
    ignoreFiles = ['assets', 'index.json']
    write_root_path = 'public/data/'
    write_json_name = 'index.json'
    dir = Path('public/notebook')

    def deep_write_json(dir):
        temp = GetDirJsonData(dir, fixUrlPath, ignoreFiles,
                              write_root_path, write_json_name)
        temp.write_json()
        ignores = [dir / i for i in ignoreFiles]
        for p in dir.iterdir():
            if p.is_dir() and p not in ignores:
                deep_write_json(p)

    deep_write_json(dir)


if __name__ == '__main__':
    main()
