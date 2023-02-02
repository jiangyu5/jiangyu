import DirData
from pathlib import Path

options = {
    'fix_url_path': {
        'old_part': 'public/notebook',
        'new_part': 'notebook'
    },
    'ignore_files': ['assets', 'index.json', 'index.md'],
    'save_root_path': {
        'new_root': 'public/data/notebook',
        'old_root': 'public/notebook'
    },
    'json_name': 'index.json'
}

dir = Path('public/notebook')

notebook = DirData(dir, options)
notebook.handle_deep(deep=2)
notebook.create_json()

for i in dir.iterdir():
    if i.is_dir():
        DirData(i, options=options).handle_deep(True, deep_save=True)
