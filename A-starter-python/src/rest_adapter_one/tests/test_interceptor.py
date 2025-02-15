import unittest
from werkzeug.exceptions import HTTPException, BadRequest, InternalServerError
from src.common.exceptions.CoreBaseException import CoreBaseException
from src.core_one.exceptions.CoreErrorCodes import CoreErrorCodes
from src.rest_adapter_one.adapter.exception_interceptor import handle_exception


class TestInterceptor(unittest.TestCase):

    def test_core_interceptor(self):
        exception_msg = 'Ooops!'
        exception = CoreBaseException(CoreErrorCodes.incompatibleInputConditions, exception_msg, 'Rest')
        result: Exception = handle_exception(exception)
        self.assertEqual(isinstance(result, HTTPException), True)
        self.assertEqual(exception_msg in getattr(result, 'message', str(result)), True)
