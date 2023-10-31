# Створіть клас Student з атрибутами name та age.
# Додайте метод print_info, який виведе інформацію про
# студента у на вигляді "Ім'я: {name}, Вік: {age}".

class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}")


student = Student('Vitalii', 27)
student.print_info()
