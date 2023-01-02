from typing import List

from dummy_repository import DummyRepository
from movie_ranking.domain.movie import Movie
from repository_interface import RepositoryInterface


class ActorRepository(RepositoryInterface, DummyRepository):
    def config(self, configuration_str: str):
        DummyRepository.config(self, configuration_str)

    def get(self, pk: int) -> Movie:
        pass

    def create(self, movie: Movie) -> Movie:
        pass

    def update(self, movie: Movie) -> Movie:
        pass

    def list(self, **kwargs) -> List[Movie]:
        pass

    def delete(self, pk: int):
        pass
