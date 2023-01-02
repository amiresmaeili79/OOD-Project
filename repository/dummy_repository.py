from abstract_repository import AbstractRepository


class DummyRepository(AbstractRepository):
    """
    Dummy repo is just a toy class to demonstrate DB connection
    """

    def __init__(self) -> None:
        self.objects = []

    def config(self, configuration_str: str):
        # in dummy repo it is already configured
        return None
