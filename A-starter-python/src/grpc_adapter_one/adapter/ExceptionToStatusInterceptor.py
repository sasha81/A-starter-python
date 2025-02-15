from typing import Any, Callable
import traceback as tb
import grpc
from grpc_interceptor import ServerInterceptor
from grpc_interceptor.exceptions import GrpcException, Unknown, FailedPrecondition

from src.common.exceptions.CoreBaseException import CoreBaseException
from src.core_one.exceptions.CoreErrorCodes import CoreErrorCodes
import logging

class CustomExceptionToStatusInterceptor(ServerInterceptor):

    def intercept(
            self,
            method: Callable,
            request: Any,
            context: grpc.ServicerContext,
            method_name: str,
    ) -> Any:
        try:
            result = method(request, context)
            context.send_initial_metadata(context.invocation_metadata())
            return result
        except CoreBaseException as e:
            logging.error(''.join(tb.format_exception(None, e, e.__traceback__)))
            metadata = context.invocation_metadata()
            logging.error('with correlationID ', metadata)

            if e.code == CoreErrorCodes.incompatibleInputConditions.value:
                context.set_code(FailedPrecondition.status_code)
            else:
                context.set_code(Unknown.status_code)

            context.set_details(e.__str__())

