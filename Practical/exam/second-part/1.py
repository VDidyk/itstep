# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.
# Додаткові можливості (за бажанням на кристалики):
# Реалізуйте систему логіну/реєстрації для керування
# сайтом. Додайте можливість редагування існуючих сторінок.
# Створіть функціонал для пошуку сторінок за ключовими
# словами у заголовку або вмісті.


from WebSite import WebSite

import sys

sys.path.append('../../../Libraries')
from Menu import Menu

web_sites = []


def create_web_site():
    web_sites.append(WebSite.create())


def show_websites():
    for index, web_site in enumerate(web_sites):
        print(f"{index + 1}. {web_site.name}")


def pick_website():
    if not len(web_sites):
        return

    show_websites()

    index = int(input(f"Choose the one (number [1-{len(web_sites)}]): ")) - 1

    if 0 <= index < len(web_sites):
        return index

    return None


def show_website():
    index = pick_website()

    if index is not None:
        print(web_sites[index])


def add_pages():
    index = pick_website()

    if index is not None:
        web_sites[index].add_web_page()


def remove_page():
    index = pick_website()

    if index is not None:
        web_sites[index].remove_web_page()


menu = Menu()

menu.append("Show all websites: ", show_websites)
menu.append("Show a website", show_website)
menu.append("Create a website", create_web_site)
menu.append("Add a page", add_pages)
menu.append("Remove a page", remove_page)

menu.start()
