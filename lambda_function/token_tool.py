import os
from datetime import datetime, timedelta
from typing import Union, Any
from urllib import response
import jwt


ACCESS_TOKEN_EXPIRE_MINUTES = 30 
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY'] 
JWT_REFRESH_SECRET_KEY = os.environ['JWT_REFRESH_SECRET_KEY']



def create_access_token(token, expires_delta: timedelta | None = None):
    encoded_jwt = jwt.encode({"token": token,"exp":datetime.now()}, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



def check_access_token(token):
        try:
            jwt.decode("JWT_STRING", "secret", algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            response = 'New Token Need!!'
            return response