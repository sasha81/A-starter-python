from abc import ABC, abstractmethod


class IDAO(ABC):
    @abstractmethod
    def getAllUsers(limit):
        return

    @abstractmethod
    def create(item: dict):
        return
