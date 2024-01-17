from pydantic import BaseModel, EmailStr, SecretStr, validator, root_validator
from datetime import datetime
from uuid import UUID
import uuid
from typing import Optional, Any
from app.users.validators import _validate_email
from app.users.utilis import uuid1_time_to_datetime
from app.users.security import generate_hash
from beanie import Document as Docs
from beanie import Indexed

class Profit_Loss_Model(BaseModel):
    profit: Optional[int]
    loss: Optional[int]
    created: Optional[Any]

    @root_validator
    def timestamp(cls, values):
        time = uuid.uuid1().time
        values['created'] = uuid1_time_to_datetime(time)




class UserSignUpSchema(BaseModel):
    uuid: UUID = uuid.uuid1()
    username: Indexed(str)
    fullname:str
    email: EmailStr
    role: str = 'staff'
    password: str
    deposit: Optional[int]
    created_at: Optional[Any] = None

    @validator('email')
    def validate_email(cls, v, values, **kwargs):
        email = v
        is_valid, msg, validated_email = _validate_email(email)
        if not is_valid:
            raise ValueError(msg)
        return email
    

    
    @root_validator(pre = True)
    def timestamp(cls, values):
        time = uuid.uuid1().time
        values['created_at'] = uuid1_time_to_datetime(time)
        return values
    
    @root_validator(pre = True)
    def hash_password(cls, values):
        password = values.get('password')
        values['password'] = generate_hash(password)
        return values
    
    @root_validator(pre =True)
    def deposited_amount(cls, values):
        if (role := values.get('role')) != 'admin':
            values['deposit'] = 100
        return values
    

        
class LoginSchema(BaseModel):
    email: EmailStr
    password: str

    # @root_validator
    # def hash_login_password(cls, values):
    #     password = values['password']
    #     hash_password = generate_hash(password)
    #     values['password'] = hash_password
    #     return values
    
