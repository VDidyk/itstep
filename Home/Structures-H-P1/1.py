# Користувач вводить з клавіатури набір чисел. Отримані
# числа необхідно зберегти до списку (тип списку оберіть в залежності від поставленого нижче завдання). Після чого покажіть меню, в якому запропонуєте користувачеві набір пунктів:
# 1. Додати нове число до списку (якщо таке число існує у
# списку, потрібно вивести повідомлення про це користувачеві без додавання числа).
# 2. Видалити усі входження числа зі списку (користувач вводить з клавіатури число для видалення)
# 3. Показати вміст списку (залежно від вибору користувача,
# покажіть список з початку або з кінця)
# 4. Перевірити, чи є значення у списку
# 5. Замінити значення у списку (користувач визначає, чи
# замінити тільки перше входження, чи всі)
# Дія виконується залежно від вибору користувача, після
# чого меню з’являється знову.


class Node:
    def __init__(self, data):
        self.data = data
        self.__next = None
        self.__prev = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node: super):
        self.__next = node

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, node: super):
        self.__prev = node

    def __str__(self):
        return f"{self.prev.data if self.prev else None} -> [{self.data}] -> {self.next.data if self.next else None}"


class LinkedList:
    head: Node = None

    def append(self, value):
        if self.check(value):
            print(f"{value} is already in the list!")
        else:
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                return
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node

    def each(self, callback):
        head = self.head
        prev_node = None

        while True:
            if not head:
                break

            node = callback(head)

            if node is None and prev_node is not None:
                prev_node.next = head.next
                if head.next:
                    head.next.prev = prev_node
            elif node is None:
                prev_node = None
                if head.next:
                    head.next.prev = prev_node

                self.head = head.next
            else:
                prev_node = head
                if head.next:
                    head.next.prev = prev_node

            head = head.next

    def remove(self, value):
        def remove_callback(node):
            if node.data == value:
                del node
                return None

            return node

        self.each(remove_callback)

    def check(self, value):
        exists = False

        def check_if_exists(node):
            if node.data == value:
                nonlocal exists
                exists = True

            return True

        self.each(check_if_exists)

        return exists

    def replace(self, value, new_value):
        def replace_callback(node):
            if node.data == value:
                node.data = new_value

            return True

        self.each(replace_callback)

    def get_last_node(self):
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        return last_node

    def print(self, reverse=False):
        if not reverse:
            def print_callback(node):
                print(node)

                return True

            self.each(print_callback)
        else:
            # Я розумію що краще зберігати посилання на останній елемент, але вже немає часу це робити :)
            node = self.get_last_node()

            while node:
                print(node)
                node = node.prev


my_lst = LinkedList()

my_lst.append(1)
my_lst.append(2)
my_lst.append(2)
my_lst.append(3)
my_lst.append(4)
my_lst.append(5)
print(my_lst.print())

print("REMOVING!")

my_lst.remove(2)
print(my_lst.print())

print("REVERSE SHOWING!")
print(my_lst.print(True))

print(my_lst.check(3))
my_lst.replace(5, 15)
print(my_lst.print())
