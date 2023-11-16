# Використовуючи поняття множинного успадкування,
# створіть клас «Коло, поміщене в квадрат».

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)


class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class CircleInSquare(Circle, Square):
    def __init__(self, side):
        Circle.__init__(self, side / 2)
        Square.__init__(self, side)

    def show(self):
        print(f"Circle Area: {self.area()}")
        print(f"Square Area: {Square.area(self)}")


circle_in_square = CircleInSquare(5)
circle_in_square.show()
