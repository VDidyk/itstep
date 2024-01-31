# Для бази даних «Лікарня», яку ви розробляли в рамках
# курсу «Теорія Баз Даних», створіть додаток для взаємодії
# з базою даних, який дозволяє створювати звіти:
# ▷ Вивести прізвища лікарів та їх спеціалізації;
# ▷ Вивести прізвища та зарплати (сума ставки та надбавки)
# лікарів, які не перебувають у відпустці;
# ▷ Вивести назви палат, які знаходяться у певному відділенні;
# Вивести усі пожертвування за вказаний місяць у
# вигляді: відділення, спонсор, сума пожертвування, дата
# пожертвування;
# ▷ Вивести назви відділень без повторень, які спонсоруються певною компанією.

from connection import Base, engine, Session
from models import Doctor, Specialization, DoctorSpecialization, Vacation, Ward, Sponsor, Donation, Department
from sqlalchemy import func
from datetime import date

Base.metadata.create_all(engine)
session = Session()

# Вивести прізвища лікарів та їх спеціалізаці
query = session.query(Doctor.surname, Specialization.name). \
    join(DoctorSpecialization, Doctor.id == DoctorSpecialization.doctor_id). \
    join(Specialization, Specialization.id == DoctorSpecialization.specialization_id)

for surname, specialization in query.all():
    print(f"Doctor Surname: {surname}, Specialization: {specialization}")

# Вивести прізвища та зарплати (сума ставки та надбавки) лікарів, які не перебувають у відпустці
current_date = date.today()

query = session.query(
    Doctor.surname,
    Doctor.salary.label('total_salary')
).outerjoin(Vacation, Doctor.id == Vacation.doctor_id).filter(
    Vacation.start_date <= current_date,
    Vacation.end_date >= current_date
)

for surname, total_salary in query.all():
    print(f"Doctor Surname: {surname}, Total Salary: {total_salary}")

# Вивести назви палат, які знаходяться у певному відділенні;
department_id = 1

wards_in_department = session.query(Ward.name).filter(Ward.department_id == department_id).all()

for ward_name, in wards_in_department:
    print(ward_name)

# Вивести усі пожертвування за вказаний місяць у
# вигляді: відділення, спонсор, сума пожертвування, дата
# пожертвування;
specified_month = 6  # червень
specified_year = 2022

donations_query = session.query(
    Department.name.label('department_name'),
    Sponsor.name.label('sponsor_name'),
    Donation.amount.label('donation_amount'),
    Donation.date.label('donation_date')
).join(Department, Department.id == Donation.department_id) \
    .join(Sponsor, Sponsor.id == Donation.sponsor_id) \
    .filter(
    func.extract('month', Donation.date) == specified_month,
    func.extract('year', Donation.date) == specified_year
)

for donation in donations_query.all():
    print(f"Department: {donation.department_name}, Sponsor: {donation.sponsor_name}, "
          f"Amount: {donation.donation_amount}, Date: {donation.donation_date.strftime('%Y-%m-%d')}")

# Вивести назви відділень без повторень, які спонсоруються певною компанією.

departments_query = session.query(Department.name).distinct(). \
    join(Donation, Department.id == Donation.department_id). \
    join(Sponsor, Sponsor.id == Donation.sponsor_id). \
    filter(Sponsor.name == "MS")

for department in departments_query.all():
    print(department.name)
