from typing import List

from movie_ranking.domain.movie import Movie
from .search_interface import SearchInterface


class NameSearch(SearchInterface):
    def search(self, name) -> List[Movie]:
        pass
