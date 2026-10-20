from sqlalchemy import Column, Integer, String
from database import base

class User(base):
    __tablename__ = "users"
    __tableargs__ ={"schema":"trainning"}

    id = Column(Integer, primary_key=True,autoincrement= True)
    name= Column(String(100))
    email = Column(String(100))
    age = Column(Integer)

class Student(base):
    __tablename__ ="student"
    __table_age__ ={"schema": "training"}
    id = Column(Integer,primary_key= True, autoincrement= True)
    name = Column(String(50))



    