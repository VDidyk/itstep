from connection import Base, engine, Session
from models import Group, Department, Teacher, GroupTeacher, Faculty

Base.metadata.create_all(engine)
session = Session()


def insert_row(model_class, data):
    new_row = model_class(**data)
    session.add(new_row)
    session.commit()
    return new_row


def update_row(model_class, filter_criteria, data_to_update):
    rows_to_update = session.query(model_class).filter_by(**filter_criteria).all()
    for row in rows_to_update:
        for key, value in data_to_update.items():
            setattr(row, key, value)
    session.commit()


def delete_row(model_class, filter_criteria):
    rows_to_delete = session.query(model_class).filter_by(**filter_criteria).all()
    for row in rows_to_delete:
        session.delete(row)
    session.commit()


# Вивести інформацію про всі навчальні групи
groups = session.query(Group).all()
for group in groups:
    print(group.__dict__)

# Вивести інформацію про всіх викладачів
teachers = session.query(Teacher).all()
for teacher in teachers:
    print(teacher.__dict__)

# Вивести назви усіх кафедр
departments = session.query(Department.Name).all()
for department in departments:
    print(department[0])

# Вивести імена та прізвища викладачів, які читають лекції в конкретній групі
group_name = 'MP-15'
query = session.query(Teacher.Name, Teacher.Surname).join(
    GroupTeacher, GroupTeacher.TeacherId == Teacher.Id).join(
    Group, GroupTeacher.GroupId == Group.Id).filter(
    Group.Name == group_name)

for result in query:
    print(result[0], result[1])

# Вивести назви кафедр і груп, які до них відносяться
query = session.query(Department.Name, Group.Name).join(
    Faculty, Faculty.DepartmentId == Department.Id).join(
    Group, Group.FacultyId == Faculty.Id)

for result in query:
    print(result[0], result[1])

# Відобразити кафедру з максимальною кількістю груп
max_groups_department = session.query(Department).order_by(Department.Id.desc()).first()
print(max_groups_department.Name)

# Відобразити кафедру з мінімальною кількістю груп
min_groups_department = session.query(Department).order_by(Department.Id.asc()).first()
print(min_groups_department.Name)

for result in query:
    print(result.Name)

Base.metadata.create_all(engine)
