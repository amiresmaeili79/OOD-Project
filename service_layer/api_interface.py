from abc import ABC, abstractmethod
from movie_ranking.domain.movie import  Movie


class ApiInterface(ABC):

    @abstractmethod
    def search(self, name, type) -> [Movie]:
        pass

    @abstractmethod
    def create_movie(self) -> Movie:
        pass

    @abstractmethod
    def update_movie(self) -> Movie:
        pass

    @abstractmethod
    def get_ranking(self) -> [Movie]:
        pass

    @abstractmethod
    def udpate_ranking(self) -> None:
        pass
