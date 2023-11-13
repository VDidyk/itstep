# До вже реалізованого класу «Дріб» додайте статичний метод, який при виклику повертає кількість створених об’єктів
# класу «Дріб».

class Fraction:
    _instances = 0

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        Fraction._instances += 1

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator  # спільний знаменник
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator  # спільний знаменник
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        other.denominator, other.numerator = other.numerator, other.denominator
        return Fraction.__mul__(self, other)

    @staticmethod
    def get_instance_count():
        return Fraction._instances


fraction1 = Fraction(4, 7)
fraction2 = Fraction(5, 8)
print(fraction1 + fraction2)
print(fraction1 - fraction2)
print(fraction1 * fraction2)
print(fraction1 / fraction2)

print(f"Instances count: {Fraction.get_instance_count()}")
