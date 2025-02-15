from src.core_one.logic.logic import DataLogic
def config_mutation(mutation):
    @mutation.field("createUser")
    async def resolve_createUsers(obj, info, input):
        return create_user(obj, info, input, DataLogic)


    return mutation

def create_user(obj, info, input, dataLogic):
    user_id = dataLogic.create(input)
    return {"id": user_id, "name": input["name"], "age": input["age"]}
