from jose import jwt
from app.users.model import UserModel
from app.config import get_settings
from datetime import datetime as dt
import datetime


settings = get_settings()

def get_jwt_token(raw_data: dict):
    secret_key = settings.secret_key
    algo = "HS256"
    raw_data['exp'] = dt.utcnow() + datetime.timedelta(days= 30)
    jwt_encode = jwt.encode(raw_data, secret_key, algorithm=algo)
    return jwt_encode

