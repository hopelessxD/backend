from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,Session

from pydantic import BaseModel
from typing import Optional,List

app = FastAPI()


#database setup
engine = create_engine("sqlite:///users.db", connect_args ={"check_same_thread":False})
SessionLocal = sessionmaker(autcommit=False,autoflush = False, bind = engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    
    
    id = Column(Integer, primary_key = True)
    name = Column(String(100), nullable = False)
    email = Column(String(100), nullable=False,unique = True)
    role = Column(String(100), nullable = False)








@app.get('/')
def root():
    return{"message": "test"}


