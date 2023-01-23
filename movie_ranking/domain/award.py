class Award:

    def __init__(self, pk: int, name: str, year: int):
        self.pk = pk
        self.name = name
        self.year = year

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_year(self):
        return self.year

    def set_year(self, year: int):
        self.year = year
