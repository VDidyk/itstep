# Створіть клас Ship, який містить інформацію про кораблі.
# За допомогою механізму успадкування реалізуйте клас
# Frigate (містить інформацію про фрегат), клас Destroyer(містить
# інформацію про есмінця), клас Cruiser (містить інформацію
# про крейсер).
# Кожен із класів має містити необхідні для роботи методи.

class Ship:
    def __init__(self, name, year_built):
        self.name = name
        self.year_built = year_built

    def get_info(self):
        print(f"Name: {self.name}, Year: {self.year_built}")


class Frigate(Ship):
    def __init__(self, name, year_built, armament):
        super().__init__(name, year_built)
        self.armament = armament

    def get_info(self):
        print(f"{super().get_info()}, Armament: {self.armament}")


class Destroyer(Ship):
    def __init__(self, name, year_built, speed):
        super().__init__(name, year_built)
        self.speed = speed

    def get_info(self):
        print(f"{super().get_info()}, Speed: {self.speed} knots")


class Cruiser(Ship):
    def __init__(self, name, year_built, displacement):
        super().__init__(name, year_built)
        self.displacement = displacement

    def get_info(self):
        print(f"{super().get_info()}, Displacement: {self.displacement} tons")


frigate = Frigate("Frigate-1", 1995, "Missiles")
destroyer = Destroyer("Destroyer-1", 2005, 30)
cruiser = Cruiser("Cruiser-1", 2022, 10000)

frigate_info = frigate.get_info()
destroyer_info = destroyer.get_info()
cruiser_info = cruiser.get_info()
