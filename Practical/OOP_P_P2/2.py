# Реалізуйте клас «Стадіон». Збережіть у класі: назву
# стадіону, дату відкриття, країну, місто, місткість. Реалізуйте
# методи класу для введення-виведення даних та інших
# операцій. До вже реалізованого класу «Стадіон» додайте
# необхідні перевантажені методи та оператори.

class Stadium:
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.capacity = capacity

    def __sub__(self, other):
        return abs(self.capacity - other.capacity)

    def __add__(self, other):
        return abs(self.capacity + other.capacity)

    def __mul__(self, other):
        return abs(self.capacity * other.capacity)

    def __truediv__(self, other):
        return abs(self.capacity / other.capacity)


stadion1 = Stadium("Стадіон 1", "01.01.1995", "Україна", "Київ", 4000)
stadion2 = Stadium("Стадіон 2", "01.01.1995", "Україна", "Київ", 6000)
print(stadion1 - stadion2)
print(stadion1 + stadion2)
print(stadion1 * stadion2)
print(stadion1 / stadion2)
