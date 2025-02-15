from flask import request, jsonify, make_response
from src.core_one.logic import logic

def setController(app):
    @app.route("/users/getAll")
    def get_all_users():
        limit = int(request.args.get('limit'))
        result = logic.DataLogic.getAllUsers(limit)
        return result