# Маємо певний словник з назвами музичних груп (виконавців) та альбомів. Назва групи використовується як ключ,
# назва альбомів — як значення. Реалізуйте: додавання, видалення, пошук, редагування, збереження та завантаження
# даних (використовуючи стиснення та розпакування)

import zlib
import pickle
from dataclasses import dataclass
import sys

sys.path.append('../../Libraries')
from Menu import Menu


class DataWorker:
    file_path = '2'

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


class Band:
    def __init__(self, name, albums):
        self.name = name
        self.albums = albums

    def __str__(self):
        return f"{self.name}:{self.albums}"


class Container:
    def __init__(self):
        self._list = []

    def show(self):
        if self._list:
            for u in self._list:
                print(u)

    def append(self):
        self._list.append(Band(input("Enter name: "), input("Enter albums separating by coma: ").split(',')))

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
                u.albums = input("Enter a new albums separating by coma: ").split(',')
        except Exception:
            pass

    def search(self, name):
        for u in self._list:
            if u.name == name:
                print(u)
                return

        print("Band was not found")

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
menu.append('Search Band', lambda: c.search(input("Enter a name: ")))
menu.append('Edit Country', lambda: c.edit())

menu.start()
