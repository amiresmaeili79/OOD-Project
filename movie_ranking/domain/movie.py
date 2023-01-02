from typing import List

from .actor import Actor
from .award import Award


class Movie:

    def __init__(self, pk: int, rating: int, name: str, genre: str, duration: int, year: int, description: str,
                 awards: List[Award], actors: List[Actor]):
        self.pk = pk
        self.rating = rating
        self.name = name
        self.genre = genre
        self.duration = duration
        self.year = year
        self.description = description
        self.awards = awards
        self.stars = actors

    def rate(self, rating_num: int):
        # code
        return True

    def get_rating(self):
        # code
        return True

    def add_awards(self, award: Award):
        # code
        return True

    def add_actors(self, actor: Actor):
        # code
        return True

    def get_actors(self):
        # code
        return True

    def get_name(self):
        # code
        return True

    def set_name(self, name: str):
        # code
        return True

    def get_genre(self):
        # code
        return True

    def set_genre(self, genre: str):
        # code
        return True

    def get_duration(self):
        # code
        return True

    def set_duration(self, duration: int):
        # code
        return True

    def get_year(self):
        # code
        return True

    def set_year(self, year: int):
        # code
        return True

    def get_description(self):
        # code
        return True

    def set_description(self, description: str):
        # code
        return True

    def add_comment(self, comment: str):
        # code
        return True

    def get_comments(self):
        # code
        return True
