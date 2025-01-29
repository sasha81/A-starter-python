import logging

from amqpstorm import Message, AMQPInvalidArgument, AMQPError
import traceback as tb
from src.common.exceptions.CoreBaseException import CoreBaseException

from src.core_one.logic import logic
import json
def on_request(message):
    properties = {
        'correlation_id': message.correlation_id
    }

    try:
        print(" [.] message.body(%s)" % (message.body,))

        response = logic.DataLogic().getAllUsers()
        #response = str({'name':'Python'})



        response = Message.create(message.channel, json.dumps(response), properties)
        response.publish(message.reply_to)

        message.ack()
    except CoreBaseException as e:
        logging.error(''.join(tb.format_exception(None, e, e.__traceback__)))
        #print(e.__str__())
        # if e.code == CoreErrorCodes.incompatibleInputConditions.value:
        #     #raise AMQPError(reply_code=406)
        #
        #
        # else:
        #     #raise AMQPError(reply_code=541)


        response = Message.create(message.channel,"{err:"+ e.__str__()+"}", properties)
        response.publish(message.reply_to)

        message.ack()