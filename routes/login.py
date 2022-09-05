import fastapi
from fastapi import Response, HTTPException
from pydantic import BaseModel, EmailStr
from boto3.dynamodb.conditions import Key
import boto3
import bcrypt
from token_tool import create_access_token

# Dynamodb
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

router = fastapi.APIRouter()


#user model
class UserIn(BaseModel):
    password: str
    email: EmailStr


@router.post('/login')
def index(input:UserIn,response: Response):

# Dynamodb

#     response = table.query(
#     KeyConditionExpression=Key('email').eq(input.email)
# )
#     items = response['Items']

# Will have to add logic for dynamodb here
# password will be the user input
    password = input.password
  
# hashed will be the return from db
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
# check users password

    if bcrypt.checkpw(password, hashed):
        print("It Matches!")
        new_token = create_access_token(input.email)
        response = HTTPException(status_code=200, detail="This is a token", headers=new_token)
        return response
    if not bcrypt.checkpw(password, hashed):
        print("It Does not Match :")
        response = HTTPException(status_code=404, detail="No user found with those credentials")
        return response

    




