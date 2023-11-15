# Створіть клас Device, який містить інформацію про пристрій.
# За допомогою механізму успадкування реалізуйте клас
# Coffee Machine (містить інформацію про кавомашину), клас
# Blender (містить інформацію про блендер), клас MeatGrinder
# (містить інформацію про м’ясорубку).
# Кожен із класів має містити необхідні для роботи методи.

class Device:
    def __init__(self, model, manufacture):
        self.model = model
        self.manufacture = manufacture
        self.name = ''

    def info(self):
        return f"{self.name} {self.manufacture} {self.model}"

    def do(self):
        raise NotImplementedError


class CoffeeMachine(Device):
    def __init__(self, model, manufacture):
        super().__init__(model, manufacture)
        self.name = 'Coffee Machine'

    def do(self):
        print(self.info() + ' is making coffe')


class Blender(Device):
    def __init__(self, model, manufacture):
        super().__init__(model, manufacture)
        self.name = 'Blender'

    def do(self):
        print(self.info() + ' is blending')


class MeatGrinder(Device):
    def __init__(self, model, manufacture):
        super().__init__(model, manufacture)
        self.name = 'Meat Grinder'

    def do(self):
        print(self.info() + ' is making grinding')


coffee_machine = CoffeeMachine('X65', "Bakky")
coffee_machine.do()

blender = Blender("SKI22", "Blleny")
blender.do()

grinder = MeatGrinder("OKS233", "Grinny")
grinder.do()
