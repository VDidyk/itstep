# Створіть клас Circle з атрибутом radius та методом
# area, який поверне площу кола з вказаним радіусом.

class Circle:
    def __init__(self, radius: int):
        self._radius = radius

    def area(self):
        return 3.14 * (self._radius ** 2)

    def set_figure(self, radius: int):
        self._radius = radius


figure = Circle(10)
print(f"The area is {figure.area()}")
figure.set_figure(20)
print(f"The new area is {figure.area()}")
