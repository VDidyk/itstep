# Для бази даних «Лікарня», яку ви розробляли в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії з
# базою даних, який дозволяє:
# ■ Вставляти рядки в таблиці бази даних.
# ■ Оновлення рядків у таблицях бази даних. При спробі
# оновлення усіх рядків в одній таблиці надайте запит на
# підтвердження користувачеві. Оновлювати усі рядки
# можна лише після підтвердження користувачем.
# ■ Видалення рядків з таблиць баз даних. При спробі видалити
# усі рядки в одній таблиці потрібно видавати користувачу
# запит на підтвердження. Видаляти усі рядки, можна тільки
# після підтвердження користувачем.

from connection import Base, engine, Session
from models import Doctor

Base.metadata.create_all(engine)
session = Session()


def insert_doctor(name, surname, phone, salary):
    new_doctor = Doctor(name=name, surname=surname, phone=phone, salary=salary)
    session.add(new_doctor)
    session.commit()


def update_doctor(doctor_id, name=None, surname=None, phone=None, salary=None):
    doctor = session.query(Doctor).filter(Doctor.id == doctor_id).one()
    if name:
        doctor.name = name
    if surname:
        doctor.surname = surname
    if phone:
        doctor.phone = phone
    if salary:
        doctor.salary = salary
    session.commit()


def update_all_doctors(name=None, surname=None, phone=None, salary=None):
    if input("Are you sure you want to update all records? (yes/no): ").lower() == 'yes':
        doctors = session.query(Doctor).all()
        for doctor in doctors:
            if name:
                doctor.name = name
            if surname:
                doctor.surname = surname
            if phone:
                doctor.phone = phone
            if salary:
                doctor.salary = salary
        session.commit()


def delete_doctor(doctor_id):
    doctor = session.query(Doctor).filter(Doctor.id == doctor_id).one()
    session.delete(doctor)
    session.commit()


def delete_all_doctors():
    if input("Are you sure you want to delete all records? (yes/no): ").lower() == 'yes':
        session.query(Doctor).delete()
        session.commit()


Base.metadata.create_all(engine)
