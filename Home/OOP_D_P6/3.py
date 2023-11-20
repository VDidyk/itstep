# Створіть базовий клас Shape для рисування плоских фігур.
# Визначте методи:
# ■ Show() — виведення на екран інформації про фігуру;
# ■ Save() — збереження фігури у файл;
# ■ Load() — зчитування фігури з файлу.
# Визначте похідні класи:
# ■ Square — квадрат із заданими з координатами лівого
# верхнього кута та довжиною сторони.
# ■ Rectangle — прямокутник із заданими координатами
# верхнього лівого кута та розмірами.
# ■ Circle — коло із заданими координатами центру та радіусом.
# ■ Ellipse — еліпс із заданими координатами верхнього кута
# описаного навколо нього прямокутника зі сторонами,
# паралельними осям координат, та розмірами цього прямокутника.
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну
# фігуру

import pickle


class Shape:
    def show(self):
        raise NotImplementedError

    def save(self):
        with open(self.__class__.__name__ + '.txt', 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(shape):
        with open(shape.__class__.__name__ + '.txt', 'rb') as file:
            return pickle.load(file)


class Square(Shape):
    _start: int
    _end: int

    def set_start(self, start: int):
        self._start = start

    def get_start(self):
        return self._start

    def set_end(self, end: int):
        self._end = end

    def get_end(self):
        return self._end

    def show(self):
        print(f"Square: start: {self._start} and end: {self._end}")


class Rectangle(Shape):
    _start: int
    _a: int
    _b: int

    def set_start(self, start: int):
        self._start = start

    def get_start(self):
        return self._start

    def set_a(self, a: int):
        self._a = a

    def get_a(self):
        return self._a

    def set_b(self, b: int):
        self._b = b

    def get_b(self):
        return self._b

    def show(self):
        print(f"Rectangle: start: {self._start}. A: {self._a}. B: {self._b}")


class Circle(Shape):
    _r: int
    _a: int
    _b: int

    def set_start(self, r: int):
        self._r = r

    def get_start(self):
        return self._r

    def set_a(self, a: int):
        self._a = a

    def get_a(self):
        return self._a

    def set_b(self, b: int):
        self._b = b

    def get_b(self):
        return self._b

    def show(self):
        print(f"Circle: R: {self._r}. Center point A: {self._a}. B: {self._b}")


class Ellipse(Shape):
    _start: int
    _a: int
    _b: int

    def set_start(self, start: int):
        self._start = start

    def get_start(self):
        return self._start

    def set_a(self, a: int):
        self._a = a

    def get_a(self):
        return self._a

    def set_b(self, b: int):
        self._b = b

    def get_b(self):
        return self._b

    def show(self):
        print(f"Ellipse: Start: {self._start}. A: {self._a}. B: {self._b}")


s = Square()
s.set_start(5)
s.set_end(15)

r = Rectangle()
r.set_start(5)
r.set_a(15)
r.set_b(20)

c = Circle()
c.set_start(5)
c.set_a(15)
c.set_b(20)

e = Ellipse()
e.set_start(5)
e.set_a(10)
e.set_b(20)

shapes = [s, r, c, e]

for shape in shapes:
    shape.save()

loaded_shapes = [Shape.load(shape) for shape in shapes]

for shape in loaded_shapes:
    shape.show()
