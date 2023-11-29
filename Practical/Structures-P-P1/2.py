# Користувач вводить з клавіатури набір рядків. Збережіть отримані рядки до двозв’язного списку. Після чого
# покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# Практичне завдання
# 1
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача,
# після чого меню з’являється знову.

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

    def print(self):
        def print_callback(node):
            print(node)

            return True

        self.each(print_callback)


my_lst = LinkedList()
nums = input("Enter numbers separated by space: ").split()
for num in nums:
    my_lst.append(int(num))
print(my_lst.print())

my_lst.remove(2)
print(my_lst.print())

print(my_lst.check(3))
my_lst.replace(5, 15)
print(my_lst.print())
