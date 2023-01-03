from abc import ABC, abstractmethod
from movie_ranking.domain.movie import  Movie


class ApiInterface(ABC):

    @abstractmethod
    def search(self, name, type) -> [Movie]:
        raise NotImplementedError("implement me!")

    @abstractmethod
    def create_movie(self) -> Movie:
        raise NotImplementedError("implement me!")

    @abstractmethod
    def update_movie(self) -> Movie:
        raise NotImplementedError("implement me!")

    @abstractmethod
    def get_ranking(self) -> [Movie]:
        raise NotImplementedError("implement me!")

    @abstractmethod
    def udpate_ranking(self) -> None:
        raise NotImplementedError("implement me!")
