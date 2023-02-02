## 暂时这样


```python
from pathlib import Path
import shutil
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

    save_path = (relative_path + '/data/') / \
        path.relative_to(relative_path) / save_json_name
    save_path.parent.mkdir(parents=True, exist_ok=True)
    save_path.write_text(json.dumps(
        data, ensure_ascii=False), encoding='utf-8')

    return data


shutil.rmtree('public/data/notebook')
get_info(notebook)

```
