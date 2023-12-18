# До вже реалізованого класу «Стадіон» додайте можливість
# стиснення та розпакування даних з використанням json та
# pickle

import json
import zlib
import pickle


class DataWorker:
    file_path = '3.txt'

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


class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __sub__(self, other):
        return abs(self.capacity - other.capacity)

    def __add__(self, other):
        return abs(self.capacity + other.capacity)

    def __mul__(self, other):
        return abs(self.capacity * other.capacity)

    def __truediv__(self, other):
        return abs(self.capacity / other.capacity)

    def __str__(self):
        return f"{self.name} {self.country} {self.city} {self.capacity} {self.opening_date}"

    def __dict__(self):
        return {
            "name": self.name,
            "opening_date": self.opening_date,
            "country": self.country,
            'city': self.city,
            "capacity": self.capacity
        }

    @staticmethod
    def save(s):
        DataWorker.save(json.dumps(s.__dict__()))

    @staticmethod
    def load():
        obj = DataWorker.read()

        if obj:
            obj = json.loads(obj)
            return Stadium(obj['name'], obj['opening_date'], obj['country'], obj['city'], obj['capacity'])
        else:
            return None


s = Stadium("TMP", '16.01.1995', "UK", "London", 100000)
s.save(s)

s = Stadium.load()
print(s)
