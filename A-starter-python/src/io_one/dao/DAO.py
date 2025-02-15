import os
from typing import List, Dict, Any
from src.common.config_getter import getConfig
from src.io_one.dao.IDAO import IDAO
from src.io_one.database import MongoManager
from src.io_one.fileio import FileIO


class DAO(IDAO):
    __mongoManager = None
    __fileio = None
    __db = None
    __config = None

    def init(args: Dict[str, Any], mongo_manager=MongoManager):
        mongo_manager.init(args)
        DAO.__mongoManager = mongo_manager.getInstance()
        DAO.__db = mongo_manager.get_db()
        DAO.__fileio = FileIO.init(args)

        THIS_MODULE_PATH = '/'.join(os.path.dirname(__file__).split('/')[:-1])
        DEFAULT_MODE = 'prod'
        DAO.__config = getConfig(THIS_MODULE_PATH, args, DEFAULT_MODE, trim=False)

    @staticmethod
    def getAllUsers(limit):
        if limit is None:
            limit = DAO.__config['queries.max']
        # raise IncompatibleInputConditions("[1,7]")
        users = DAO.__db["users"].find({}).limit(limit)
        users = list(users)
        return list(map(DAO.cut_user_dict, users))

    @staticmethod
    def create(item: dict) -> str:
        user = DAO.__db["users"].insert_one(item)
        return str(user.inserted_id)

    @staticmethod
    def append(collection: str, item: Dict[str, Any]):
        DAO.__db[collection].insert_one(item)

    @staticmethod
    def getAll(collection: str):
        return DAO.__db[collection].find({})

    @staticmethod
    def cut_user_dict(user):
        if ("name" in user) and ("age" in user):
            dct = {"id": str(user["_id"]), "name": user["name"], "age": user["age"]}
        return dct
