from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import json

with open('config.json') as f:
    config = json.load(f)

user = config['database']['user']
password = config['database']['password']

db_url = f"postgresql+psycopg2://{user}:{password}@localhost:5432/sales"

engine = create_engine(db_url)

Base = declarative_base()

Session = sessionmaker(bind=engine)