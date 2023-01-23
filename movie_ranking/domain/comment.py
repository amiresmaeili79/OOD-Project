import datetime


class Comment:

    def __init__(self, body: str):
        self.body = body
        self.datetime = datetime.datetime.now()

    def get_body(self):
        return self.body

    def get_datetime(self):
        return self.datetime
