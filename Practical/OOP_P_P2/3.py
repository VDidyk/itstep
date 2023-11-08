# До вже реалізованого класу «Автомобіль» додайте необхідні перевантажені методи та оператори.

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The engine of the {self.year} {self.brand} {self.model} has started!")

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    def __repr__(self):
        return f"Car('{self.brand}', '{self.model}', {self.year})"


car1 = Car("Mazda", "CX5", 2016)
car2 = Car("BMW", "X5", 2012)

car1.start_engine()

print(car1 == car2)
print(car1 < car2)
