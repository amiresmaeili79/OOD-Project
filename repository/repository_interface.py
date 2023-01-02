from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    """
    Interface for respositories
    """

    @abstractmethod
    def config(configuration_str: str):
        raise NotImplementedError("implement me!")

    @abstractmethod
    def get(**kwargs):
        raise NotImplementedError("Implement Me")

    @abstractmethod
    def create(**kwargs):
        raise NotImplementedError("Implement Me")

    @abstractmethod
    def update(**kwargs):
        raise NotImplementedError("Implement Me")

    @abstractmethod
    def list(**kwargs):
        raise NotImplementedError("Implement Me")

    @abstractmethod
    def delete(**kwargs):
        raise NotImplementedError("Implement Me")
