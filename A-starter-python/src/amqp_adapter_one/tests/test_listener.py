import json
import unittest

from src.amqp_adapter_one.adapter.listener import process_request
from src.common.exceptions.CoreBaseException import CoreBaseException
from src.core_one.exceptions.CoreErrorCodes import CoreErrorCodes


class TestListener(unittest.TestCase):
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

    def test_process_request(self):
        limit = 2
        correlation_id = 'A'
        reply_to = 'queue_1'
        body = json.dumps({'length': limit})
        mock_dataLogic = type('AnonymousClass', (), {'getAllUsers': lambda _limit: self.__collection[:_limit]})
        message = MessageStub(correlation_id, reply_to, body, 'channel_1')
        amqp_message = AMQP_MessageStub()
        process_request(message, mock_dataLogic, amqp_message)
        self.assertEqual(message.was_ack_called, True)
        self.assertEqual(amqp_message.replied_to, reply_to)
        self.assertEqual(amqp_message.published_message, json.dumps(self.__collection[:limit]))
    def test_process_exception(self):
        exception_msg = 'Oops!'
        limit = 2
        correlation_id = 'A'
        reply_to = 'queue_1'
        body = json.dumps({'length': limit})
        mock_dataLogic = type('AnonymousClass', (),
                              {'getAllUsers':
                                   lambda _limit: raise_exception(CoreBaseException(CoreErrorCodes.incompatibleInputConditions, exception_msg,'AMQP'))})
        message = MessageStub(correlation_id, reply_to, body, 'channel_1')
        amqp_message = AMQP_MessageStub()
        process_request(message, mock_dataLogic, amqp_message)
        self.assertEqual(message.was_ack_called, True)
        self.assertEqual(amqp_message.replied_to, reply_to)
        self.assertEqual(json.loads(amqp_message.published_message)['err']['message'], exception_msg)

def raise_exception(e):
    raise e

class MessageStub:
    was_ack_called = False
    correlation_id = None
    reply_to = None
    body = None
    channel = None

    def __init__(self, correlation_id: str, reply_to: str, body: dict, channel):
        self.correlation_id = correlation_id
        self.body = body
        self.channel = channel
        self.reply_to = reply_to

    def ack(self):
        self.was_ack_called = True


class AMQP_MessageStub:
    published_message = None
    replied_to = None
    def create(self, channel, message, properties):
        self.published_message = message
        return type('AnonymousClass', (), {'publish': lambda _msg: self.set_replied_to(_msg)})

    def set_replied_to(self, msg):
        self.replied_to = msg
