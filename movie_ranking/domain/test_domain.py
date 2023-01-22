from unittest import TestCase

from ..domain.actor import Actor
from ..domain.award import Award
from ..domain.comment import Comment
from ..domain.movie import Movie


class TestMovie(TestCase):

    def setUp(self) -> None:
        self.movie = Movie(1, 3, 9, "Jaws", "Thriller", 1.5, 2000, "Scary movie about sharks")

    def test_set_name(self):
        self.movie.set_name("Jaws2")
        self.assertEqual(self.movie.get_name(), "Jaws2")
        self.movie.objects.clear()

    def test_add_awards(self):
        awards = Award(3, "Golden Globe", 2002)
        self.movie.add_awards()
        self.assertEqual(self.movie.awards, [awards])
        self.movie.objects.clear()

    def test_add_actors(self):
        actor = Actor(2, "Shark", 22)
        self.movie.add_actors()
        self.assertEqual(self.movie.stars, [actor])
        self.movie.objects.clear()

    def test_set_genre(self):
        self.movie.set_genre("Scary")
        self.assertEqual(self.movie.genre, "Scary")
        self.movie.objects.clear()

    def test_set_year(self):
        self.movie.set_year(2001)
        self.assertEqual(self.movie.get_year(), 2001)
        self.movie.objects.clear()

    def test_set_duration(self):
        self.movie.set_duration(2)
        self.assertEqual(self.movie.get_duration(), 2)
        self.movie.objects.clear()

    def test_set_description(self):
        self.movie.set_description(2)
        self.assertEqual(self.movie.get_description(), "A new movie")
        self.movie.objects.clear()

    def test_add_comments(self):
        comment = Comment(4, "Great Movie!")
        self.movie.add_comment(comment)
        self.assertEqual(self.movie.get_comments(), [comment])
        self.movie.objects.clear()


class TestActor(TestCase):

    def setUp(self) -> None:
        self.actor = Actor(2, "Shark", 22)

    def test_set_name(self):
        self.actor.set_name("Dolphin")
        self.assertEqual(self.actor.get_name(), "Dolphin")
        self.actor.objects.clear()

    def test_set_age(self):
        self.actor.set_age(25)
        self.assertEqual(self.actor.get_age(), 25)
        self.actor.objects.clear()


class TestAward(TestCase):

    def setUp(self) -> None:
        self.award = Award(3, "Golden Globe", 2002)

    def test_set_name(self):
        self.award.set_name("Oscar")
        self.assertEqual(self.award.get_name(), "Oscar")
        self.award.objects.clear()

    def test_set_year(self):
        self.award.set_year(2001)
        self.assertEqual(self.award.get_year(), 2001)
        self.award.objects.clear()


class TestComment(TestCase):

    def setUp(self) -> None:
        self.comment = Comment(4, "Great Movie!")

    def test_get_body(self):
        self.assertEqual(self.comment.get_body(), "Great Movie!")
        self.comment.objects.clear()
