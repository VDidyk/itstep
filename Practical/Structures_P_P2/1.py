# Реалізуйте клас стека роботи з цілими значеннями
# (стек цілих). Стек має бути фіксованого розміру.
# Реалізуйте набір операцій для роботи зі стеком
# o розміщення цілого значення у стеку;
# o виштовхування цілого значення зі стеку;
# o підрахунок кількості цілих у стеку;
# o перевірку, чи порожній стек;
# o перевірку, чи повний стек;
# o очищення стеку;
# o отримання значення без виштовхування
# верхнього цілого в стеку.
#  На старті додатка відобразіть меню, в якому
# користувач може вибрати необхідну операцію.


class Stack:
    def __init__(self, limit):
        self.__stack = []
        self.limit = limit

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.limit

    def push(self, item):
        if len(self.__stack) >= self.limit:
            raise Exception("Stack is full")
        self.__stack.append(item)

    def pop(self):
        if len(self.__stack) <= 0:
            raise Exception("Stack is empty")
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


stack = Stack(10)

for i in range(1, 11):
    stack.push(i)

print(stack)
print(stack.pop())
print(stack)
print(stack.size())
print(stack.is_full())
print(stack.is_empty())
print(stack.peek())
print(stack)
stack.clear()
print(stack)
print(stack.is_empty())
