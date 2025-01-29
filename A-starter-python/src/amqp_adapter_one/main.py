"""
A simple RPC Server.
"""
import os

import amqpstorm
from adapter import listener
from src.common.argparser import getParser
from src.common.config_getter import getConfig
from src.core_one.logic.logic import DataLogic

THIS_MODULE_PATH = os.path.dirname(__file__)
DEFAULT_MODE = 'prod'

parser = getParser()
args = parser.parse_args()
DataLogic.init(args)
config = getConfig(THIS_MODULE_PATH, args, DEFAULT_MODE)
#DataLogic.append('users',{"name": "Sasha1", "age":42})

if __name__ == '__main__':
    CONNECTION = amqpstorm.Connection(hostname=config['hostname'], username=config['username'], password=config['password'])
   # CONNECTION = amqpstorm.Connection('rabbitmq-host', 'sasha', 'sasha')
   # CONNECTION = amqpstorm.Connection(config['RabbitMQ']['CONNECTION'], config['RabbitMQ']['USERNAME'], config['RabbitMQ']['PASSWORD'])
    CHANNEL = CONNECTION.channel()
    print(" [x] Connection is up, chanel created")
   # CHANNEL.queue.declare(queue='python-queue')
    CHANNEL.queue.bind(exchange=config['exchange'],routing_key=config['routing_key'],queue=config['queue'])
    #CHANNEL.basic.qos(int(config['prefetch_count']))
    CHANNEL.basic.consume(listener.on_request, config['queue'])

    print(" [x] Awaiting AMQP RPC requests")
    CHANNEL.start_consuming()