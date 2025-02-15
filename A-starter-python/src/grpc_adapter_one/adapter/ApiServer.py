from src.core_one.logic.logic import DataLogic
from src.grpc_adapter_one import api_pb2 as apis
from src.grpc_adapter_one.api_pb2_grpc import ApiServicer


class ApiServer(ApiServicer):
    def getAll(self, request, context):
        responseObj = apis.Users()
        users = DataLogic.getAllUsers(int(request.length))
        users = getItemsFromUsers(users)
        responseObj.users.extend( users)
        return responseObj

    def getStream(self, request_iterator, context):
        for req in request_iterator:
            result = DataLogic.create({"name": req.name, "age": req.age})
            yield apis.User(id=result, name=req.name, age=req.age)

    def sayHello(self, request, context):
        return apis.Hello(message=f'Hello {request.name}!')


def getItemsFromUsers(users):
    user_list = []
    for user in users:
        user_list.append(apis.User(id=str(user['id']), name=user['name'], age=user['age']))
    return user_list
