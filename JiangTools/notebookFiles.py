# !!! vscode 下运行时，./ 为 vue 项目
# public 下的 notebook 文件夹
# 如果 该目录 为文件夹，则 创建 index.json
# json 包含该目录下的所有文件

from pathlib import Path
from pathlib import WindowsPath
import json
import os
from turtle import Turtle


def statistics(path: WindowsPath, ignoreFiles: list[WindowsPath] = []) -> dict:
    data = {
        'name': path.name,
        'count': 0,
        'files': [],
    }

    for i in path.iterdir():
        if i in ignoreFiles:
            continue
        data['count'] += 1
        data['files'].append(
            {'name': i.stem,
             'path': os.fspath(i).replace('\\', '/').replace('public/', '/')
             })
    return data


def createIndexJson(path: WindowsPath, indexFileName: str = 'index.json'):
    index_json_path = Path(path / indexFileName)
    index_json_path.touch(exist_ok=True)

    res_statistics = statistics(
        path, ignoreFiles=[index_json_path, index_json_path.parent / indexMarkdown])
    res_statistics['children'] = []

    for p in path.iterdir():
        if p.is_dir():
            (p / 'index.md').touch(exist_ok=True)
            tempRes = createIndexJson(p)
            res_statistics['children'].append(tempRes)

    index_json_path.write_text(json.dumps(
        res_statistics, ensure_ascii=False), encoding='utf-8')

    return res_statistics


if __name__ == "__main__":
    # notebook 的目录
    indexFileName = 'index.json'
    notebook_path = 'public/notebook'
    indexMarkdown = 'index.md'

    # 每个文件夹下忽略的文件
    ignore_files = [Path()]
    createIndexJson(Path(notebook_path))
