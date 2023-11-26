from click import STRING
from pydantic import BaseModel, EmailStr
from datetime import datetime 
from typing import Optional

#Schema coming from our pydantic
class PostBase(BaseModel):
    title: str
    content: str
    published: bool =True
    #rating: Optional[int] =None

class PostCreate(PostBase):
    pass 

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime
    class Config:
        from_attributes=True

class Post(PostBase):
    id: int
    created_at: datetime
    owner_id : int
    owner: UserOut
    #not sure if it is needed
    class Config:
        #orm_mode = True #not used any more , it is from old versions
        from_attributes=True

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int]=None