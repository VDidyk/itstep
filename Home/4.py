# Реалізуйте клас «Годинник». Збережіть у класі:
# назву моделі годинника, виробника годинника, рік
# випуску, ціну годинника, тип годинника (наручний,
# настінний і т. д.). Реалізуйте конструктор та методи
# класу для введення-виведення даних, а також для
# інших операцій. Використовуйте механізм
# перевантаження методів.


class Clock:
    def __init__(self, manufacturer="", price=0, year=0, model="", type_of_clock=""):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.price = price
        self.type_of_clock = type_of_clock

    def __str__(self):
        return (f"Model: {self.model}, Manufacturer: {self.manufacturer}, "
                f"Year: {self.year}, Price: {self.price}, type_of_clock: {self.type_of_clock}")

    def input(self):
        self.manufacturer = input("Enter the manufacturer: ")
        self.year = int(input("Enter the year: "))
        self.price = float(input("Enter the price: "))
        self.model = input("Enter the model: ")
        self.type_of_clock = input("Enter the type_of_clock: ")

    def __eq__(self, other):
        return (self.model == other.model and
                self.year == other.year and
                self.manufacturer == other.manufacturer and
                self.type_of_clock == other.type_of_clock and
                self.price == other.price)

    def show(self):
        print(self)


clock1 = Clock("Rolex", 5011, 2023, "gold", "watch")
clock2 = Clock("Gipson", 50, 2012, "Chine", "wall")

clock1.show()
clock2.show()

print(clock1 == clock2)

clock3 = Clock()
clock3.input()
clock3.show()
