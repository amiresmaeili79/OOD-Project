from movie_ranking.domain.movie import  Movie
from movie_ranking.repository.repository_interface import RepositoryInterface
from isearch import SearchInterface

class CliApi(ApiInterface):

    def __init__(self, repository: RepositoryInterface, search: SearchInterface ) -> None:
        this.repository = repository
        this.search = search

    def search(self, name, type) -> [Movie]:
        pass

    def create_movie(self) -> Movie:
        pass

    def update_movie(self) -> Movie:
        pass

    def get_ranking(self) -> [Movie]:
        pass

    def udpate_ranking(self) -> None:
        pass