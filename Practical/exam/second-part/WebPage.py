import datetime


class WebPage:
    _title: str
    _content: str
    _published_at: datetime

    def __init__(self):
        self._published_at = datetime.datetime.now()

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def published_at(self):
        return self._published_at

    def __str__(self):
        return f"{self.title}. Published at: {self.published_at}. Content: {self.content}"

    def display(self):
        print(self)
