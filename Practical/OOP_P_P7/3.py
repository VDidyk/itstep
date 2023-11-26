# Створіть клас для представлення відомостей про
# замовлення. Забезпечте, щоб номер замовлення був
# тільки для читання за допомогою керованих атрибутів,
# але його можна було переглядати.
import random


class Order:
    def __init__(self, total):
        self.__number = random.randint(10000, 100000);
        self.total = total

    @property
    def number(self):
        return self.__number


o = Order(100)
print(o.number)
