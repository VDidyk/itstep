# Для класів із попереднього завдання реалізуйте магічний метод str, а також метод int (який повертає вік
# службовця).

from dataclasses import dataclass


@dataclass
class Employer:
    name: str
    age: int

    def __int__(self):
        return self.age

    def print(self):
        print(self)

    def __str__(self):
        return f"Name: {self.name}. Age: {self.age}"


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


e = Employer('Tom', 25)
e.print()

p = President('Jack', 54)
p.print()

m = Manager("Jenna", 19)
m.print()

w = Worker("Helga", 40)
w.print()

print(int(w))
