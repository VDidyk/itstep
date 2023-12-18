# Реалізація програми для додавання, видалення та
# відстеження завдань/заміток. Зберігати ці завдання у
# форматі JSON у файлі. Можливість завантаження
# раніше збережених завдань для подальшої роботи з
# ними.

import json
import sys

sys.path.append('../../Libraries')
from Menu import Menu


class TaskManager:
    def __init__(self, filename='tasks.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
        else:
            print("Task index out of range.")

    def show(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}: {task}")


task_manager = TaskManager()

menu = Menu()

menu.append('Show tasks', lambda: task_manager.show())
menu.append('Add task', lambda: task_manager.add_task(input("Enter a new task: ")))
menu.append('Remove task', lambda: task_manager.remove_task(int(input("Enter task index to remove: "))))
menu.start()
