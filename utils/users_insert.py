import pymongo
from models.users import Users
from utils.users_select import select_user
import models.driver_mongodb
from utils.users_update import update_users

"""

Function to insert user in mongoDB is passed as a parameter to the Users class
Perform the query before inserting

"""


def insert_user(Users):
    try:
        users_insert = models.driver_mongodb.Connect.db.users

        user = select_user(Users.email)

        if user == None:
            users_id = users_insert.insert_one(Users.__dict__()).inserted_id
            users_id
            return f"Usuário cadastrado com sucesso!"
        else:
            update_users(user, Users)
            return f"Usuário alterado com sucesso!"
    except:
        return f"Error!"
