# from bson.objectid import ObjectId
# from .db import auth_user_model


# async def list_all_users():
#     users = []
#     async for user in users_collection.find():
#         users.append(user)
#     return users

# # async def create_users():
# #     user = await 

# async def add_user(user_info: dict):
#     user = await users_collection.insert_one(user_info)
#     new_student = await users_collection.find_one({'-id': user.inserted_id})
#     return auth_user_model(new_student)

