from abc import ABC, abstractmethod


class AbstractRepository(ABC):
    """
    Abstract repository which handles connection to the
    persistent layer
    """

    @abstractmethod
    def config(self, configuration_str: str):
        raise NotImplementedError("implement me!")
