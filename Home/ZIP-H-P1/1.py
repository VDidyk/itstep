# Маємо певний словник з назвами країн і столиць. Назва
# країни використовується як ключ, назва столиці — як значення. Реалізуйте: додавання, видалення, пошук, редагування,
# збереження та завантаження даних (використовуючи стиснення та розпакування).

import zlib
import pickle
from dataclasses import dataclass
import sys

sys.path.append('../../Libraries')
from Menu import Menu


class DataWorker:
    file_path = '1'

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


class Country:
    def __init__(self, name, capital):
        self.name = name
        self.capital = capital

    def __str__(self):
        return f"{self.name}:{self.capital}"


class Container:
    def __init__(self):
        self._list = []

    def show(self):
        if self._list:
            for u in self._list:
                print(u)

    def append(self):
        self._list.append(Country(input("Enter name: "), input("Enter capital: ")))

    def remove(self):
        try:
            del self._list[int(input("Enter the index: "))]
        except Exception:
            pass

    def edit(self):
        try:
            u = self._list[int(input("Enter the index: "))]

            if u:
                u.name = input("Enter a new name: ")
                u.capital = input("Enter a new capital: ")
        except Exception:
            pass

    def search(self, name):
        for u in self._list:
            if u.name == name:
                print(u)
                return

        print("Country was not found")

    def load(self):
        self._list = DataWorker.read()
        if self._list == None:
            self._list = []

    def save(self):
        DataWorker.save(self._list)


c = Container()

menu = Menu()

menu.append('Show Data', lambda: c.show())
menu.append('Load Data', lambda: c.load())
menu.append('Save Data', lambda: c.save())
menu.append('Add Data', lambda: c.append())
menu.append('Delete Data', lambda: c.remove())
menu.append('Search Country', lambda: c.search(input("Enter a name: ")))
menu.append('Edit Country', lambda: c.edit())

menu.start()
