"""
Database.py:

Modules used:

-create_engine: allows you to create a database with a specified sql program
- object types: used to specify what tables will be
- declarative base:
"""
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create SQLite database engine
engine = create_engine("sqlite:///Bills.db")

# Allows you to create model classes within sqlalchemy
Base = declarative_base()


# Bills class represents tracking table
class Bills(Base):
    __tablename__ = 'bill_tracker'
    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Amount = Column(Integer)
    Bill_Date = Column(Date)


# Create a session to interact with database
Session = sessionmaker(bind=engine)


# Deletes existing data in the database then creates it again to stop duplicates everytime it is run.
def setup_database():
    Base.metadata.drop_all(engine)
    print('Data Deleted')
    Base.metadata.create_all(engine)
    print('Data Added')


def create_session():
    return Session()
