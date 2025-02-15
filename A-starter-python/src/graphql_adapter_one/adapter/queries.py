from src.core_one.logic.logic import DataLogic
def config_query(query):
    @query.field("getAllUsers")
    def resolve_getAllUsers(_, info, limit):
        result = DataLogic.getAllUsers(limit)
        return result


    return query
