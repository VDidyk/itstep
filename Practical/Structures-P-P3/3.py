# Розробіть додаток, який дозволяє зберігати інформацію
# про логіни і паролі користувачів. Кожному користувачеві
# відповідає пара «логін — пароль». При старті додатку
# відображається меню:
# ■ Додати нового користувача;
# ■ Видалити існуючого користувача;
# ■ Перевірити, чи існує такий користувач;
# ■ Змінити логін існуючого користувача;
# ■ Змінити пароль існуючого користувача.
# Для реалізації завдання обов’язково застосуйте одну
# із структур даних. При виборі структури керуйтеся постановкою завдання.

import sys

sys.path.append('../../Libraries')
from Menu import Menu


class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password


class UserContainer:
    def __init__(self):
        self.users = {}

    def append(self):
        login = input("Enter the login: ")

        user = self.find(login)

        if user:
            print(f"User {login} already exists!")
        else:
            self.users[login] = User(login, input("Enter the password: "))

    def find(self, login):
        if login in self.users:
            return self.users[login]
        else:
            return None

    def show(self):
        for u in self.users.values():
            print(u.login)


uc = UserContainer()

menu = Menu()
menu.append('Show users', lambda: uc.show())
menu.append('Add new user', lambda: uc.append())
menu.start()
