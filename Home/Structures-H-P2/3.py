# Дано три вежі та n дисків різного розміру, відсортованих
# за зростанням, розміщених на першій вежі у вигляді піраміди.
# Потрібно перемістити всі диски на третю вежу,
# використовуючи проміжну вежу, за умови, що можна
# переміщати тільки один диск за раз та диск завжди можна
# покласти лише на диск більшого розміру або на порожню
# вежу.
# Ця задача може бути вирішена за допомогою
# рекурсивного алгоритму, використовуючи стек для
# зберігання проміжних ходів при переміщенні дисків між
# вежами.

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


def hanoi(n, source, middleware, target, stack):
    if n == 1:
        target.push(source.pop())
    else:
        hanoi(n - 1, source, target, middleware, stack)
        target.push(source.pop())
        hanoi(n - 1, middleware, source, target, stack)


s1 = Stack()
s2 = Stack()
s3 = Stack()

for i in range(1, 21):
    s1.push(i)

print(s1)
print(s2)
print(s3)

hanoi(s1.size(), s1, s2, s3, None)

print(s1)
print(s2)
print(s3)
