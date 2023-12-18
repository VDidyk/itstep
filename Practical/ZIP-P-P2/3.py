# До вже реалізованого класу «Дріб» додайте можливість стиснення та розпакування даних з
# використанням json та pickle.

import json
import pickle


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator  # спільний знаменник
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator  # спільний знаменник
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        other.denominator, other.numerator = other.numerator, other.denominator
        return Fraction.__mul__(self, other)

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    # Existing methods ...

    # JSON Serialization
    def to_json(self):
        return json.dumps({'numerator': self.numerator, 'denominator': self.denominator})

    # JSON Deserialization
    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data['numerator'], data['denominator'])

    # Pickle Serialization
    def to_pickle(self):
        return pickle.dumps(self)

    # Pickle Deserialization
    @classmethod
    def from_pickle(cls, pickle_str):
        return pickle.loads(pickle_str)


f = Fraction(1, 2)
json_data = f.to_json()
pickle_data = f.to_pickle()

f_json = Fraction.from_json(json_data)
f_pickle = Fraction.from_pickle(pickle_data)
