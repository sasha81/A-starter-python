import unittest
from unittest.mock import patch
from src.core_one.logic.logic import DataLogic
from src.grpc_adapter_one.adapter import ApiServer
from src.grpc_adapter_one.adapter.ApiServer import get_all, get_stream


class TestGRPCApi(unittest.TestCase):
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
    __type_collection = [
        type('AnonymousClass', (), {"id": "A1", "name": "Sasha", "age": 40}),
        type('AnonymousClass', (), {"id": "A2", "name": "Masha", "age": 41}),
        type('AnonymousClass', (), {"id": "A3", "name": "Oxana", "age": 42}),
    ]

    def test_getAll(self):
        dataLogic = type('AnonymousClass', (), {'getAllUsers': lambda limit: self.__collection[:limit]})
        request = type('AnonymousClass', (), {'length': 2})
        context = type('AnonymousClass', (), {'set_code': 3, 'set_details': "A"})
        result = get_all(request, context, dataLogic)
        self.assertEqual(len(result.users), request.length)

    def test_getStream(self):
        __id = "ABC"
        mock_dataLogic = type('AnonymousClass', (),
                              {'create': lambda _input: __id})

        result = get_stream(iter(self.__type_collection), {}, mock_dataLogic)
        res_1 = next(result)
        self.assertEqual(res_1.id, __id)
        self.assertEqual(res_1.name, self.__type_collection[0].name)
        self.assertEqual(res_1.age, self.__type_collection[0].age)
