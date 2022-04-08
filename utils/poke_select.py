import pandas
import pymongo
from models.poke_abilites import PokeAbiliteis
import models.driver_mongodb


def select_poke(name: str) -> dict:
    try:

        poke_select = models.driver_mongodb.Connect.db.pokemon

        poke_dict = poke_select.find_one({"name": name})

        return {"name": poke_dict["name"], "pic": poke_dict["pic"], "ability": poke_dict["ability"]}

    except:
        pass

def select_all_poke() -> pandas.DataFrame:
    try:

        poke_select = models.driver_mongodb.Connect.db.pokemon

        poke_dict = poke_select.find()

        df = pandas.DataFrame(poke_dict)
        #for x in poke_dict:
         #   print(x)
        return df

    except:
        pass

