import os
from typing import List, Dict, Any

from src.io_one.dao.DAO import DAO



class DataLogic:
    def init_with_DAO(args: Dict[str, Any], DAO = DAO):
        pass
    def init(args: Dict[str, Any], DAO = DAO):
        DAO.init(args)

    @staticmethod
    def append(collection: str, item: Dict[str, Any]):
        DAO.append(collection, item)

    @staticmethod
    def getAll(collection: str):
        return DAO.getAll(collection)

    @staticmethod
    def getAllUsers(limit: int):
        # raise IncompatibleInputConditions("[1,7]")
        users = DAO.getAllUsers(limit)
        return users

    @staticmethod
    def create(item: dict) -> str:
        userId = DAO.create(item)
        return userId
