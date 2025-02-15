import unittest

from graphql import GraphQLError

from src.graphql_adapter_one.adapter.error_handler import custom_format_error


class TestError(unittest.TestCase):

    def test_error(self):
        error = GraphQLError('message_1')
        result = custom_format_error(error)
        self.assertEqual(result["message"], "INTERNAL SERVER ERROR")
