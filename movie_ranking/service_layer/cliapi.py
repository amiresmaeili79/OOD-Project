from typing import List

from movie_ranking.domain.movie import Movie
from movie_ranking.repository.repository_interface import RepositoryInterface
from .api_interface import ApiInterface
from .search_interface import SearchInterface


class CliApi(ApiInterface):

    def __init__(self, repository: RepositoryInterface, search: SearchInterface) -> None:
        self.repository = repository
        self.search = search

    def search(self, name, type) -> List[Movie]:
        pass

    def create_movie(self) -> Movie:
        pass

    def update_movie(self) -> Movie:
        pass

    def get_ranking(self) -> List[Movie]:
        return self.repository.list()

    def update_ranking(self) -> None:
        pass
