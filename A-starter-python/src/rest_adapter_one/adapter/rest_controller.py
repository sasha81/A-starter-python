from flask import request, jsonify, make_response
from src.core_one.logic.logic import DataLogic

def setController(app):
    @app.route("/users/getAll")
    def get_all_users():
        return process_get_all_users(request, DataLogic)


def process_get_all_users(request, dataLogic):
    limit = int(request.args.get('limit'))
    result = dataLogic.getAllUsers(limit)
    return result
