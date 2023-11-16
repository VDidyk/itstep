# Використовуючи механізм множинного успадкування, створіть клас «Автомобіль». Також мають бути класи:
# «Колеса», «Двигун», «Двері» та ін.
from dataclasses import dataclass


@dataclass
class Wheels:
    count: int


@dataclass
class Engine:
    power: float


@dataclass
class Doors:
    count: int


class Car(Wheels, Engine, Doors):
    def __init__(self):
        super().__init__(4)
        Engine.__init__(2)
        Doors.__init__(4)
