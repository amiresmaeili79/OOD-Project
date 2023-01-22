from copy import deepcopy
from unittest import TestCase

from .actor_repository import ActorRepository
from .dummy_repository import DummyRepository
from .movie_repository import MovieRepository
from .repository_interface import RepositoryInterface
from .repository_registry import RepositoryRegistry
from ..domain.actor import Actor
from ..domain.award import Award
from ..domain.movie import Movie


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


class TestMovieRepository(TestCase):

    def setUp(self) -> None:
        self.repo = MovieRepository()
        self.repo.config("foo")

        self.movies = []
        for i in range(10):
            movie = Movie(i, i, f"Movie_{i}", f"Genre_{i}", 120 + 10 * i, 1995 + i, f"Description_{i}", [
                Award(i, f"Award_{i}", 1995 + i), Award(i, f"Award_{i + 1}", 1998 + i)
            ], [Actor(i, f"Actor_{i}", 30 + i), Actor(i, f"Actor_{i + 1}", 40 + i)])
            self.movies.append(movie)

    def test_add_movie(self):
        self.repo.create(self.movies[0])
        self.repo.create(self.movies[1])

        self.assertEqual(self.repo.objects[self.movies[0].pk], self.movies[0])
        self.assertEqual(self.repo.objects[self.movies[1].pk], self.movies[1])

        self.repo.objects.clear()  # make sure no side effect exists

    def test_get_movie(self):
        self.repo.objects[0] = self.movies[0]

        self.assertEqual(self.repo.get(0), self.movies[0])

        self.repo.objects.clear()

    def test_list_movies(self):
        self.repo.objects = {m.pk: m for m in self.movies}

        self.assertEqual(len(self.repo.list()), len(self.movies))

        test_idx = len(self.movies)

        self.assertEqual(self.repo.list()[test_idx - 1], self.movies[test_idx - 1])
        self.repo.objects.clear()

    def test_update_movie(self):
        self.repo.objects = {m.pk: m for m in self.movies}

        movie_to_update: Movie = deepcopy(self.repo.objects[0])
        movie_to_update.year = movie_to_update.year + 10
        movie_to_update.rating = movie_to_update.rating + 0.3

        self.repo.update(movie_to_update)
        self.assertEqual(movie_to_update, self.repo.objects[movie_to_update.pk])

        self.repo.objects.clear()

    def test_delete_movie(self):
        self.repo.objects = {m.pk: m for m in self.movies}

        remove_idx = len(self.movies) // 2
        self.repo.delete(remove_idx)
        self.assertEqual(len(self.repo.objects), len(self.movies) - 1)
        with self.assertRaises(KeyError):
            self.repo.delete(remove_idx)


class TestActorRepository(TestCase):

    def setUp(self) -> None:
        self.actors = []
        for i in range(10):
            actor = Actor(i, f"Actor_{i}", i + 30)
            self.actors.append(actor)

        self.repo = ActorRepository()
        self.repo.config("foo")

    def test_add_actor(self):
        self.repo.create(self.actors[0])
        self.repo.create(self.actors[1])

        self.assertEqual(self.repo.objects[self.actors[0].pk], self.actors[0])
        self.assertEqual(self.repo.objects[self.actors[1].pk], self.actors[1])

        self.repo.objects.clear()  # make sure no side effect exists

    def test_get_actor(self):
        self.repo.objects[0] = self.actors[0]

        self.assertEqual(self.repo.get(0), self.actors[0])

        self.repo.objects.clear()

    def test_list_actors(self):
        self.repo.objects = {m.pk: m for m in self.actors}

        self.assertEqual(len(self.repo.list()), len(self.actors))

        test_idx = len(self.actors)

        self.assertEqual(self.repo.list()[test_idx - 1], self.actors[test_idx - 1])
        self.repo.objects.clear()

    def test_update_actor(self):
        self.repo.objects = {m.pk: m for m in self.actors}

        actor_to_update: Actor = deepcopy(self.repo.objects[0])
        actor_to_update.year = actor_to_update.age + 10

        self.repo.update(actor_to_update)
        self.assertEqual(actor_to_update, self.repo.objects[actor_to_update.pk])

        self.repo.objects.clear()

    def test_delete_actor(self):
        self.repo.objects = {m.pk: m for m in self.actors}

        remove_idx = len(self.actors) // 2
        self.repo.delete(remove_idx)
        self.assertEqual(len(self.repo.objects), len(self.actors) - 1)
        with self.assertRaises(KeyError):
            self.repo.delete(remove_idx)
