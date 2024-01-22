# Створіть однотабличну базу даних People (ім’я, прізвище, місто, країна, дата народження) з однойменною
# таблицею. Напишіть програму, яка дозволяє користувачеві ввести запит і отримати результати роботи запиту.
# Підтримуйте лише SELECT як запит. Якщо ви спробуєте
# виконати інші запити, потрібно буде генерувати помилку

import json
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.sql import text

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

person1 = Person(first_name='John', last_name='Doe', city='New York', country='USA', birth_date='1990-01-15')
person2 = Person(first_name='Jane', last_name='Smith', city='London', country='UK', birth_date='1985-03-22')

session.add_all([person1, person2])
session.commit()

while True:
    person_query = input("Enter your query or 'exit':")

    if person_query.lower() == 'exit':
        break

    try:
        result = session.execute(text(person_query))
        rows = result.fetchall()

        if rows:
            [print(row) for row in rows]
        else:
            print("No result")

    except Exception as e:
        print(f'Error {e}')

session.close()
