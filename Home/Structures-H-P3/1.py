# Розробіть додаток, що імітує чергу запитів до сервера.
# Мають бути клієнти, які надсилають запити на сервер, кожен
# з яких має свій пріоритет. Кожен новий клієнт потрапляє у
# чергу залежно від свого пріоритету. Зберігайте статистику
# запитів (користувач, час) в окремій черзі.
# Передбачте виведення статистики на екран. Вибір необхідних структур даних визначте самостійно.

from datetime import datetime
import random


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


class User:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority


class Request:
    def __init__(self, user):
        self.user = user
        self.date = datetime.now()

    def __str__(self):
        return f"{self.user.name}: {self.date}"


q = PriorityQueue(1000)

users = [
    User('Jack', 15),
    User('Vova', 3),
    User('Tailer', 1),
]

for i in range(1, 100):
    u = users[random.randint(0, 2)]
    q.insert_with_priority(Request(u), u.priority)

q.show()
