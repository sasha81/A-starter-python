from abc import ABC, abstractmethod


class IMongoManager(ABC):

    @abstractmethod
    def init(args, DEFAULT_MODE: str) -> None:
        return

    @abstractmethod
    def get_db(self):
        return

    @abstractmethod
    def getInstance(self):
        return