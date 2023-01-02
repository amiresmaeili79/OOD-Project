from typing import List

from movie_ranking.domain.actor import Actor
from .dummy_repository import DummyRepository
from .repository_interface import RepositoryInterface


class ActorRepository(RepositoryInterface, DummyRepository):
    def config(self, configuration_str: str):
        DummyRepository.config(self, configuration_str)

    def get(self, pk: int) -> Actor:
        return self.objects[0]

    def create(self, actor: Actor) -> Actor:
        return self.objects[0]

    def update(self, actor: Actor) -> Actor:
        return self.objects[0]

    def list(self, **kwargs) -> List[Actor]:
        return self.objects

    def delete(self, pk: int):
        return True

    def fill_mock(self):
        for i in range(10):
            self.objects.append(
                Actor(i, f"Actor_{i}", i + 30)
            )

    def __str__(self):
        return "actor"
