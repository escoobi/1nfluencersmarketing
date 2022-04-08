import pymongo
from models.users import Users
import models.driver_mongodb


def select_user(email: str) -> dict:
    try:

        users_select = models.driver_mongodb.Connect.db.users

        users_dict = users_select.find_one({"email": email})

        return {"name": users_dict["name"], "email": users_dict["email"], "password": users_dict["password"]}

    except:
        pass


def select_user_auth(email: str, password: str) -> dict:
    try:

        users_select = models.driver_mongodb.Connect.db.users

        users_dict = users_select.find_one({"email": email, "password": password})

        return {"name": users_dict["name"], "email": users_dict["email"], "password": users_dict["password"]}

    except:
        pass
