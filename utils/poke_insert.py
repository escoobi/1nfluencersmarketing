import models.driver_mongodb
from models.poke import Poke

from models.poke_abilites import PokeAbiliteis

import pymongo

from utils.poke_select import select_poke


def insert_poke(Poke):
    try:

        if select_poke(Poke.name) == None:
            poke_insert = models.driver_mongodb.Connect.db.pokemon
            poke_id = poke_insert.insert_one(Poke.__dict__()).inserted_id
            poke_id

        else:
            print("Cadastro já realizado!")
    except:
        pass
