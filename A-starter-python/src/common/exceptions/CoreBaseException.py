from src.core_one.exceptions.CoreErrorCodes import CoreErrorCodes
import json

class CoreBaseException(Exception):
    """Exception raised for errors in the input salary.

      Attributes:
          salary -- input salary which caused the error
          message -- explanation of the error
      """

    def __init__(self, code: CoreErrorCodes, message: str, module: str, inner=None, language="Python"):
        super().__init__(message)
        self.code = code.value
        self.message = message
        self.module = module
        self.inner = inner
        self.language = language


    def __str__(self):
        return json.dumps(self.__dict__)
        # if self.inner is None:
        #
        #     # return "{\"code\":{},\"message\":{},\"module\":{},\"language\":{}}".format(self.code, self.message,
        #     #                                                                            self.module, self.language)
        # else:
        #     return "{\"code\":{},\"message\":{},\"module\":{},\"language\":{},\"inner\":{}}".format(self.code,
        #                                                                                             self.message,
        #                                                                                             self.module,
        #                                                                                             self.language,
        #                                                                                             self.inner.__str__())
