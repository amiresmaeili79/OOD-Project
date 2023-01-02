import datetime


class Comment:

    def __init__(self, pk: int, body: str):
        self.pk = pk
        self.body = body
        self.datetime = datetime.datetime.now()

    def get_body(self):
        # code
        return True

    def get_datetime(self):
        # code
        return True
