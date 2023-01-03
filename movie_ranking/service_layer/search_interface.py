from abc import ABC, abstractmethod
from typing import List

from movie_ranking.domain.movie import Movie


class SearchInterface(ABC):

    @abstractmethod
    def search(self, name) -> List[Movie]:
        pass
