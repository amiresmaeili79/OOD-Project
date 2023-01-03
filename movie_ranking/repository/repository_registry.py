from typing import Dict

from .repository_interface import RepositoryInterface


class RepositoryRegistry:

    def __init__(self) -> None:
        self.registries: Dict[str, "RepositoryInterface"] = {}

    def add_repository(self, repo: "RepositoryInterface", configuration: str) -> None:
        setattr(self, str(repo), repo)
        repo.config(configuration)
