from typing import List

from movie_ranking.domain.actor import Actor
from movie_ranking.domain.award import Award
from movie_ranking.domain.movie import Movie
from .dummy_repository import DummyRepository
from .repository_interface import RepositoryInterface


class MovieRepository(RepositoryInterface, DummyRepository):
    def config(self, configuration_str: str):
        DummyRepository.config(self, configuration_str)

    def get_max_pk(self) -> int:
        if len(self.objects.values()) == 0:
            return 0
        return max(self.objects.keys())

    def get_by_name(self, name: str) -> List[Movie]:
        result = []
        for m in self.objects.values():
            if m.name == name:
                result.append(m)

        return result

    def get(self, pk: int) -> Movie:
        return self.objects[pk]

    def create(self, movie: Movie) -> Movie:
        if movie.pk in self.objects:
            raise KeyError("Object is already added")

        self.objects[movie.pk] = movie
        return self.objects[movie.pk]

    def update(self, movie: Movie) -> Movie:
        self.objects[movie.pk] = movie
        return movie

    def list(self, **kwargs) -> List[Movie]:
        return list(self.objects.values())

    def delete(self, pk: int):
        del self.objects[pk]

    def fill_mock(self):
        for i in range(10):
            movie = Movie(i, i, f"Movie_{i}", f"Genre_{i}", 120 + 10 * i, 1995 + i, f"Description_{i}", [
                Award(i, f"Award_{i}", 1995 + i), Award(i, f"Award_{i + 1}", 1998 + i)
            ], [Actor(i, f"Actor_{i}", 30 + i), Actor(i, f"Actor_{i + 1}", 40 + i)])
            self.objects[movie.pk] = movie

    def __str__(self):
        return "movie"
