import os

from flask import Flask
from py_eureka_client import eureka_client

from src.common.argparser import getParser
from src.common.config_getter import getConfig
from src.core_one.logic.logic import DataLogic
from src.rest_adapter_one.adapter.exception_interceptor import handle_exception
from src.rest_adapter_one.adapter.rest_controller import setController

app = Flask(__name__)

setController(app)
#
# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

THIS_MODULE_PATH = os.path.dirname(__file__)
DEFAULT_MODE = 'prod'

parser = getParser()
args = parser.parse_args()
config = getConfig(THIS_MODULE_PATH, args, DEFAULT_MODE, trim=False)
host = config["rest.host"]
deployment_port = int(config["rest.port"])
eureka_report_port = int(config["eureka.rest_deployment_port"])
print("config[eureka.url]: ",config["eureka.url"])
print("config[eureka.rest_deployment_port]: ",eureka_report_port )
try:
    eureka_client.init(eureka_server=config["eureka.url"], app_name=config["eureka.rest_app_name"],instance_host=host, instance_port=eureka_report_port)
except:
    print("Rest adapter can't connect to Eureka: ")
DataLogic.init(args)

#DataLogic.append('users',{"name": "Sasha", "age":42})
if __name__ == '__main__':
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.register_error_handler(Exception, handle_exception)
    app.run(host=host, port=deployment_port)