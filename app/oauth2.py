from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "ghfgh5fghfg65jf65f65jf65jfgfg5h5grteg6hg6f5n655fhf6g5h"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_TIME = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes = ACCESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp":expire})

    encoded_jwt= jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

    return encoded_jwt