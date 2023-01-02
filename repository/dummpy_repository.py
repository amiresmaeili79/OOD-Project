from .abstract_repository import AbstractRepository



class DummyRepository(AbstractRepository):

    """
    Dummpy repo is just a toy class to demonestrate DB connection
    """

    def __init__(self) -> None:
        self.movies = []
        self.actors = []
    
    def config(configuration_str: str):
        # in dummpy repo it is already configured
        return None