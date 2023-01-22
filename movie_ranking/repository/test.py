from unittest import TestCase

from .dummy_repository import DummyRepository
from .repository_interface import RepositoryInterface
from .repository_registry import RepositoryRegistry


class TestRepositoryRegistry(TestCase):

    def setUp(self) -> None:
        pass

    def test_add_registry(self):
        class MyRepo(RepositoryInterface, DummyRepository):
            def config(self, configuration_str: str):
                DummyRepository.config(self, configuration_str)

            def get(self, **kwargs):
                pass

            def create(self, **kwargs):
                pass

            def update(self, **kwargs):
                pass

            def list(self, **kwargs):
                pass

            def delete(self, **kwargs):
                pass

            def __str__(self):
                return "myrepo"

        foo_repo = MyRepo()
        foo_registry = RepositoryRegistry()
        foo_registry.add_repository(foo_repo, "")

        self.assertTrue(hasattr(foo_registry, "myrepo"))
