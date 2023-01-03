from movie_ranking.domain.movie import  Movie
from movie_ranking.repository.repository_interface import RepositoryInterface
from search_interface import SearchInterface
from api_interface import ApiInterface
from html_template_api import HtmlTemplateApi
from rest_api import RestApi

class CliApi(ApiInterface, HtmlTemplateApi, RestApi):

    def __init__(self, repository: RepositoryInterface, search: SearchInterface ) -> None:
        self.repository = repository
        self.search = search

    def search(self, name, type) -> list[Movie]:
        pass

    def create_movie(self) -> Movie:
        pass

    def update_movie(self) -> Movie:
        pass

    def get_ranking(self) -> list[Movie]:
        pass

    def udpate_ranking(self) -> None:
        pass