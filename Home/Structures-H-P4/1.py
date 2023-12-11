# Реалізуйте базу даних зі штрафами податкової
# інспекції. Ідентифікувати кожну конкретну людину буде
# персональний ідентифікаційний код. В однієї людини може
# бути багато штрафів.
# Реалізуйте:
# 1. Повний друк бази даних;
# 2. Друк даних за конкретним кодом;
# 3. Друк даних за конкретним типом штрафу;
# 4. Друк даних за конкретним містом;
# 5. Додавання нової людини з інформацією про неї;
# 6. Додавання нових штрафів для вже існуючого запису;
# 7. Видалення штрафу;
# 8. Заміна інформації про людину та її штрафи.
# Використайте дерево для реалізації цього завдання.

import sys

sys.path.append('../../Libraries')
from Menu import Menu


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Person:
    def __init__(self, id_code, name, city):
        self.id_code = id_code
        self.name = name
        self.city = city
        self.fines = []

    def add_fine(self, fine_type, amount):
        self.fines.append({"type": fine_type, "amount": amount})

    def __repr__(self):
        return f"{self.id_code}: {self.name}, {self.city}, Fines: {self.fines}"


class TaxFineTree:
    def __init__(self):
        self.root = None

    def insert_person(self, person):
        if self.root is None:
            self.root = Node(person)
        else:
            self._insert_recursive(person, self.root)

    def _insert_recursive(self, person, current_node):
        if person.id_code < current_node.value.id_code:
            if current_node.left is None:
                current_node.left = Node(person)
            else:
                self._insert_recursive(person, current_node.left)
        elif person.id_code > current_node.value.id_code:
            if current_node.right is None:
                current_node.right = Node(person)
            else:
                self._insert_recursive(person, current_node.right)

    def find_person(self, id_code):
        return self._find_recursive(id_code, self.root)

    def _find_recursive(self, id_code, current_node):
        id_code = int(id_code)
        if current_node is None:
            return None
        if id_code == current_node.value.id_code:
            return current_node.value
        elif id_code < current_node.value.id_code:
            return self._find_recursive(id_code, current_node.left)
        else:
            return self._find_recursive(id_code, current_node.right)

    def add_fine_to_person(self, id_code, fine_type, amount):
        person = self.find_person(id_code)
        if person:
            person.add_fine(fine_type, amount)
        else:
            print(f"No person found with ID code {id_code}")

    def print_all(self):
        self._print_recursive(self.root)

    def _print_recursive(self, current_node):
        if current_node is not None:
            self._print_recursive(current_node.left)
            print(current_node.value)
            self._print_recursive(current_node.right)

    def print_by_fine_type(self, fine_type):
        self._print_by_fine_type_recursive(self.root, fine_type)

    def _print_by_fine_type_recursive(self, current_node, fine_type):
        if current_node is not None:
            self._print_by_fine_type_recursive(current_node.left, fine_type)
            for fine in current_node.value.fines:
                if fine['type'] == fine_type:
                    print(current_node.value)
                    break
            self._print_by_fine_type_recursive(current_node.right, fine_type)

    def print_by_city(self, city):
        self._print_by_city_recursive(self.root, city)

    def _print_by_city_recursive(self, current_node, city):
        if current_node is not None:
            self._print_by_city_recursive(current_node.left, city)
            if current_node.value.city == city:
                print(current_node.value)
            self._print_by_city_recursive(current_node.right, city)


t = TaxFineTree()
t.insert_person(Person(123, "Tailer", "Lviv"))
t.add_fine_to_person(123, "Road", 666)

menu = Menu()

menu.append("Print entire database", lambda: t.print_all())
menu.append("Print data by ID code", lambda: print(t.find_person(input("Enter ID code: "))))
menu.append("Print data by fine type", lambda: t.print_by_fine_type(input("Enter fine type: ")))
menu.append("Print data by city", lambda: t.print_by_city(input("Enter city: ")))
menu.append("Add new person",
            lambda: t.insert_person(Person(input("Enter ID code: "), input("Enter name: "), input("Enter city: "))))
menu.append("Add fine to existing person",
            lambda: t.add_fine_to_person(input("Enter person's ID code: "), input("Enter fine type: "),
                                         float(input("Enter fine amount: "))))
menu.start()
