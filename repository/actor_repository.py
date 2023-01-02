from dummy_repository import DummyRepository
from repository_interface import RepositoryInterface


class ActorRepository(RepositoryInterface, DummyRepository):
    def config(self, configuration_str: str):
        DummyRepository.config(self, configuration_str)

    def get(self, pk: int):
        pass

    def create(self, movie):
        pass

    def update(self, movie):
        pass

    def list(self, **kwargs):
        pass

    def delete(self, pk: int):
        pass