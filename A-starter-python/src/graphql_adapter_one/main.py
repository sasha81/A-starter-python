import os

import uvicorn as uvicorn
from ariadne import QueryType, make_executable_schema, load_schema_from_path, graphql_sync, MutationType
from ariadne.asgi import GraphQL
from flask import Flask, request, jsonify
from py_eureka_client import eureka_client

from src.common.argparser import getParser
from src.common.config_getter import getConfig
from src.core_one.logic.logic import DataLogic
from src.graphql_adapter_one.adapter.error_handler import custom_format_error
from src.graphql_adapter_one.adapter.mutations import config_mutation
from src.graphql_adapter_one.adapter.queries import config_query

type_defs = load_schema_from_path("schema.graphql")

query = QueryType()
mutation = MutationType()

query = config_query(query)
mutation = config_mutation(mutation)
schema = make_executable_schema(type_defs, query, mutation)

THIS_MODULE_PATH = os.path.dirname(__file__)
DEFAULT_MODE = 'prod'

parser = getParser()
args = parser.parse_args()
config = getConfig(THIS_MODULE_PATH, args, DEFAULT_MODE, trim=False)
host = config["graphql.host"]
deployment_port = int(config["graphql.port"])
eureka_report_port = int(config["eureka.graphql_deployment_port"])
print("config[eureka.url]: ",config["eureka.url"])
print("config[eureka.graphql_deployment_port]: ",eureka_report_port )
try:
    eureka_client.init(eureka_server=config["eureka.url"], app_name=config["eureka.graphql_app_name"],
                       instance_host=config["eureka.rest_host"], instance_port=eureka_report_port)
except:
    print("Graphql adapter can't connect to Eureka: ")
DataLogic.init(args)
app = GraphQL(schema, debug=True,  error_formatter=custom_format_error)
if __name__ == "__main__":
    uvicorn.run(app, host=host, port=deployment_port)
# app = Flask(__name__)
# @app.route("/graphql", methods=["POST"])
# def graphql_server():
#    data = request.get_json()
#    success, result = graphql_sync(schema, data, context_value={"request": request})
#    status_code = 200 if success else 400
#    return jsonify(result), status_code
#
# # Run the app
# if __name__ == "__main__":
#    app.run(debug=True)