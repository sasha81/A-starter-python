from src.core_one.logic.logic import DataLogic
from src.grpc_adapter_one import api_pb2 as apis
from src.grpc_adapter_one.api_pb2_grpc import ApiServicer


class ApiServer(ApiServicer):
    def getAll(self, request, context):

        responseObj = apis.Items()
        users = DataLogic.getAll("users")

        items = getItemsFromUsers(users)
        responseObj.items.extend(items)

        return responseObj

    def getStream(self, request, context):
        for i in range(1, request.length + 1):
            yield apis.Item(id=i, name=f'name {i}')

    def sayHello(self, request, context):
        return apis.Hello(message=f'Hello {request.name}!')

def getItemsFromUsers(users):
    user_list = []
    count = 0
    for user in users:
        user['_id'] = count
        user_list.append(apis.Item(id=user['_id'], name = user['name']))
        count = count + 1
    return user_list