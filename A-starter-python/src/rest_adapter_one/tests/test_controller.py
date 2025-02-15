import unittest

from src.rest_adapter_one.adapter.rest_controller import process_get_all_users


class TestRest(unittest.TestCase):
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

    def test_get_all(self):
        __limit = 2
        mock_request = type('AnonymousClass', (),
                            {'args': type('AnonymousClass', (),
                                          {'get': lambda _input: __limit})})
        mock_dataLogic = type('AnonymousClass', (), {'getAllUsers': lambda _limit: self.__collection[:_limit]})

        result = process_get_all_users(mock_request, mock_dataLogic)
        self.assertEqual(result, self.__collection[:__limit])
