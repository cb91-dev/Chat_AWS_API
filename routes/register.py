import fastapi
from pydantic import BaseModel, EmailStr
from boto3.dynamodb.conditions import Key, Attr
import boto3
from fastapi import Response,status, HTTPException
from token_tool import create_access_token
import bcrypt

# Dynamodb
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('users')

router = fastapi.APIRouter()

# new user class
class NewUser(BaseModel):
    email: EmailStr
    password: str
    user_name:str


@router.post('/register')
def index(input:NewUser,response: Response):

 # will have to add logic for dynamodb here

    # response = table.query(
    # KeyConditionExpression=Key(input.email)
    # )
    # items = response['Items']
  # will have to add logic for dynamodb here
    items = 'test@test.com'
    if items == items:
        if items != input.email:
            response = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                        detail=f'This email is already in use')
            return response
        else:
            token = create_new_user(input)
            response = HTTPException(status_code=status.HTTP_201_CREATED,
                        detail=f'User created',
                        headers=token)
            return response
    return HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                        detail=f'No user input')





# creating new user
def create_new_user(new_user_data):

    password = new_user_data.password
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())

    # Dynamodb
    # table.put_item(
    #     Item={
    #     'email': new_user_data.email,
    #     'password': hashed,
    #     'user_name': new_user_data.user_name
    #     }
    # )
    response = create_access_token(new_user_data.email)

    return response
