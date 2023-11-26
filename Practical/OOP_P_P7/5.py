# Створіть клас Multiplier, який при ініціалізації
# отримує множник. Забезпечте можливість викликати
# цей об'єкт з аргументом та повертати множене
# значення.

class Multiplier:
    def __init__(self, number):
        self.__number = number

    def __call__(self, *args, **kwargs):
        return self.__number * args[0]


m = Multiplier(15)
print(m(2))
