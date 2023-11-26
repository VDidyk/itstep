# Створіть клас для представлення користувача з
# атрибутами: ім'я та вік. Додайте властивості для
# валідації віку користувача. Наприклад, вік повинен
# бути у межах від 0 до 120.

class User:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 0 or age > 120:
            raise ValueError

        self.__age = age


u = User("Tailer", 27)
u.age = 150
print(u.age)
