# Модифікуйте перше завдання так, щоб користувач не
# міг вводити запит, а користувався готовими фільтрами.
# Наприклад: відображення усіх людей, відображення усіх
# людей з одного міста (користувач задає з клавіатури як значення), відображення усіх людей з однієї країни (користувач задає з
# клавіатури як параметр).

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


def show_rows(result):
    rows = result.fetchall()

    if rows:
        [print(row) for row in rows]
    else:
        print("No result")


def filter_by_city(city):
    if not city:
        return

    show_rows(session.execute(text(f"Select * from people where city='{city}'")))


def filter_by_country(country):
    if not country:
        return

    show_rows(session.execute(text(f"Select * from people where country='{country}'")))


menu = Menu()

menu.append("Filter by city", lambda: filter_by_city(input("Enter the city: ")))
menu.append("Filter by country", lambda: filter_by_country(input("Enter the country: ")))

menu.start()

session.close()
