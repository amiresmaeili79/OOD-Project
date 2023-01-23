from typing import List

import uuid

from movie_ranking.domain.movie import Movie
from movie_ranking.domain.actor import Actor
from movie_ranking.domain.award import Award
from movie_ranking.domain.comment import Comment
from movie_ranking.repository.repository_interface import RepositoryInterface
from .api_interface import ApiInterface
from .search_interface import SearchInterface

import argparse


class CliApi(ApiInterface):

    def __init__(self, repository: RepositoryInterface, actor_repository : RepositoryInterface , search: SearchInterface) -> None:
        self.repository = repository
        self.search_approach = search
        self.actor_repository = actor_repository

        while True:
            print("Choose one of options:")
            print("1 - Search movie")
            print("2 - Create movie")
            print("3 - Update movie")
            print("4 - Get rankings")
            print("5 - Add comment")
            print("6 - Add rating")
            print("7 - Exit")

            option = input("option: ")

            if option == "7":
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
                case 5:
                    self.add_comment()
                case 6:
                    self.add_rating()

    def search(self) -> List[Movie]:
        name = input("Enter the name:")
        movies = self.search_approach.search(self.repository.list(), name)
        print(len(movies))
        if len(movies) == 0:
            print("No movie found")
        else:
            movie = movies[0]

            print("==================================")
            print(movie.name)
            print(movie.genre, " - ", movie.year)
            print("Rate : ", movie.rating)
            print("Description", movie.description)
            print("Stars:")
            for s in movie.stars:
                print(s.name)
            print("\n")

            print("Awards:")
            for s in movie.awards:
                print(s.name, " in ", s.year)
            print("\n")

            print("Comments:")
            for s in movie.comments:
                print(s.datetime, " : ", s.body)
            print("\n")
            print("==================================")

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

        movie = Movie(pk, rating, 1, name, genre, duration, year, description, awards, actors, comments)

        return self.repository.create(movie)

    def update_movie(self) -> Movie:

        name = input("insert movie name:")
        movie = self.repository.get_by_name(name)[0]

        movie.name = input("insert movie name:")
        movie.rating = int(input("insert movie rating:"))
        movie.genre = input("insert movie genre:")
        movie.duration = int(input("insert movie duration:"))
        movie.year = int(input("insert movie year:"))
        movie.description = input("insert movie description:")

        actors = []

        have_actors = input("Update actors ? \n (options : yes no):")
        if have_actors == "yes":
            while True:
                name = input("Name :")
                age = int(input("Age :"))
                pk = self.actor_repository.get_max_pk() + 1

                actor = Actor(pk, name, age)

                self.actor_repository.create(actor)
                actors.append(actor)

                cont = input("Continue ? \n (options : yes no) :")
                if cont == "no":
                    break

        awards = []

        have_awards = input("Update awards ? \n (options : yes no) :")
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

        movie.awards = awards
        movie.stars = actors

        return self.repository.update(movie)

    def get_ranking(self) -> List[Movie]:
        print(len(self.repository.list()))
        print(self.repository.list()[0].name)
        ranking = sorted(self.repository.list(), key=lambda x: x.rating, reverse=True)
        i = 1
        print("==================================")
        print("Rankings :")
        for r in ranking:

            print(i, "-", r.name)
            i += 1

        print("==================================")

    def update_ranking(self) -> None:
        print("Update rankings")
        pass

    def add_comment(self) -> None:
        movie_name = input("Enter movie name:")
        try:
            movie = self.repository.get_by_name(movie_name)[0]
        except:
            print("Movie not found")
            return

        comment = input("Your comment :")
        movie.comments.append(Comment(comment))
        self.repository.update(movie)

    def add_rating(self) -> None:
        movie_name = input("Enter movie name:")
        try:
            movie = self.repository.get_by_name(movie_name)[0]
        except:
            print("Movie not found")
            return

        rating = input("Enter rating:")
        movie.rate(int(rating))
        self.repository.update(movie)
