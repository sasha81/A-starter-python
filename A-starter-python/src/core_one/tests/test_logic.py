import unittest
from unittest.mock import MagicMock
from src.core_one.logic.logic import DataLogic
from src.io_one.tests.DAO_stub import DAO_stub
from src.io_one.tests.MongoManagerStub import CollectionStub, MongoManagerStub


class TestLogic(unittest.TestCase):
    __id = '1'

    __collection = [{
        "_id": 1,
        "age": 42,
        "name": "Sasha"
    },
        {"_id": 2,
         "age": 41,
         "name": "Masha"
         },
        {"_id": 3,
         "age": 40,
         "name": "Oxana"
         }
    ]

    def setUp(self):
        collectionStub = CollectionStub(self.__collection, self.__id)
        mongoManagerStub = MongoManagerStub({'collection_name': 'users', 'collection': collectionStub})
        DAO_stub.init({'collection_name': 'users', 'collection': collectionStub}, mongoManagerStub)
        DataLogic.init_with_DAO({'collection_name': 'users', 'collection': collectionStub}, DAO_stub)

    def test_get_all(self):
        lim = 2
        result = DataLogic.getAllUsers(lim)
        self.assertEqual(len(result), lim)
        self.assertEqual(result[0]['name'], self.__collection[0]['name'])
        self.assertEqual(result[0]['id'], str(self.__collection[0]['_id']))

    def test_create_user(self):
        user = {"name": "A", "age": 15}
        result = DataLogic.create(user)
        self.assertEqual(result, self.__id)
