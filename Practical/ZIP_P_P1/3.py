# Маємо певний словник з логінами і паролями користувачів. Логін використовується як ключ, пароль —
# як значення. Реалізуйте: додавання, видалення, пошук,
# редагування, збереження та завантаження даних (використовуючи стиснення та розпакування).

import zlib
import pickle
from dataclasses import dataclass
import sys

sys.path.append('../../Libraries')
from Menu import Menu


class DataWorker:
    file_path = '3'

    @staticmethod
    def save(data):
        compressed_data = zlib.compress(pickle.dumps(data))
        with open(DataWorker.file_path, 'wb') as file:
            file.write(compressed_data)

    @staticmethod
    def read():
        try:
            with open(DataWorker.file_path, 'rb') as file:
                read_compressed_data = file.read()
                return pickle.loads(zlib.decompress(read_compressed_data))
        except FileNotFoundError:
            return None


class User:
    def __init__(self, login, password):
        self._login = login
        self._password = password

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, login):
        self._login = login

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    def __str__(self):
        return f"{self._login}:{self._password}"


class Container:
    def __init__(self):
        self._list = []

    def show(self):
        for u in self._list:
            print(u)

    def append(self):
        self._list.append(User(input("Enter login: "), input("Enter password: ")))

    def remove(self):
        try:
            del self._list[int(input("Enter the index: "))]
        except Exception:
            pass

    def edit(self):
        try:
            u = self._list[int(input("Enter the index: "))]

            if u:
                u.login = input("Enter a new Login: ")
        except Exception:
            pass

    def search(self, login):
        for u in self._list:
            if u.login == login:
                print(u)
                return

        print("User was not found")

    def load(self):
        self._list = DataWorker.read()

    def save(self):
        DataWorker.save(self._list)


c = Container()

menu = Menu()

menu.append('Show Data', lambda: c.show())
menu.append('Load Data', lambda: c.load())
menu.append('Save Data', lambda: c.save())
menu.append('Add Data', lambda: c.append())
menu.append('Delete Data', lambda: c.remove())
menu.append('Search User', lambda: c.search(input("Enter a login: ")))
menu.append('Edit User', lambda: c.edit())

menu.start()
