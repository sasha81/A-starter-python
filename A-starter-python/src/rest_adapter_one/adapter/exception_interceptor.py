import logging
import traceback as tb

from werkzeug.exceptions import HTTPException, BadRequest, InternalServerError

from src.common.exceptions.CoreBaseException import CoreBaseException
from src.core_one.exceptions.CoreErrorCodes import CoreErrorCodes



#@app.errorhandler(Exception)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    logging.error(''.join(tb.format_exception(None, e, e.__traceback__)))
    if isinstance(e, HTTPException):
        return e
    elif isinstance(e, CoreBaseException):
        if e.code == CoreErrorCodes.incompatibleInputConditions.value:
            http_exception=BadRequest(e.message)
            return http_exception

    else:
        return InternalServerError(e.message)
