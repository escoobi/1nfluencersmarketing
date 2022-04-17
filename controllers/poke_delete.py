import pymongo

from models.poke_abilites import PokeAbiliteis

import models.driver_mongodb

"""
Method for delete pokemon in mongoDb

takes as a parameter the Poke models
"""
def delete_poke(Poke):

    poke_delete = models.driver_mongodb.Connect.db.pokemon

    poke_id = poke_delete.delete_one(Poke.__dict__())

    poke_id