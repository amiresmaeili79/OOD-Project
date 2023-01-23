from typing import List

import uuid

from movie_ranking.domain.movie import Movie
from movie_ranking.domain.actor import Actor
from movie_ranking.domain.award import Award
from movie_ranking.repository.repository_interface import RepositoryInterface
from .api_interface import ApiInterface
from .search_interface import SearchInterface

import argparse


class CliApi(ApiInterface):

    def __init__(self, repository: RepositoryInterface, actor_repository : RepositoryInterface , search: SearchInterface) -> None:
        self.repository = repository
        self.search_approach = search
        self.actor_repository = actor_repository

        while True :
            print("Choose one of options:")
            print("1 - Search movie")
            print("2 - Create movie")
            print("3 - Update movie")
            print("4 - Get rankings")
            print("5 - Exit")

            option = input("option: ")

            if option == "5":
                break

            match int(option):
                case 1:
                    m = self.search()
                case 2:
                    m = self.create_movie()
                case 3:
                    m = self.update_movie()
                case 4:
                    ranking = self.get_ranking()

    def search(self) -> List[Movie]:
        print("searching")
        name = input("Enter the name:")
        return self.search_approach.search(self.repository.list(), name)

    def create_movie(self) -> Movie:

        name = input("insert movie name:")
        rating = int(input("insert movie rating:"))
        genre = input("insert movie genre:")
        duration = int(input("insert movie duration:"))
        year = int(input("insert movie year:"))
        description = input("insert movie description:")
        actors = []

        have_actors = input("Actors ? \n (options : yes no):")
        if have_actors == "yes":
            while True:
                name = input("Name :")
                age = int(input("Age :"))
                pk = self.actor_repository.get_max_pk() + 1

                actor = Actor(pk, name, age)

                self.actor_repository.create(actor)
                actors.append(actor)

                cont = input("Continue ? \n (options : yes no) :")
                if cont == "no" :
                    break

        awards = []

        have_awards = input("Awards ? \n (options : yes no) :")
        if have_awards == "yes":
            while True:
                pk = int(uuid.uuid4())
                name = input("Name :")
                year = int(input("Year :"))

                award = Award(pk, name, year)

                awards.append(award)

                cont = input("Continue ? \n (options : yes no) :")
                if cont == "no":
                    break

        comments = []
        pk = self.repository.get_max_pk() + 1

        movie = Movie(pk, rating, 0, name, genre, duration, year, description, awards, actors, comments)

        return self.repository.create(movie)

    def update_movie(self) -> Movie:
        pk = int(input("insert movie pk:"))
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

    def add_comment(self) -> None:
        movie_name = input("Enter movie name:")
        movie = Movie()
        for m in self.repository.list():
            if m.name == movie_name :
                movie = m
                break

        comment = input("Your comment :")
        movie.comments.append(comment)


    def add_rating(self) -> None:
        pass
