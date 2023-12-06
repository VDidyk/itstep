# Створіть клас черги для роботи із символьними значеннями. Ви маєте створити реалізації для операцій над
# елементами:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ Enqueue — додати новий елемент до черги;
# ■ Dequeue — видалення елемента з черги;
# ■ Show — відображення на екрані всіх елементів черги.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію

class Queue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def peek(self):
        if not self.is_empty():
            item = self.queue[0]
            print(f"{item}")
        else:
            print("Черга порожня")

    def enqueue(self, item, ):
        if not self.is_full():
            self.queue.append(item)
        else:
            print("Черга заповнена")

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Черга порожня")

    def show(self):
        if not self.is_empty():
            print("Елементи в черзі")
            for item in self.queue:
                print(f"Елемент {item}")
        else:
            print("Черга порожня")


q = Queue(6)
print(q.is_empty())

q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
q.show()
print(q.dequeue())
q.show()
