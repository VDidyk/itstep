# Історія дій: Створіть клас Calculator, який
# використовує стек для зберігання операцій та
# операндів. Методи класу можуть виконувати операції,
# зберігаючи їх у стеці для подальшого відновлення
# історії обчислень.

class Stack:
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        return self.__stack.pop()

    def size(self):
        return len(self.__stack)

    def clear(self):
        self.__stack = []

    def peek(self):
        if len(self.__stack) <= 0:
            raise Exception("Stack is empty")
        return self.__stack[-1]

    def __str__(self):
        return str(self.__stack)


class Calculator:
    def __init__(self):
        self.history = Stack()

    def add(self, x, y):
        result = x + y
        self.history.push((x, "+", y, result))
        return result

    def subtract(self, x, y):
        result = x - y
        self.history.push((x, "-", y, result))
        return result

    def multiply(self, x, y):
        result = x * y
        self.history.push((x, "*", y, result))
        return result

    def divide(self, x, y):
        if y == 0:
            raise ValueError("Zero dividing")
        result = x / y
        self.history.push((x, "/", y, result))
        return result

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []


c = Calculator()

print(c.add(2, 3))
print(c.multiply(2, 5))
print(c.divide(10, 2))
print(c.subtract(6, 3))
print(c.history)
