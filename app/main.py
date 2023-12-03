
#from typing import Optional, List
#from typing_extensions import deprecated
#from fastapi import FastAPI , Response, status, HTTPException, Depends
#from fastapi.params import Body
#from pydantic import BaseModel
#from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
#from sqlalchemy.orm import Session
#import models, utils
#from .schemas import PostCreate, Post, UserCreate, UserOut
#import time 

from fastapi import FastAPI, middleware 
from fastapi.middleware.cors import CORSMiddleware
from . import models #,utils
from .database import  engine #, get_db
from .routers import post, user, auth 
from .config import settings 

#after alembic migration we do not need this any more
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# "https://www.google.com"
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)

#path(route) opperation 
#path we have to go in the url
#send get request to our API #the path after the domain name of our API
@app.get("/")  
async def root():
    return {"message": "welcome kimon  "}



