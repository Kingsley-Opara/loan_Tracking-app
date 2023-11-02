from fastapi import FastAPI, Body, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
# from .crud import add_user, list_all_users
from typing import List
from fastapi.encoders import jsonable_encoder
from app.users.model import UserModel, ProfitAndLossModel
from app.users.schema import UserSignUpSchema, Profit_Loss_Model, LoginSchema
from app.db import create_collection, auth_user_model
from bunnet.exceptions import DocumentWasNotSaved
from app.users.security import verify_hash
from app.users.jwt import get_jwt_token
from fastapi_jwt_auth import AuthJWT
from datetime import datetime as dt
import datetime


app = FastAPI()

origins = [
    "http://localhost:3000",
    '*',

]



app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

@app.on_event('startup')
async def on_startup():
    await create_collection()
    print('good')
    


@app.get('/')
def home():
    # init_bunnet(database=client2.user_db, document_models=[UserModel, Profit_Loss_Model])
    return {'this': "is good"}



@app.post('/api/user/create/')
async def create_user(data: UserSignUpSchema = Body(...)):
    # init_bunnet(database=client2.user_db, document_models=[UserModel,  Profit_Loss_Model])    
    
    # profit_margin = Profit_Loss_Model(profit = randomly_generate_profit())
    json = jsonable_encoder(data.dict())
    user = UserModel(**json)
    # insert_user = await user.insert()
    try:
        insert_user = await user.insert()
        
        return {'data': 'valid request'}
    except:
        return HTTPException(status_code=400, detail=f'An account has already been created using this {data.email}')
    # return {'bad': 'data'}


@app.get('/api/list/')
async def list_api_view():
    results = UserModel.find()
    data = await results.to_list()
    
    
    return {'data': data}
    
    
@app.post('/api/user/login')
async def login_view(response: Response, login: LoginSchema = Body(...)):
    user = UserModel.find_one(UserModel.email == login.email)
    if await user.exists():
        user_instance = await user._find_one()
        password = user_instance['password']
        verifield, msg = verify_hash(pw_hash= password, pw_raw= login.password)
        if not verifield:
            return HTTPException(status_code= 400, detail= f'{msg}')
        raw_data = {
            'uuid': str(user_instance['uuid']),
            'username': user_instance['username'],
            'fullname': user_instance['fullname'],
            'created_at': user_instance['created_at'],
            'role': user_instance['role']

        }
        token = get_jwt_token(raw_data= raw_data)
        response.set_cookie('jwt_token', token, 
                            datetime.timedelta(days= 30), 
                            datetime.timedelta(days= 30),
                            '/login/', None, False, True, 'lax')
        return {'token': token}
    

    return HTTPException(status_code=400, detail='Invalid credentail....consider creating an account')
    

    
# @app.post('/api/user/login/test')
# async def login_view(login: LoginSchema = Body(...)):
#     user = UserModel.find_one(UserModel.email == login.email)
#     if user.exists():
#         user_instance = await user._find_one()
#         password = user_instance['password']
#         verifield, msg = verify_hash(pw_hash= password, pw_raw= login.password)
#         if not verifield:
#             return HTTPException(status_code= 400, detail= f'{msg}')
#         raw_data = {
#             'uuid': str(user_instance['uuid']),
#             'username': user_instance['username'],
#             'fullname': user_instance['fullname'],
#             'created_at': user_instance['created_at'],
#             'role': user_instance['role']

#         }
#         token = get_jwt_token(raw_data= raw_data)
#         return {'token': token} 

#     return HTTPException(status_code=400, detail='Invalid credentail....consider creating an account')
    





