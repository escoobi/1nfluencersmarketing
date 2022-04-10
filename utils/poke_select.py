import pandas
import pymongo
import models.driver_mongodb

"""
Method for select pokemon in mongoDb

1- The first function takes the name of the pokemon to query and returns a dictionary
2 - The second function receives or does not receive attributes, it queries all pokemon registered in mongoDB and returns a pandas.DataFrame
"""


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

        df = pandas.DataFrame(poke_dict, columns=["name", "pic", "ability"])
        df["name"] = df["name"].apply(lambda x: f'<form action="pokemon" method="post"><button type="submit" name="pokemon" value="{x}">{x}</button></form>')
        df["pic"] = df["pic"].apply(lambda x: f'<img src="{x}" alt="Pokemon" width="30" height="30">')

        return df

    except:
        pass
