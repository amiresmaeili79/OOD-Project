from movie_ranking.repository.actor_repository import ActorRepository
from movie_ranking.repository.movie_repository import MovieRepository
from movie_ranking.repository.repository_registry import RepositoryRegistry

if __name__ == "__main__":
    repo_registry = RepositoryRegistry()
    movie_repo = MovieRepository()
    movie_repo.fill_mock()
    actor_repo = ActorRepository()
    actor_repo.fill_mock()

    repo_registry.add_repository(movie_repo, "")
    repo_registry.add_repository(actor_repo, "")

    print(repo_registry.movie.list())

