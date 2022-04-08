import pymongo
from models.poke_abilites import PokeAbiliteis
import models.driver_mongodb

"""
Method for update pokemon in mongoDb
takes as a parameter the Poke class for update in mongoDb
"""
def update_Poke(Poke):
    poke_update = models.driver_mongodb.Connect.db.pokemon

    dic_set = {'$set': Poke.__dict__()}
    poke_id = poke_update.update_one(Poke.__dict__(), dic_set)