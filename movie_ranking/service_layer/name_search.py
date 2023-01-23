from typing import List

from movie_ranking.domain.movie import Movie
from .search_interface import SearchInterface


class NameSearch(SearchInterface):
    def search(self, movies, name) -> List[Movie]:
        result = []
        for m in movies:
            if m.name == name:
                movie = m
                result.append(m)

        return result
