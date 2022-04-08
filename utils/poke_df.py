import json

import pandas

from pandas.io.json import json_normalize

from models.poke_abilites import PokeAbiliteis

from utils.poke_insert import insert_poke

import requests


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
            insert_poke(PokeAbiliteis(poke.name, poke.pic, poke.name_abilities))

        return df.to_json(orient="records")
    else:
        return {"code": ress.status_code}
