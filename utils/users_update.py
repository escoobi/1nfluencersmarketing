import pymongo

from models.users import Users

import models.driver_mongodb

"""

Function to update user in mongoDB is passed as a parameter to the Users class

"""
def update_users(users_, Users): # Recebe um dict original e um dict para poder ser alterado
    users_update = models.driver_mongodb.Connect.db.users
    dic_set = {'$set': Users.__dict__()}
    users_id = users_update.update_one({"password": users_["password"]}, dic_set)
