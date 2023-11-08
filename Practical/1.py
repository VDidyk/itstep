# Створіть клас "Користувач" з атрибутами "ім'я", "вік" та
# "email". Застосуйте інкапсуляцію, щоб забезпечити, що ці
# дані можна отримати лише через методи класу.

from dataclasses import dataclass


@dataclass
class User:
    __name: str = None
    __age: int = None
    __email: str = None

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_email(self):
        return self.__email


user = User('Ivo Bobul', 92, 'lev@gmail.com')

print(user.get_name())
print(user.get_age())
print(user.get_email())
