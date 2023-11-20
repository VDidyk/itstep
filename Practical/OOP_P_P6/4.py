# Створіть базовий клас Employer (службовець) з функцією Print(). Функція має виводити інформацію про службовця. Для базового класу це може бути рядок із написом
# «This is Employer class».
# Створіть від нього три похідні класи: President, Manager, Worker. Перевизначте функцію Print() для виведення
# інформації, що відповідає кожному типу службовця.

from dataclasses import dataclass


@dataclass
class Employer:
    name: str

    def print(self):
        print(f"Name: {self.name}.")


class President(Employer):
    def print(self):
        super().print()
        print("This is President class")


class Manager(Employer):
    def print(self):
        super().print()
        print("This is Manager class")


class Worker(Employer):
    def print(self):
        super().print()
        print("This is Worker class")


e = Employer('Tom')
e.print()

p = President('Jack')
p.print()

m = Manager("Jenna")
m.print()

w = Worker("Helga")
w.print()
