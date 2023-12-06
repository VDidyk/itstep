# Створіть клас черги з пріоритетами для роботи із
# символьними значеннями.
# Ви маєте створити реалізації для операцій над елементами черги:
# ■ IsEmpty — перевірка, чи черга пуста;
# ■ IsFull — перевірка черги на заповнення;
# ■ InsertWithPriority — додати елемент з пріоритетом у
# чергу;
# Практичне завдання
# 1
# ■ PullHighestPriorityElement — видалення елемента з
# найвищим пріоритетом із черги;
# ■ Peek — повернення найбільшого за пріоритетом елемента. Зверніть увагу, що елемент не видаляється з
# черги;
# ■ Show — відображення на екрані всіх елементів черги.
# Показуючи елемент, також необхідно вказати і його
# пріоритет.
# На старті додатка відобразіть меню, в якому користувач може вибрати необхідну операцію.


class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.capacity

    def insert_with_priority(self, item, priority):
        if not self.is_full():
            self.queue.append((item, priority))  # кортеж (елемент, пріорітет)
            print(f"Елемент {item} з пріорітетом {priority} додано до черги")
            self.queue.sort(key=lambda x: x[1])  # сортування за пріорітетом
        else:
            print("Черга заповнена")

    def pull_hignest_priority_element(self):
        if not self.is_empty():
            item, priority = self.queue.pop(0)
            print(f"Елемент {item} з пріорітетом {priority} вилучено з черги")
        else:
            print("Черга порожня")

    def peek(self):
        if not self.is_empty():
            item, priority = self.queue[0]
            print(f"Найбільший за пріорітетом {priority} елемент {item}")
        else:
            print("Черга порожня")

    def show(self):
        if not self.is_empty():
            print("Елементи в черзі")
            for item, priority in self.queue:
                print(f"Елемент {item} з {priority}-пріорітетом")
        else:
            print("Черга порожня")


q = PriorityQueue(6)
print(q.is_empty())
q.insert_with_priority("Hello", 1)
q.insert_with_priority("World", 3)
q.show()
q.insert_with_priority("Python", 1)
q.insert_with_priority("Zero", 1)
q.insert_with_priority("Apple", 1)
q.insert_with_priority(1, 2)
q.show()
print()
q.pull_hignest_priority_element()
q.show()
