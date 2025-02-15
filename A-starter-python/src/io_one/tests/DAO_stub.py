from typing import Dict, Any

from src.io_one.dao.DAO import DAO
from src.io_one.tests.MongoManagerStub import MongoManagerStub


class DAO_stub(DAO):
    def init(args: Dict[str, Any], mongo_manager=MongoManagerStub):
        DAO.init(args, mongo_manager)