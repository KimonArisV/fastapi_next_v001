from passlib.context import CryptContext

#what algo to use for hashing 
pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash_it(password:str):
    return pwd_context.hash(password)

def verify(password, hashed_pass):
    return pwd_context.verify(password,hashed_pass)
