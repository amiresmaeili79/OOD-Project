from abc import ABC, abstractmethod
from movie_ranking.domain.movie import  Movie


class SearchInterface(ABC):

    @abstractmethod
    def search(self, name) -> [Movie]:
        pass
