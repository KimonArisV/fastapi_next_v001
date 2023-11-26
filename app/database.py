from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time 
from .config import settings

#SQLALCHEMY_DATABASE_URL ='postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@\
{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

#this is the connection of sqlalchemy to our postgres database 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



#for runnign raw sql sequence and connecting with postgres instead of using sqlalchemy
"""
while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi_tutorial_db',user='postgres',password='kimon24',
                                cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("databse connection was sucessfull")
        break
    except Exception as error:
        print("connection to databse failed")
        print(f"the error was {error}")
"""