from typing import List

from .actor import Actor
from .award import Award
from .comment import Comment


class Movie:

    def __init__(self, pk: int, rating: int, rate_cnts: int, name: str, genre: str, duration: int, year: int,
                 description: str,
                 awards: List[Award], actors: List[Actor], comments: List[Comment]):
        self.pk = pk
        self.rating = rating
        self.name = name
        self.genre = genre
        self.duration = duration
        self.year = year
        self.description = description
        self.awards = awards
        self.stars = actors
        self.rate_cnts = rate_cnts
        self.comments = comments

    def rate(self, rating_num: int):
        current_rate = self.rate * self.rate_cnts
        self.rate_cnts += 1
        self.rate = current_rate / self.rate_cnts

    def get_rating(self):
        return self.rate

    def add_awards(self, award: Award):
        self.awards.append(award)

    def add_actors(self, actor: Actor):
        self.stars.append(actor)

    def get_actors(self):
        return self.stars

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_genre(self):
        return self.genre

    def set_genre(self, genre: str):
        self.genre = genre

    def get_duration(self):
        return self.duration

    def set_duration(self, duration: int):
        self.duration = duration

    def get_year(self):
        return self.year

    def set_year(self, year: int):
        self.year = year

    def get_description(self):
        return self.description

    def set_description(self, description: str):
        self.description = description

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def get_comments(self):
        return self.comments
