# Створіть клас для підрахунку площі геометричних
# фігур. Клас має надавати функціональність підрахунку
# площі трикутника за різними формулами, площі прямокутника, площі квадрата, площі ромба. Методи класу для
# підрахунку площі реалізуйте за допомогою статичних
# методів. Також клас має розрахувати кількість підрахунків площі та повернути це значення статичним методом.

class AreaCalculator:
    calculation_count = 0

    @staticmethod
    def calculate_triangle_area_by_sides(a, b, c):
        # Півпериметр для формули Герона
        s = (a + b + c) / 2
        AreaCalculator.calculation_count += 1
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5

    @staticmethod
    def calculate_triangle_area_by_base_height(base, height):
        AreaCalculator.calculation_count += 1
        return 0.5 * base * height

    @staticmethod
    def calculate_rectangle_area(length, width):
        AreaCalculator.calculation_count += 1
        return length * width

    @staticmethod
    def calculate_square_area(side):
        AreaCalculator.calculation_count += 1
        return side ** 2

    @staticmethod
    def calculate_rhombus_area(diagonal1, diagonal2):
        AreaCalculator.calculation_count += 1
        return 0.5 * diagonal1 * diagonal2

    @staticmethod
    def get_calculation_count():
        return AreaCalculator.calculation_count


print(AreaCalculator.calculate_square_area(20))
print(AreaCalculator.get_calculation_count())
