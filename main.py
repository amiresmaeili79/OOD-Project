from movie_ranking.repository.actor_repository import ActorRepository
from movie_ranking.repository.movie_repository import MovieRepository
from movie_ranking.repository.repository_registry import RepositoryRegistry
from movie_ranking.service_layer.cliapi import CliApi
from movie_ranking.service_layer.name_search import NameSearch

if __name__ == "__main__":
    repo_registry = RepositoryRegistry()
    movie_repo = MovieRepository()
    movie_repo.fill_mock()
    actor_repo = ActorRepository()
    actor_repo.fill_mock()

    name_search = NameSearch()

    repo_registry.add_repository(movie_repo, "")
    repo_registry.add_repository(actor_repo, "")

    cli_api = CliApi(movie_repo, name_search)