# Змініть стек із першого завдання таким чином, щоб його
# розмір був нефіксованим.

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


stack = Stack()

for i in range(1, 30):
    stack.push(i)

print(stack)
print(stack.pop())
print(stack)
print(stack.size())
print(stack.is_empty())
print(stack.peek())
print(stack)
stack.clear()
print(stack)
print(stack.is_empty())
