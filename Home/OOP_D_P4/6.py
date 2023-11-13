# Створіть клас Student, який має атрибути name, age,
# grade та courses. Реалізуйте метод класу add_course, який
# додає новий предмет до списку курсів студента

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []

    def add_course(self, new_course):
        if new_course not in self.courses:
            self.courses.append(new_course)

    def __str__(self):
        return f"{self.name} {self.courses}"


student = Student("Vitalii", 27, 11)
student.add_course("AI")
print(student)
