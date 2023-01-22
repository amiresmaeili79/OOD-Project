class Actor:

    def __init__(self, pk: int, name: str, age: int):
        self.pk = pk
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age: int):
        self.age = age
