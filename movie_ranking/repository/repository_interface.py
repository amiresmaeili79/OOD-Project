from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    """
    Interface for repositories
    """

    @abstractmethod
    def config(self, configuration_str: str):
        raise NotImplementedError("implement me!")

    @abstractmethod
    def get(self, *args, **kwargs):
        raise NotImplementedError("Implement Me")

    @abstractmethod
    def create(self, *args, **kwargs):
        raise NotImplementedError("Implement Me")

    @abstractmethod
    def update(self, *args, **kwargs):
        raise NotImplementedError("Implement Me")

    @abstractmethod
    def list(self, *args, **kwargs):
        raise NotImplementedError("Implement Me")

    @abstractmethod
    def delete(self, *args, **kwargs):
        raise NotImplementedError("Implement Me")
