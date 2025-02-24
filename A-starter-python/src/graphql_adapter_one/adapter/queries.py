from src.core_one.logic.logic import DataLogic


def config_query(query):
    @query.field("getAllUsers")
    def resolve_getAllUsers(_, info, limit):
        return get_all_users(_, info, limit, DataLogic)

    return query


def get_all_users(_, info, limit, dataLogic):
    result = dataLogic.getAllUsers(limit)
    return result
