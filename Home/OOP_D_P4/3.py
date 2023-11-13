# Створіть клас для підрахунку максимуму з чотирьох
# аргументів, мінімуму з чотирьох аргументів, середнє
# арифметичне із чотирьох аргументів, факторіалу аргументу. Реалізуйте функціональність у вигляді статичних
# методів.

class MathOperations:
    @staticmethod
    def max_of_four(a, b, c, d):
        return max(a, b, c, d)

    @staticmethod
    def min_of_four(a, b, c, d):
        return min(a, b, c, d)

    @staticmethod
    def average_of_four(a, b, c, d):
        return (a + b + c + d) / 4

    @staticmethod
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * MathOperations.factorial(n - 1)


print(MathOperations.factorial(20))
