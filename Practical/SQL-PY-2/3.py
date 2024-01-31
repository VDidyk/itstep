from sqlalchemy import create_engine, inspect, MetaData, Table, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import json
from sqlalchemy import text

with open('config.json') as f:
    config = json.load(f)

user = config['database']['user']
password = config['database']['password']

db_url = f"postgresql+psycopg2://{user}:{password}@localhost:5432/tailer"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

inspector = inspect(engine)
metadata = MetaData()
metadata.reflect(bind=engine)


def display_tables():
    tables = inspector.get_table_names()
    for table in tables:
        print(f"Table: {table}")


def display_columns(table_name):
    columns = inspector.get_columns(table_name)
    for column in columns:
        print(f"Column: {column['name']}")


def display_columns_with_types(table_name):
    columns = inspector.get_columns(table_name)
    for column in columns:
        print(f"Column: {column['name']}, Type: {column['type']}")


def create_table(table_name, columns):
    try:
        table = Table(table_name, metadata, *columns, extend_existing=True)
        table.create(engine)
    except Exception:
        print("error")


def delete_table(table_name):
    try:
        table = Table(table_name, metadata)
        table.drop(engine)
    except Exception as e:
        print(f"Error deleting table {table_name}: {e}")


# create_table('test', [Column('id', Integer, primary_key=True), Column('name', String)])
# delete_table('test')
# create_table('doctors', [Column('id', Integer, primary_key=True), Column('name', String)])

def add_column(table_name, column_name):
    if table_name in metadata.tables:
        existing_table = metadata.tables[table_name]

        while True:
            column_type = 'Integer'

            new_column = Column(column_name, eval(column_type))

            new_table = Table(
                table_name,
                metadata,
                Column('id', Integer, primary_key=True),
                *existing_table,
                new_column,
                extend_existing=True
            )

            existing_table.drop(bind=engine, checkfirst=True)

            new_table.create(bind=engine, checkfirst=True)

    else:
        print(f"Таблиці {table_name} не існує.")


def update_column(table_name, column_name, new_column_type):
    if table_name in metadata.tables:
        existing_table = metadata.tables[table_name]

        while True:
            if column_name in existing_table.c:
                existing_column = existing_table.c[column_name]
                existing_table.drop_column(existing_column)
                new_column = Column(column_name, new_column_type)
                existing_table.append_column(new_column)
                alter_column_sql = f"ALTER TABLE {table_name} ALTER COLUMN {column_name} TYPE {new_column_type}"

                with engine.connect() as connection:
                    connection.execute(text(alter_column_sql))

                print(f"Тип стовпця {column_name} у таблиці {table_name} успішно змінено на {new_column_type}.")
                break
            else:
                print(f"Стовпця {column_name} у таблиці {table_name} не існує.")
                break
    else:
        print(f"Таблиці {table_name} не існує.")


def delete_column(table_name, column_name):
    if table_name in metadata.tables:
        existing_table = metadata.tables[table_name]

        while True:
            if column_name in existing_table.c:
                existing_column = existing_table.c[column_name]

                existing_table.drop_column(existing_column)
                delete_column_sql = f"ALTER TABLE {table_name} DROP COLUMN {column_name}"
                with engine.connect() as connection:
                    connection.execute(text(delete_column_sql))

                print(f"Стовпець {column_name} успішно видалено з таблиці {table_name}.")
                break
            else:
                print(f"Стовпця {column_name} у таблиці {table_name} не існує.")
                break
    else:
        print(f"Таблиці {table_name} не існує.")

display_tables()
# display_columns('doctors')
# display_columns_with_types('doctors')
add_column('doctors', 'test')
# update_column('doctors', 'new_column', Integer)
# delete_column('doctors', 'new_column')
session.commit()
session.close()
