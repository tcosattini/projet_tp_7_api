from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import timedelta
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# A changer pour la production et à mettre dans un .ENV
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)


