# Створіть клас Human, який міститиме інформацію
# про людину.
# За допомогою механізму успадкування реалізуйте
# клас Builder (містить інформацію про будівельника),
# клас Sailor (містить інформацію про моряка), клас Pilot
# (містить інформацію про льотчика).
# Кожен із класів має містити необхідні для роботи
# методи.

class Human:
    def __init__(self, name: str = ''):
        self.name = name


class Builder(Human):
    def build(self):
        print(f"{self.name} is building...")


class Sailor(Human):
    def swim(self):
        print(f"{self.name} is swimming...")


class Pilot(Human):
    def fly(self):
        print(f"{self.name} is flying...")


builder = Builder("Tom")
builder.build()

sailor = Sailor("Jack")
sailor.swim()

pilot = Pilot("John")
pilot.fly()
