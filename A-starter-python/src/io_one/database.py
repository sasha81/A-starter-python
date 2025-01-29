import os

import pymongo

from src.common.config_getter import getConfig
from typing import List, Dict, Any

from src.io_one.IMongoManager import IMongoManager


class MongoManager(IMongoManager):
    __instance = None
    __args = None
    __DEFAULT_MODE = None
    __db = None


    @staticmethod
    def init(args, DEFAULT_MODE: str = 'prod'):
        if hasattr(args, "mode"):
            MongoManager.__args = args
            MongoManager.__DEFAULT_MODE = DEFAULT_MODE
        else:
            MongoManager.__args = DEFAULT_MODE
            MongoManager.__DEFAULT_MODE = DEFAULT_MODE

    @staticmethod
    def getInstance():
        if MongoManager.__instance == None:
            THIS_MODULE_PATH = os.path.dirname(__file__)
            config = getConfig(THIS_MODULE_PATH, MongoManager.__args, MongoManager.__DEFAULT_MODE, trim=False)
            MongoManager(config)
            result = MongoManager.__instance
        return result

    # @staticmethod
    # def init_db(db: str):
    #     MongoManager.__db = MongoManager.__instance[db]
    #     return MongoManager.__db

    @staticmethod
    def get_db():
        return MongoManager.__db
    def __init__(self, config: Dict[str, Any]):
        if MongoManager.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            host = config['mongodb.host']+':'+str(config['mongodb.port'])
            username = config['mongodb.username']
            password = config['mongodb.password']
            db_name=config['mongodb.db_name']
            MongoManager.__instance = pymongo.MongoClient(host=host, username = username, password = password)
            MongoManager.__db = MongoManager.__instance[db_name]