import pymongo
from models.users import Users
from utils.users_select import select_user
import models.driver_mongodb


def insert_user(Users):

    try:
        users_insert = models.driver_mongodb.Connect.db.users

        users_id = users_insert.insert_one(Users.__dict__()).inserted_id

        users_id
    except:
        pass

if select_user(Users.email) == None:
    insert_user(Users)
else:
    print("Cadastro já realizado!")


