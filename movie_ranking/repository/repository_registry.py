from typing import Dict
from repository_interface import RepositoryInterface

class RepositoryRegistry:

    def __init__(self) -> None:
        self.registeries: Dict[str, "RepositoryInterface"] = {}
    

    def add_repository(self, repo: "RepositoryInterface", configuration: str) -> None:
        self.registeries[str(repo)] = repo
        repo.config(configuration)
    

    def objects(self, repo_name: str) -> "RepositoryInterface":
        return self.registeries[repo_name]