from WebPageContainer import WebPagesContainer
from WebPage import WebPage


class WebSite:
    _name: str
    _url: str
    _web_pages_container: WebPagesContainer = WebPagesContainer()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    def __str__(self):
        return f"Name: {self.name}. Url: {self.url}. Pages: {self._web_pages_container}\n"

    def add_web_page(self):
        page = WebPage()

        title = 'Test'
        while not title:
            title = input("Enter the title: ")

        content = 'Content'
        while not content:
            content = input("Enter the content: ")

        page.title = title
        page.content = content

        self._web_pages_container.add(page)

    def remove_web_page(self):
        title = input("Enter the title: ")

        if self._web_pages_container.remove(title):
            print(f"{title} has been removed")
        else:
            print(f"{title} has not been found")

    def display(self):
        print(self)

    @staticmethod
    def create() -> 'WebSite':
        name = 'Test'
        while not name:
            name = input("Enter the name: ")

        url = 'https://www.localhost.com'

        while not url:
            url = input("Enter the url: ")

        website = WebSite()
        website.name = name
        website._url = url

        return website
