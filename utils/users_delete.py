import pymongo
from models.users import Users
import models.driver_mongodb

def delete_users(Users):

    users_delete = models.driver_mongodb.Connect.db.users

    users_id = users_delete.delete_one(Users.__dict__())

Users = Users = Users("gustavo.o.c@icloud.com", "Gustavo Oliveira Cardozo", "12")
delete_users(Users)