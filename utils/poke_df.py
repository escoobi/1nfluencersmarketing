import json

import pandas

from pandas.io.json import json_normalize

from blueprints.pokemon.Class.poke_abilites import PokeAbiliteis

from utils.poke_insert import insert_poke

import requests


"""
Method for process DataFrame in Pandas
This function receives the name of the pokemon as a parameter and performs the query in the API.
A dataFrame was created to receive the JSON from the API query.
A loop was created to check the pokemon's skills, as it has pokemon with more than one skills.
In the loop I compare the dataFrames and pass skills and other information to the Poke Class which returns me a dictionary ready to send to mongoDB.
"""


def df_pandas_poke(pokemon: str) -> str:
    ress = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

    if ress.status_code == 200:

        df_abilities = pandas.DataFrame(ress.json()["abilities"])

        df = pandas.DataFrame()

        for x in range(df_abilities["ability"].index.size):
            poke = PokeAbiliteis(ress.json()["name"],
                                 ress.json()["sprites"]["other"]["official-artwork"]["front_default"],
                                 df_abilities.iloc[x]["ability"]["name"])

            df = df.append(poke.__dict__(), ignore_index=True)
            insert_poke(PokeAbiliteis(poke.name, poke.pic, poke.name_abilities)) # Insert Class in MongoDB.

        return df.to_json(orient="records") # return a json classification for records
    else:
        return {"code": ress.status_code}
