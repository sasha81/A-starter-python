import unittest

from src.io_one.dao.DAO import DAO
from src.io_one.tests.MongoManagerStub import CollectionStub, MongoManagerStub


class TestDAO(unittest.TestCase):
    __id = "1"
    __collection = [{
        "_id": 1,
        "age": 42,
        "name": "Sasha"
    },
        {"_id": 2,
         "age": 41,
         "name": "Masha"
         }]

    def setUp(self):
        collectionStub = CollectionStub(self.__collection, self.__id)
        mongoManagerStub = MongoManagerStub({'collection_name': 'users', 'collection': collectionStub})
        DAO.init({'collection_name': 'users', 'collection': collectionStub}, mongoManagerStub)

    def test_get_all(self):
        length = 10
        result = DAO.getAll('users').limit(length)
        self.assertEqual(len(result), len(self.__collection))

    def test_get_all_users(self):
        limit = 1
        result = DAO.getAllUsers(limit)
        self.assertEqual(len(result), limit)

    def test_create_user(self):
        user = {"name": "A", "age": 19}
        result = DAO.create(user)
        self.assertEqual(result, self.__id)
