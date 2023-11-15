# Створіть базовий клас «Тварина» та похідні класи:
# «Тигр», «Крокодил», «Кенгуру». Встановіть за допомогою
# конструктора ім’я кожної тварини та її характеристики.
# Створіть для кожного класу необхідні методи та поля.

class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        raise NotImplementedError("Not implemented.")


class Tiger(Animal):
    def __init__(self, name, speed):
        super().__init__(name)
        self.speed = speed

    def info(self):
        return f"Tiger {self.name} runs with speed {self.speed} km/h."


class Crocodile(Animal):
    def __init__(self, name, length):
        super().__init__(name)
        self.length = length

    def info(self):
        return f"Crocodile {self.name} has length {self.length} м."


class Kangaroo(Animal):
    def __init__(self, name, jump_distance):
        super().__init__(name)
        self.jump_distance = jump_distance

    def info(self):
        return f"Kangaroo {self.name} jumps {self.jump_distance} m."


tiger = Tiger("Kitty", 70)
crocodile = Crocodile("Ali", 4)
kangaroo = Kangaroo("Ken", 6)

print(tiger.info())
print(crocodile.info())
print(kangaroo.info())
