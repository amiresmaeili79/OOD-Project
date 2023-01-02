from typing import List

from movie_ranking.domain.actor import Actor
from movie_ranking.domain.award import Award
from movie_ranking.domain.movie import Movie
from .dummy_repository import DummyRepository
from .repository_interface import RepositoryInterface


class MovieRepository(RepositoryInterface, DummyRepository):
    def config(self, configuration_str: str):
        DummyRepository.config(self, configuration_str)

    def get(self, pk: int) -> Movie:
        return self.objects[0]

    def create(self, movie: Movie) -> Movie:
        return self.objects[0]

    def update(self, movie: Movie) -> Movie:
        return self.objects[0]

    def list(self, **kwargs) -> List[Movie]:
        return self.objects

    def delete(self, pk: int):
        return True

    def fill_mock(self):
        for i in range(10):
            movie = Movie(i, i, f"Movie_{i}", f"Genre_{i}", 120 + 10 * i, 1995 + i, f"Description_{i}", [
                Award(i, f"Award_{i}", 1995 + i), Award(i, f"Award_{i + 1}", 1998 + i)
            ], [Actor(i, f"Actor_{i}", 30 + i), Actor(i, f"Actor_{i + 1}", 40 + i)])
            self.objects.append(movie)

    def __str__(self):
        return "movie"
