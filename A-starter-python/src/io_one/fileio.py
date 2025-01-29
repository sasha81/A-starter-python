import os

from src.common.config_getter import getConfig


class FileIO:
    __ABSOLUTE_PATH = None
    __READ_RELATIVE_PATH = None
    __WRITE_RELATIVE_PATH = None
    __mode = None
    __DEFAULT_MODE = None

    @staticmethod
    def init(args, default_mode: str = 'prod'):
        if hasattr(args, "mode"):
            FileIO.__mode = args.mode
        else:
            FileIO.__mode = default_mode
        FileIO.__DEFAULT_MODE = default_mode
        FileIO.__ABSOLUTE_PATH = os.path.dirname(__file__)
        config = getConfig(FileIO.__ABSOLUTE_PATH, {'mode': FileIO.__mode}, FileIO.__DEFAULT_MODE, trim=False)
        FileIO.__READ_RELATIVE_PATH = config['files.import']
        FileIO.__WRITE_RELATIVE_PATH = config['files.export']
        return FileIO

    @staticmethod
    def read_file(file_name: str):
        path = FileIO.__ABSOLUTE_PATH + '/' + FileIO.__READ_RELATIVE_PATH + '/' + file_name
        try:
            with open(path) as f:
                contents = f.read()
                return contents
        except:
            print('file not found: ' + path)

    @staticmethod
    def write_file(file_name: str, content: str):
        path = FileIO.__ABSOLUTE_PATH + '/' + FileIO.__WRITE_RELATIVE_PATH + '/' + file_name
        try:
            with open(path) as f:
                f.write(content)
        except:
            print('Cant open: ' + path)
