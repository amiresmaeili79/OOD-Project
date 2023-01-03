from search_interface import SearchInterface
from movie_ranking.domain.movie import Movie


class NameSearch(SearchInterface):
    def search(self, name) -> list[Movie]:
        pass
