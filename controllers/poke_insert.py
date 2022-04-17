import models.driver_mongodb

from controllers.poke_select import select_poke

"""
Method for insert pokemon in mongoDb

takes as a parameter the Poke models

perform the query to check if you already have the registration
"""

def insert_poke(Poke):
    try:

        if select_poke(Poke.name) == None: # Consult registre
            poke_insert = models.driver_mongodb.Connect.db.pokemon
            poke_id = poke_insert.insert_one(Poke.__dict__()).inserted_id
            poke_id

        else:
            pass
    except:
        pass
