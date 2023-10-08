from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'admin',
    'database': 'python_api',
    'port': '3308'
}
SQLALCHEMY_DATABASE_URL = f'mysql+mysqlconnector://{config["user"]}:{config["password"]}@{config["host"]}:{config["port"]}/{config["database"]}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(autocommit = False, autoflush = False, bind= engine)

Base = declarative_base()
session = Session()