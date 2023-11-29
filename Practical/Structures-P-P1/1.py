# Користувач вводить з клавіатури набір чисел. Збережіть отримані числа до однозв’язного списку. Після
# чого покажіть меню, в якому запропонуєте користувачеві
# набір пунктів:
# 1. Додати елемент до списку.
# 2. Видалити елемент зі списку.
# 3. Показати вміст списку.
# 4. Перевірити, чи є значення у списку.
# 5. Замінити значення у списку.
# Дія виконується залежно від вибору користувача, після чого меню з’являється знову


# Синтаксис Однозв'язковий список
class Node:
    def __init__(self, data):
        self.data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node: super):
        self.__next = node

    def __str__(self):
        return f"[{self.data}] -> {self.__next}"


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

    def each(self, callback):
        head = self.head
        prev_node = None

        while True:
            if not head:
                break

            node = callback(head)

            if node is None and prev_node is not None:
                prev_node.next = head.next
            elif node is None:
                prev_node = None
                self.head = head.next
            else:
                prev_node = head

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

    def __str__(self):
        return f"{self.head}"


my_lst = LinkedList()
nums = input("Enter numbers separated by space: ").split()
for num in nums:
    my_lst.append(int(num))
print(my_lst)

my_lst.remove(2)
print(my_lst)

print(my_lst.check(3))
my_lst.replace(5, 15)
print(my_lst)
