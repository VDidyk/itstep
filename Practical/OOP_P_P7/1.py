# Створіть клас Calculator, який може виконувати
# операції додавання, віднімання, множення та ділення.
# Кожна операція буде реалізована як метод класу.
# Об'єкт класу Calculator буде функтором, що може
# викликатися для виконання обраної операції.

class Calculator:
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Ділити на нуль не можна!")
        return a / b

    @staticmethod
    def plus(a, b):
        return a + b

    @staticmethod
    def minus(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    def __call__(self, *args, **kwargs):
        if args[0] == '/':
            return Calculator.divide(args[1], args[2])
        elif args[0] == '+':
            return Calculator.plus(args[1], args[2])
        elif args[0] == '-':
            return Calculator.minus(args[1], args[2])
        elif args[0] == '*':
            return Calculator.mul(args[1], args[2])


calculator = Calculator()
print(calculator("/", 4, 2))
print(calculator("+", 4, 2))
print(calculator("-", 4, 2))
print(calculator("*", 4, 2))
