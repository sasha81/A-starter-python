from src.common.exceptions.CoreBaseException import CoreBaseException
from src.core_one.exceptions.CoreErrorCodes import CoreErrorCodes


class IncompatibleInputConditions(CoreBaseException):
    def __init__(self, cond_numbers: str):
        # message = "input conditions " + "".join(str(x) for x in cond_numbers) + " are incompatible"
        # code = CoreErrorCodes.incompatibleInputConditions
        super().__init__(code=CoreErrorCodes.incompatibleInputConditions, message="input conditions "+cond_numbers+" are incompatible", module='Core')
        # message = "input conditions "+"".join(cond_numbers)+" are incompatible"
        # code = CoreErrorCodes.incompatibleInputConditions
        # print(code, message)

