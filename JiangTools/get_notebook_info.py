
from pathlib import Path
import time
import json
import os

relative_path = 'public'
notebook = Path('public/notebook')
ignore_files = ['assets', 'index.md', 'index.json', '关于']
save_json_name = 'index.json'


def str_time(times):
    '''时间戳转为时间'''
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(times))


def get_md(data):
    md = ''
    files = data['files']
    for n in files:
        if n['type'] == 'dir':
            md += f'[{n["name"]}](#{n["path"].replace(" ", "%20")})\n\n'
            md += f'&emsp;&emsp;&emsp;&emsp;推荐阅读：\n\n'
            for i in n['files']:
                md += f'&emsp;&emsp;&emsp;&emsp;{i["mtime"][2:-3]}&ensp;[{i["name"]}](#{i["path"].replace(" ", "%20")})\n\n'
        else:
            md += f'{n["mtime"][2:-3]}&ensp;[{n["name"]}](#{n["path"].replace(" ", "%20")})\n\n'

    return md


def get_info(path):
    stat = path.stat()
    data = {
        'name': path.stem,
        'path': '/' + os.fspath(path.relative_to(relative_path)).replace('\\', '/'),
        'type': 'dir' if path.is_dir() else 'file',
        'atime': str_time(stat.st_atime),
        'mtime': str_time(stat.st_mtime),
        'ctime': str_time(stat.st_ctime),
        'files': [],
        'count': 0
    }

    if path.is_file():
        del data['files']
        return data

    _ignore_files = [path / i for i in ignore_files]
    for p in path.iterdir():
        if p in _ignore_files:
            continue
        data['count'] += 1
        data['files'].append(get_info(p))

    # 文件排序，data['files']，暂时仅对 notebook 逆序
    if path == notebook:
        data['files'].sort(key=lambda x: x['name'], reverse=True)

    # 保存 json 类型数据
    save_path = (relative_path + '/data/') / \
        path.relative_to(relative_path) / save_json_name
    save_path.parent.mkdir(parents=True, exist_ok=True)
    save_path.write_text(json.dumps(
        data, ensure_ascii=False), encoding='utf-8')

    # index.md 默认生成
    index_md = path / 'index.md'
    index_md.touch()
    index_md.write_text(get_md(data), encoding='utf-8')

    return data


# shutil.rmtree('public/data/notebook')
get_info(notebook)
