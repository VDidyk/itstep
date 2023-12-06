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

    def remove(self):
        login = input("Enter the login: ")

        if login in self.users:
            del self.users[login]

    def check(self):
        login = input("Enter the login: ")

        user = self.find(login)

        if user:
            print("User exists")
        else:
            print("User does not exist")

    def find(self, login):
        if login in self.users:
            return self.users[login]
        else:
            return None

    def show(self):
        for u in self.users.values():
            print(u.login)

    def change_login(self):
        login = input("Enter the login: ")

        user = self.find(login)

        if user:
            self.users[login].login = input("Enter a new login: ")
        else:
            print("User does not exist")

    def change_password(self):
        login = input("Enter the login: ")

        user = self.find(login)

        if user:
            self.users[login].password = input("Enter a new password: ")
        else:
            print("User does not exist")


uc = UserContainer()

menu = Menu()
menu.append('Show users', lambda: uc.show())
menu.append('Add new user', lambda: uc.append())
menu.append('Remove user', lambda: uc.remove())
menu.append('Check user', lambda: uc.check())
menu.append('Change login', lambda: uc.change_login())
menu.append('Change login', lambda: uc.change_password())
menu.start()
