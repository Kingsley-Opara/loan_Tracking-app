from pymongo.mongo_client import MongoClient
from motor import motor_asyncio
from app.config import get_settings
from beanie import init_beanie
from app.users.model import UserModel
from app.users.schema import Profit_Loss_Model

settings = get_settings()

url = settings.mongo_url
client = motor_asyncio.AsyncIOMotorClient(url)


def auth_user_model(data: dict):
    user = {
        "uuid":data['uuid'],
        'username': data['username'],
        "fullname": data['fullname'],
        'email': data['email'],
        'role': data['role'],
        "password": data['password'],
        "deposit": data['deposit'],
        'created_at': data['created_at']

    }
    return user

async def create_collection():
    await init_beanie(database=client.user_db, document_models=[UserModel])