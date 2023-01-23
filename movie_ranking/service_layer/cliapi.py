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

        match int(option):
            case 1:
                m = self.search()
            case 2:
                m = self.create_movie()
            case 3:
                m = self.update_movie()
            case 4:
                ranking = self.get_ranking()
            case 5:
                self.update_ranking()

    def search(self) -> List[Movie]:
        print("searching")
        name = input("Enter the name:")
        genre = input("Enter the type:")
        self.search_approach.search(name)

    def create_movie(self) -> Movie:
        pk = int(input("insert movie pk:")) # What is pk
        name = input("insert movie name:")
        rating = int(input("insert movie rating:"))
        genre = input("insert movie genre:")
        duration = int(input("insert movie duration:"))
        year = int(input("insert movie year:"))
        description = input("insert movie description:")
        awards = []
        actors = []
        comments = []

        movie = Movie(pk, rating, name, genre, duration, year, description, awards, actors, comments)

        return self.repository.create(movie)

    def update_movie(self) -> Movie:
        pk = int(input("insert movie pk:"))  # What is pk
        name = input("insert movie name:")
        rating = int(input("insert movie rating:"))
        genre = input("insert movie genre:")
        duration = int(input("insert movie duration:"))
        year = int(input("insert movie year:"))
        description = input("insert movie description:")
        awards = []
        actors = []
        comments = []

        movie = Movie(pk, rating, name, genre, duration, year, description, awards, actors, comments)

        return self.repository.update(movie)

    def get_ranking(self) -> List[Movie]:
        return self.repository.list().sort(lambda x: x.rating)

    def update_ranking(self) -> None:
        print("Update rankings")
        pass
