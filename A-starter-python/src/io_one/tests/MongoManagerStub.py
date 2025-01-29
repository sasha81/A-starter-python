from src.io_one.IMongoManager import IMongoManager

from typing import List, Dict, Any

class MongoManagerStub(IMongoManager):
    __db=None;
    def __init__(self, config: Dict[str, Any]):
        self.__db = {}
        self.__db[config['collection_name']] = config['collection']


    def init(self,args) -> None:
        pass


    def get_db(self):
        return self.__db


    def getInstance(self):
        pass


class CollectionStub:
    __collection=None

    def __init__(self,collection):
        self.__collection = collection
    def find(self, args):
        return self.__collection

    def insert_one(self, args: Dict[str, Any]):
        self.__collection.append(args)
        return True