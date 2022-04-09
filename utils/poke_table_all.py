from flask import render_template, Flask

from utils.users_select import select_user_auth

from utils.poke_select import select_all_poke

from models.users import Users

"""
Method for render a template with list pokemon
"""


def poke_all(email: str, password: str):
    usr_dict: dict = select_user_auth(email, password)

    usr: Users = Users(usr_dict["email"], usr_dict["name"], usr_dict["password"])

    if usr.name is not None:
        return usr
