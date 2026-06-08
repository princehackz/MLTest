from jose import jwt
from passlib.context import CryptContext
SECRET="finance_secret"
pwd=CryptContext(schemes=["bcrypt"])
def hash_password(p): return pwd.hash(p)
def verify_password(p,h): return pwd.verify(p,h)
def create_token(d): return jwt.encode(d,SECRET,algorithm="HS256")
