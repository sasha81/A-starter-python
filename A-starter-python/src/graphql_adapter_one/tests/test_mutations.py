import unittest

from src.graphql_adapter_one.adapter.mutations import create_user


class TestMutation(unittest.TestCase):

    def test_mutation(self):
        __id = "ABC"
        __input = {'name': 'A', 'age': 19}
        mock_dataLogic = type('AnonymousClass', (),
                              {'create': lambda _input: __id})
        result = create_user({}, {}, __input, mock_dataLogic)
        self.assertEqual(result['id'], __id)
        self.assertEqual(result['name'], __input["name"])
        self.assertEqual(result['age'], __input["age"])
