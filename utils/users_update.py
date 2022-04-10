import pymongo

from models.users import Users

import models.driver_mongodb

"""

Function to update user in mongoDB is passed as a parameter to the Users class

"""
def update_users(Users):
    users_update = models.driver_mongodb.Connect.db.users

    dic_set = {'$set': Users.__dict__()}
    users_id = users_update.update_one(Users.__dict__(), dic_set)


Users = Users("gustavo.o.c@icloud.com", "Gustavo Oliveira Cardozo", "89")
update_users(Users)