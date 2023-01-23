from abc import ABC, abstractmethod
from typing import List

from movie_ranking.domain.movie import Movie


class ApiInterface(ABC):

    @abstractmethod
    def search(self) -> List[Movie]:
        raise NotImplementedError("implement me!")

    @abstractmethod
    def create_movie(self) -> Movie:
        raise NotImplementedError("implement me!")

    @abstractmethod
    def update_movie(self) -> Movie:
        raise NotImplementedError("implement me!")

    @abstractmethod
    def get_ranking(self) -> List[Movie]:
        raise NotImplementedError("implement me!")

    @abstractmethod
    def update_ranking(self) -> None:
        raise NotImplementedError("implement me!")
