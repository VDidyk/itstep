from WebPage import WebPage


class WebPagesContainer:
    _web_pages: list = []

    def add(self, web_page: WebPage):
        self._web_pages.append(web_page)

    def remove(self, title) -> bool:
        for page in self._web_pages:
            if page.title == title:
                self._web_pages.remove(page)
                return True

        return False

    def __str__(self):
        result = ''
        for page in self._web_pages:
            result += str(page) + "\n"
        return result
