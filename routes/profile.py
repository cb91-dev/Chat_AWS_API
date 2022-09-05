import fastapi
import json
from fastapi.security import OAuth2PasswordBearer
from fastapi import Response, HTTPException,Depends
from token_tool import create_access_token

router = fastapi.APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.get('/profile')
def index(token):


    # convert into JSON:
    print(token)
    return 'Hello'