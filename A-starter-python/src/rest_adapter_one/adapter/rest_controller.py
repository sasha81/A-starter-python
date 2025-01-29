
from src.core_one.logic import logic

def setController(app):
    @app.route("/optimizer/getAll")
    def hello_world():
        result =  logic.DataLogic.getAllUsers()
        return result