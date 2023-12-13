# При старті програми з’являється меню з наступними
# пунктами:
# 1. Завантаження даних;
# 2. Збереження даних;
# 3. Додавання даних;
# 4. Видалення даних.
# Використайте список цілих як сховища даних. Також
# застосуйте стиснення/розпакування даних.

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


@dataclass
class Container:
    _list = []

    def show(self):
        print(self._list)

    def append(self):
        self._list = input("Enter the value: ")

    def remove(self):
        try:
            del self._list[int(input("Enter the index"))]
        except Exception:
            pass

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

menu.start()
