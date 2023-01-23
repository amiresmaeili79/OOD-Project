from typing import List

from movie_ranking.domain.movie import Movie
from .search_interface import SearchInterface


class NameSearch(SearchInterface):
    def search(self, movies, name) -> List[Movie]:
        movies
        for m in self.repository.list():
            if m.name == movie_name:
                movie = m
                break
