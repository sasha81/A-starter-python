import unittest
from unittest.mock import MagicMock
from src.core_one.logic.logic import DataLogic
from src.io_one.tests.MongoManagerStub import CollectionStub, MongoManagerStub


class TestLogic(unittest.TestCase):


    __collection = [{
        "age": 42,
        "name": "Sasha"
    },
        {
            "age": 41,
            "name": "Masha"
        }]
    def setUp(self):
        collectionStub = CollectionStub(self.__collection)
        mongoManagerStub = MongoManagerStub({'collection_name':'users','collection': collectionStub})
        DataLogic.init({'collection_name':'users','collection': collectionStub},mongoManagerStub)


    def test_get_all(self):
        result = DataLogic.getAll('users')
        self.assertEqual(len(result),len(self.__collection))

