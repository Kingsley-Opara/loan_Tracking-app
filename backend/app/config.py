from pydantic import BaseSettings, Field
from functools import lru_cache
from app.users.model import UserModel, ProfitAndLossModel
from fastapi_jwt_auth import AuthJWT


class Settings(BaseSettings):
    secret_key: str = Field(..., env = 'SECRET_KEY')
    mongo_url: str = Field(..., env= 'DB_URL')
    redis_url:str = Field(..., env = 'REDIS_URL')
    # authjwt_secret_key: str = Field(..., env = 'AUTHJWT_SECRET_KEY')
    # ACCESS_TOKEN_EXPIRES_IN: int = 30
    # REFRESH_TOKEN_EXPIRES_IN: int = 90
    # JWT_ALGORITHM: str = 'HS256'
    # CLIENT_ORIGIN: str

    class Config:
        env_file = '.env'


@lru_cache()
def get_settings():
    return Settings()


# settings = get_settings()
# class AuthTokenSettings(BaseSettings):
#     authjwt_secret_key: str = settings.authjwt_secret_key
#     authjwt_alogrithm: str = settings.JWT_ALGORITHM
#     auth_token_location: set = {'cookies', 'headers'}
#     authjwt_access_cookie_key: str = 'access_token'
#     authjwt_refresh_cookie_key: str = 'refresh_token'
#     authjwt_cookie_csrf_protect: bool = False


#     class Config:
#         env_file = '.env'


# @AuthJWT.load_config
# def get_auth_token_settings():
#     return AuthTokenSettings()
