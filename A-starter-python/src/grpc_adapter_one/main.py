import os
from concurrent import futures

import grpc
from py_eureka_client import eureka_client

# from myproject.grpc_adapter_one.adapter import ApiServer
import src.grpc_adapter_one.adapter as ApiServer
from src.common.argparser import getParser
from src.common.config_getter import getConfig, load_yml_config
from src.core_one.logic.logic import DataLogic
from src.grpc_adapter_one.adapter.ExceptionToStatusInterceptor import CustomExceptionToStatusInterceptor
from src.grpc_adapter_one.api_pb2_grpc import add_ApiServicer_to_server

THIS_MODULE_PATH = os.path.dirname(__file__)
DEFAULT_MODE = 'prod'

parser = getParser()
args = parser.parse_args()
config = getConfig(THIS_MODULE_PATH, args, DEFAULT_MODE, trim=False)
DataLogic.init(args)

deployment_port = int(config["grpc.port"])
max_workers = int(config["grpc.max_workers"])
eureka_report_port = int(config["eureka.grpc_deployment_port"])

try:
    eureka_client.init(eureka_server=config["eureka.url"], app_name=config["eureka.grpc_app_name"],
                       instance_host=config["eureka.grpc_host"], instance_port=eureka_report_port)
except Exception as e:
    print("gRPC adapter can't connect to Eureka: ", e)

interceptors = [CustomExceptionToStatusInterceptor()]
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers), interceptors=interceptors)
    apiServ = ApiServer.getApiServer()
    add_ApiServicer_to_server( apiServ, server)
    server.add_insecure_port(f'[::]:{deployment_port}')
    server.start()
    print(" [x] gRPC is up at port"+f'[::]:{deployment_port}')
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
