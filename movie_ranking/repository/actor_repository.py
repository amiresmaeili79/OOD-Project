from typing import List

from movie_ranking.domain.actor import Actor
from .dummy_repository import DummyRepository
from .repository_interface import RepositoryInterface


class ActorRepository(RepositoryInterface, DummyRepository):
    def get_by_name(self, *args, **kwargs):
        pass

    def config(self, configuration_str: str):
        DummyRepository.config(self, configuration_str)

    def get_max_pk(self) -> int:
        if len(self.objects.values()) == 0:
            return 0
        return max(self.objects.keys())

    def get(self, pk: int) -> Actor:
        return self.objects[pk]

    def create(self, actor: Actor) -> Actor:

        if actor.pk in self.objects:
            raise KeyError("Object is already added")

        self.objects[actor.pk] = actor
        return self.objects[actor.pk]

    def update(self, actor: Actor) -> Actor:
        self.objects[actor.pk] = actor
        return actor

    def list(self, **kwargs) -> List[Actor]:
        return list(self.objects.values())

    def delete(self, pk: int):
        del self.objects[pk]

    def fill_mock(self):
        for i in range(10):
            actor = Actor(i, f"Actor_{i}", i + 30)
            self.objects[actor.pk] = actor

    def __str__(self):
        return "actor"
