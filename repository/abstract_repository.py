from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    """
    Abstract repository which hanldes connection to the
    persistent layer
    """

    @abstractmethod
    def config(configuration_str: str):
        raise NotImplementedError("implement me!")