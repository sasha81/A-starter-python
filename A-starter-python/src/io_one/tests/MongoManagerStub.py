from src.io_one.IMongoManager import IMongoManager

from typing import List, Dict, Any


class MongoManagerStub(IMongoManager):
    __db = None;

    def __init__(self, config: Dict[str, Any]):
        self.__db = {}
        self.__db[config['collection_name']] = config['collection']

    def init(self, args) -> None:
        pass

    def get_db(self):
        return self.__db

    def getInstance(self):
        pass


class CollectionStub:
    __collection = None
    __id = None
    def __init__(self, collection, id):
        self.__collection = collection
        self.__id = id

    def find(self, args):
        return type('AnonymousClass', (), {'limit': lambda num: self.__collection[:num]})

    def insert_one(self, args: Dict[str, Any]):
        self.__collection.append(args)
        return type('AnonymousClass', (), {'inserted_id': self.__id})
