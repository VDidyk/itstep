# Створіть базовий клас «Фігура» з методом для підрахунку
# площі. Створіть похідні класи: прямокутник, коло, прямокутний трикутник, трапеція, зі своїми методами для підрахунку
# площі
import math
from dataclasses import dataclass


class Figure:
    def get_area(self):
        print(f"{self.__class__.__name__} area is {self._calculate()}")

    def _calculate(self):
        raise NotImplementedError


@dataclass
class Rectangle(Figure):
    a: int
    b: int

    def _calculate(self):
        return self.a * self.b


@dataclass
class Circle(Figure):
    r: int

    def _calculate(self):
        return math.pi * (self.r * self.r)


@dataclass
class RightTriangle(Figure):
    a: int
    b: int

    def _calculate(self):
        return 0.5 * self.a * self.b


@dataclass
class Trapeze(Figure):
    a: int
    b: int
    h: int

    def _calculate(self):
        return ((self.a + self.b) / 2) * self.h


figures = [
    Rectangle(5, 15),
    Circle(15),
    RightTriangle(5, 15),
    Trapeze(5, 15, 20),
]

[x.get_area() for x in figures]
