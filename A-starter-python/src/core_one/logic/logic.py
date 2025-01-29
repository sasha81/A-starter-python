from typing import List, Dict, Any

from src.core_one.exceptions.IncompatibleInputConditionsException import IncompatibleInputConditions
from src.io_one.database import MongoManager
from src.io_one.fileio import FileIO


class DataLogic:
    __mongoManager = None
    __fileio = None
    __db = None
    def init( args: Dict[str, Any],mongo_manager=MongoManager):
        mongo_manager.init(args)
        DataLogic.__mongoManager = mongo_manager.getInstance()
        DataLogic.__db = mongo_manager.get_db()
        DataLogic.__fileio = FileIO.init(args)


    @staticmethod
    def append(collection: str, item: Dict[str, Any]):
        DataLogic.__db[collection].insert_one(item)

    @staticmethod
    def getAll(collection: str):
        #message = "input conditions "+"".join(str(x) for x in [2,7])+" are incompatible"
        #raise IncompatibleInputConditions("[1,7]")
        return DataLogic.__db[collection].find({})

    @staticmethod
    def getAllUsers():
       # raise IncompatibleInputConditions("[1,7]")
        users = list(DataLogic.__db["users"].find())
        return list(map(cut_user_dict, users))

    @staticmethod
    def create(item):
        return DataLogic.__db["users"].insert_one(item)


def cut_user_dict(user):
    if ("name" in user) and ("age" in user):
        dct = {"name": user["name"], "age": user["age"]}
    return dct