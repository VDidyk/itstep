# Додайте до додатку можливість зберігати результати
# роботи фільтрів у файл. Наприклад, результат роботи
# фільтра для відображення усіх людей або результат роботи
# фільтра з відображення людей з одного міста.

import json
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import text
import sys

sys.path.append('../../Libraries')
from Menu import Menu

with open('config.json') as f:
    config = json.load(f)

user = config['database']['user']
password = config['database']['password']

db_url = f"postgresql+psycopg2://{user}:{password}@localhost:5432/people"
engine = create_engine(db_url)

base = declarative_base()


class Person(base):
    __tablename__ = 'people'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    city = Column(String(50))
    country = Column(String(50))
    birth_date = Column(Date())


base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# person1 = Person(first_name='Dean', last_name='Ambrose', city='New York', country='USA', birth_date='1995-01-15')
# person2 = Person(first_name='Jane', last_name='Smith', city='Washington', country='USA', birth_date='1984-03-22')
#
# session.add_all([person1, person2])
session.commit()


def write_to_file(data):
    file_name = "logs.txt"

    with open(file_name, 'a') as file:
        file.write(str(data) + '\n')


def show_rows(result):
    rows = result.fetchall()

    if rows:
        for row in rows:
            write_to_file(row)
            print(row)

    else:
        print("No result")


def filter_by_city(city):
    if not city:
        return

    show_rows(session.execute(text(f"Select * from people where lower(city)='{city.lower()}'")))


def filter_by_country(country):
    if not country:
        return

    show_rows(session.execute(text(f"Select * from people where lower(country)='{country.lower()}'")))


def filter_by_city_and_country(city, country):
    if not country or not city:
        return

    show_rows(session.execute(
        text(f"Select * from people where lower(country)='{country.lower()}' and lower(city)='{city.lower()}'")))


def filter_by_city_or_country(city, country):
    if not country or not city:
        return

    show_rows(session.execute(
        text(f"Select * from people where lower(country)='{country.lower()}' or lower(city)='{city.lower()}'")))


def add_person():
    person = Person(
        first_name=input("Enter the name: "),
        last_name=input("Enter the last name: "),
        city=input("Enter the city: "),
        country=input("Enter the country: "),
        birth_date=input("Enter the birth date: ")
    )

    session.add(person)
    session.commit()


def delete_person():
    rows = session.execute(text(f"Select * from people order by id")).fetchall()
    people = []

    if rows:
        count = 1
        for row in rows:
            print(f"{count}. {row}")
            count += 1
            people.append(row)

        number = int(input("Select person: ")) - 1

        session.execute(
            text(f"delete from people where id={people[number][0]}"))

    else:
        print("No result")


def change_field():
    rows = session.execute(text(f"Select * from people order by id")).fetchall()
    people = []

    if rows:
        count = 1
        for row in rows:
            print(f"{count}. {row}")
            count += 1
            people.append(row)

        number = int(input("Select person: ")) - 1

        if number < 0 or number > len(people) - 1:
            return

        columns = [column.name for column in Person.__table__.columns]

        print("Choose column to change:")
        count = 0
        for c in columns:
            print(f"{c} - {people[number][count]}")
            count += 1

        column = input("Enter the column name: ")

        if column not in columns:
            return

        session.execute(
            text(f"Update people set {column}='{input('Enter a new value: ')}' where id={people[number][0]}"))

    else:
        print("No result")


menu = Menu()

menu.append("Filter by city", lambda: filter_by_city(input("Enter the city: ")))
menu.append("Filter by country", lambda: filter_by_country(input("Enter the country: ")))
menu.append("Filter by city and country",
            lambda: filter_by_city_and_country(input("Enter the city: "), input("Enter the country: ")))
menu.append("Filter by city or country",
            lambda: filter_by_city_or_country(input("Enter the city: "), input("Enter the country: ")))
menu.append("Add person",
            lambda: add_person())
menu.append("Change person",
            lambda: change_field())
menu.append("Delete person",
            lambda: delete_person())

menu.start()

session.close()
