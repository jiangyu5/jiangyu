from pathlib import Path, WindowsPath
import os
import json
import time


class DirData():
    '''
        实例对象属性

        json 包含的 dir 的信息如下：

        {
            'dir': '',
            'dir_path': '',
            'files': [],
            'files_path': [],
            'files_count': 0,
            'files_deep'?: []
        }

        实例方法 write_json() 将数据保存至 newPart 替换 dir 部分后的新路径
    '''

    def __init__(self, dir: str | WindowsPath, options={}) -> None:
        self.dir = self._path_type_currection(dir)
        self.options = self._init_options(
            self._options(), options)
        self.data = self._get_dir_data_json()

    @staticmethod
    def _options() -> dict:
        '''json 文件处理的默认配置'''
        return {'fix_url_path':
                {'old_part': '', 'new_part': ''},
                'ignore_files': [],
                'save_root_path': {
                    'new_root': '',
                    'old_root': ''
                },
                'json_name':  ''}

    def _init_options(self, init_options, options) -> dict:
        '''初始化配置'''
        for key, value in options.items():
            init_options[key] = value
        init_options['ignore_files'] = [
            self.dir / i for i in options['ignore_files']]
        return init_options

    @staticmethod
    def _path_type_currection(path: str | WindowsPath, res_win_type=True) -> WindowsPath | str:
        '''路径 str 和 WindowsPath 类型相互转换

        参数 res_win_type 默认 True

        True：str | WindowsPath --> WindowsPath；

        False：WindowsPath | str --> str'''
        if res_win_type:
            return path if isinstance(path, WindowsPath) else Path(path)
        else:
            return os.fspath(path) if isinstance(path, WindowsPath) else path

    def _fix_path(self, path: str | WindowsPath, old_part: str, new_part: str) -> str:
        t_path = self._path_type_currection(path, False)
        return t_path.replace('\\', '/').replace(old_part, new_part)

    def _fix_url_path(self, path: str | WindowsPath) -> str:
        '''json 中的 url 修正为网页能够访问的路径'''
        return self._fix_path(path, self.options['fix_url_path']['old_part'], self.options['fix_url_path']['new_part'])

    def _fix_save_root_path(self, path: str | WindowsPath) -> str:
        '''替换存储 json 的根目录'''
        return self._fix_path(path, self.options['save_root_path']['old_root'], self.options['save_root_path']['new_root'])

    @staticmethod
    def str_time(times):
        '''时间戳转为时间'''
        return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime(times))

    def _get_file_info(self, path: WindowsPath):
        '''获得文件夹下的文件（夹）信息'''
        stat = path.stat()
        atime = self.str_time(stat.st_atime)  # 最近访问时间
        mtime = self.str_time(stat.st_mtime)  # 最近修改时间
        ctime = self.str_time(stat.st_ctime)  # 创建时间
        return {
            'name': path.name,
            'type': 'dir' if path.is_dir() else 'file',
            'atime': atime,
            'mtime': mtime,
            'ctime': ctime
        }

    def _get_dir_data_json(self) -> json:
        '''获得 json 数据，即文件夹的信息'''
        data = {
            'dir': self.dir.name,
            'dir_path': self._fix_url_path(self.dir),
            'files': [],
            'files_path': [],
            'files_count': 0,
        }

        for i in self.dir.iterdir():
            if i in self.options['ignore_files']:
                continue
            data['files'].append(self._get_file_info(i))
            data['files_path'].append(self._fix_url_path(i))
            data['files_count'] += 1
        return data

    def handle_deep(self,  deep: int | bool = 2, deep_save: bool = False) -> json:
        '''获得 json 文件夹数据的深度，当 deep 为 True 时，为尽可能获取。返回值为完整的json数据。
        注意保存后的层级是依次递减的。

        ！！若要每个的层级获取深度相同，需要修改此函数，有需求再修改！！'''
        if deep is not True:
            deep -= 1

        if (deep > 0):
            self.data['files'].clear()
            for i in self.dir.iterdir():
                if i in self.options['ignore_files']:
                    continue
                _file_info = self._get_file_info(i)
                if i.is_dir():
                    _file_info = dict(
                        DirData(i, self.options).data, **_file_info)
                self.data['files'].append(_file_info)
        if deep_save:
            self.create_json()
        return self.data

    def create_json(self, save_path='') -> str:
        '''保存 json，自定义路径时需要指定文件名，返回保存的路径。'''
        if save_path == '':
            save_path = self._fix_save_root_path(
                self.dir / self.options['json_name'])
        save_path = self._path_type_currection(save_path)
        save_path.parent.mkdir(parents=True, exist_ok=True)
        save_path.write_text(json.dumps(
            self.data, ensure_ascii=False), encoding='utf-8')
        return self._path_type_currection(save_path, False)
