from pydantic import BaseModel, EmailStr, SecretStr, validator, root_validator
from typing import Optional, Any
from bunnet import Document
from beanie import Document as Docs, Indexed
from uuid import UUID
import uuid
from datetime import datetime
from app.users.schema import UserSignUpSchema, Profit_Loss_Model
from fastapi.encoders import jsonable_encoder

class ProfitAndLossModel(Docs):
    User: list
    profit: Optional[Profit_Loss_Model]

class UserModel(Docs):
    uuid: UUID = uuid.uuid1()
    username: Indexed(str)
    fullname:str
    email: Indexed(EmailStr, unique = True)
    role: str = 'staff'
    password: str
    deposit: Optional[int]
    created_at: Optional[Any] = None

    





        
        
    


