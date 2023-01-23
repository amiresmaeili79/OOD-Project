from unittest import TestCase

from ..domain.actor import Actor
from ..domain.award import Award
from ..domain.comment import Comment
from ..domain.movie import Movie


class TestMovie(TestCase):

    def setUp(self) -> None:
        self.movie = Movie(1, 3, 9, "Jaws", "Thriller", 1.5, 2000, "Scary movie about sharks",
        [],[],[])

    def test_set_name(self):
        self.movie.set_name("Jaws2")
        self.assertEqual(self.movie.get_name(), "Jaws2")

    def test_add_awards(self):
        awards = Award(3, "Golden Globe", 2002)
        self.movie.add_awards(awards)
        self.assertEqual(self.movie.awards, [awards])

    def test_add_actors(self):
        actor = Actor(2, "Shark", 22)
        self.movie.add_actors(actor)
        self.assertEqual(self.movie.stars, [actor])

    def test_set_genre(self):
        self.movie.set_genre("Scary")
        self.assertEqual(self.movie.genre, "Scary")

    def test_set_year(self):
        self.movie.set_year(2001)
        self.assertEqual(self.movie.get_year(), 2001)

    def test_set_duration(self):
        self.movie.set_duration(2)
        self.assertEqual(self.movie.get_duration(), 2)

    def test_set_description(self):
        self.movie.set_description("A new movie")
        self.assertEqual(self.movie.get_description(), "A new movie")

    def test_add_comments(self):
        comment = Comment(4, "Great Movie!")
        self.movie.add_comment(comment)
        self.assertEqual(self.movie.get_comments(), [comment])


class TestActor(TestCase):

    def setUp(self) -> None:
        self.actor = Actor(2, "Shark", 22)

    def test_set_name(self):
        self.actor.set_name("Dolphin")
        self.assertEqual(self.actor.get_name(), "Dolphin")

    def test_set_age(self):
        self.actor.set_age(25)
        self.assertEqual(self.actor.get_age(), 25)


class TestAward(TestCase):

    def setUp(self) -> None:
        self.award = Award(3, "Golden Globe", 2002)

    def test_set_name(self):
        self.award.set_name("Oscar")
        self.assertEqual(self.award.get_name(), "Oscar")

    def test_set_year(self):
        self.award.set_year(2001)
        self.assertEqual(self.award.get_year(), 2001)


class TestComment(TestCase):

    def setUp(self) -> None:
        self.comment = Comment("Great Movie!")

    def test_get_body(self):
        self.assertEqual(self.comment.get_body(), "Great Movie!")
