import unittest
from unittest.mock import patch
from ariadne import QueryType, make_executable_schema, load_schema_from_path, graphql_sync, MutationType
from src.core_one.logic.logic import DataLogic
from src.graphql_adapter_one.adapter.queries import config_query, get_all_users


class TestQueries(unittest.TestCase):
    __collection = [{
        "id": '1',
        "age": 42,
        "name": "Sasha"
    },
        {"id": '2',
         "age": 41,
         "name": "Masha"
         },
        {"id": '3',
         "age": 40,
         "name": "Oxana"
         }
    ]

    def test_query(self):
        limit = 5
        mock_dataLogic = type('AnonymousClass', (), {'getAllUsers': lambda limit: self.__collection[:limit]})
        result = get_all_users({}, {}, limit, mock_dataLogic)
        self.assertEqual(len(result), len(self.__collection))
