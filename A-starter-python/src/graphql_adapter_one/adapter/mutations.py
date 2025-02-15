from src.core_one.logic.logic import DataLogic
def config_mutation(mutation):
    @mutation.field("createUser")
    async def resolve_createUsers(obj, info, input):
        return {"id": "ABC", "name": input["name"], "age": input["age"]}

    return mutation
