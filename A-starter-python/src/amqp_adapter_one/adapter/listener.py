import logging

from amqpstorm import Message, AMQPInvalidArgument, AMQPError
import traceback as tb
from src.common.exceptions.CoreBaseException import CoreBaseException
from src.core_one.exceptions.CoreErrorCodes import CoreErrorCodes
from src.core_one.logic.logic import DataLogic
import json
def on_request(message):
    process_request(message, DataLogic, Message)

def process_request(message, dataLogic, amqp_message):
    properties = {
        'correlation_id': message.correlation_id
    }

    try:
        print(" [.] message.body(%s)" % (message.body,))
        limit = json.loads(message.body)['length']
        response = dataLogic.getAllUsers(limit)
        response = amqp_message.create(message.channel, json.dumps(response), properties)
        response.publish(message.reply_to)
        message.ack()
    except CoreBaseException as e:
        logging.error(''.join(tb.format_exception(None, e, e.__traceback__)))
        response = amqp_message.create(message.channel, "{\"err\":" + e.__str__() + "}", properties)
        response.publish(message.reply_to)

        message.ack()
