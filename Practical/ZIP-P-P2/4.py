# До вже реалізованого класу «Годинник» додайте
# мож-ливість стиснення та розпакування даних з
# використан-ням json та pickle.

import json
import pickle


class Clock:
    def __init__(self, manufacturer="", price=0, year=0, model="", type_of_clock=""):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.type_of_clock = type_of_clock

    def __str__(self):
        return (f"Model: {self.model}, Manufacturer: {self.manufacturer}, "
                f"Year: {self.year}, Price: {self.price}, type_of_clock: {self.type_of_clock}")

    def input(self):
        self.manufacturer = input("Enter the manufacturer: ")
        self.year = int(input("Enter the year: "))
        self.price = float(input("Enter the price: "))
        self.model = input("Enter the model: ")
        self.type_of_clock = input("Enter the type_of_clock: ")

    def __eq__(self, other):
        return (self.model == other.model and
                self.year == other.year and
                self.manufacturer == other.manufacturer and
                self.type_of_clock == other.type_of_clock and
                self.price == other.price)

    def show(self):
        print(self)

        # JSON Serialization

    def to_json(self):
        return json.dumps(
            {'manufacturer': self.manufacturer, 'price': self.price, 'year': self.year, 'model': self.model,
             'type_of_clock': self.type_of_clock})

        # JSON Deserialization

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['manufacturer'], data['price'], data['year'], data['model'], data['type_of_clock'])

    # Pickle Serialization
    def to_pickle(self):
        return pickle.dumps(self)

    # Pickle Deserialization
    @classmethod
    def from_pickle(cls, pickle_str):
        return pickle.loads(pickle_str)


# Example Usage
clock = Clock("Rolex", 10000, 2020, "Submariner", "Wristwatch")
json_data = clock.to_json()
pickle_data = clock.to_pickle()

clock_json = Clock.from_json(json_data)
clock_json.show()
clock_pickle = Clock.from_pickle(pickle_data)
clock_pickle.show()
