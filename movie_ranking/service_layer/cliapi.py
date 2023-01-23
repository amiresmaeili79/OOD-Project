from typing import List

from movie_ranking.domain.movie import Movie
from movie_ranking.repository.repository_interface import RepositoryInterface
from .api_interface import ApiInterface
from .search_interface import SearchInterface

import argparse


class CliApi(ApiInterface):

    def __init__(self, repository: RepositoryInterface, search: SearchInterface) -> None:
        self.repository = repository
        self.search_approach = search

        print("Choose one of options:")
        print("1 - Search movie")
        print("2 - Create movie")
        print("3 - Update movie")
        print("4 - Get rankings")
        print("5 - Update rankings")

        option = input("option: ")

        if int(option) == 1:
            name = input("Enter the name:")
            type = input("Enter the type:")
            m = self.search(name, type)

        if int(option) == 2:
            m = self.create_movie()

        if int(option) == 3:
            m = self.update_movie()

        if int(option) == 4:
            ranking = self.get_ranking()

        if int(option) == 5:
            self.update_ranking()

    def search(self, name, type) -> List[Movie]:
        print("searching")
        pass

    def create_movie(self) -> Movie:
        print("insert movie name:")
        return self.repository.create(Movie(0, 0, "", "", 0, 0, "", [], []))

    def update_movie(self) -> Movie:
        print("insert movie new name")
        return self.repository.update(Movie(0, 0, "", "", 0, 0, "", [], []))

    def get_ranking(self) -> List[Movie]:
        print("rankings :")
        return self.repository.list()

    def update_ranking(self) -> None:
        print("Update rankings")
        pass
