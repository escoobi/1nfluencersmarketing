import json
import ast
from flask import Blueprint, request, render_template, jsonify, make_response
from models.poke_abilites import PokeAbiliteis
from controllers.poke_update import update_poke
from controllers.poke_select import select_all_poke, select_poke
from controllers.poke_df import df_pandas_poke

app_pokemon = Blueprint("pokemon", __name__, url_prefix="/pokemon")


@app_pokemon.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        try:
            poke_dict = ast.literal_eval(request.cookies.get("cookiePokemonDict"))  # used pck ast.literal at code for convert str to dict
            user_dict = ast.literal_eval(request.cookies.get("cookieUsers"))  # used pck ast.literal at code for convert str to dict
            poke_dict["ability"] = request.form["ability"]
            poke_update = PokeAbiliteis(poke_dict["name"], poke_dict["pic"], poke_dict["ability"])
            update_poke(poke_update)  # Realiza o update no mongoDb
            poke_list = select_all_poke()
            return render_template("/pokemon/index.html", user=user_dict["email"], table=poke_list.to_html(escape=False, index=False), message="List Pokemon update!")
        except:
            pass
    return render_template("/pokemon/index.html")


@app_pokemon.route("/poke", methods=['POST', 'GET'])
def poke():
    if request.method == "POST":
        try:
            poke_dict = ast.literal_eval(request.cookies.get("cookiePokemonDict"))  # used pck ast.literal at code for convert str to dict
            user_dict = ast.literal_eval(request.cookies.get("cookieUsers"))  # used pck ast.literal at code for convert str to dict
            poke_dict["ability"] = request.form["ability"]
            poke_update = PokeAbiliteis(poke_dict["name"], poke_dict["pic"], poke_dict["ability"])
            update_poke(poke_update)  # Realiza o update no mongoDb
            poke_list = select_all_poke()
            return render_template("/pokemon/index.html", user=user_dict["email"], table=poke_list.to_html(escape=False, index=False), message="List Pokemon update!")
        except:
            pass
    return render_template("/pokemon/index.html")


@app_pokemon.route('/poke_json', methods=['GET'])
def poke_json():
    try:
        cookiePokemon = request.cookies.get('cookiePokemon')

        if cookiePokemon is not None:
            df_json = df_pandas_poke(str(request.args['pokemon_add']).lower())  # Fuction return DataFrame and insert Pokemon in MongoDb
            json_load = json.loads(df_json)
            return jsonify(html="application/json",
                           message="ok",
                           data=json_load,
                           status=200
                           )

    except:
        pass
    return render_template("/pokemon/index.html")


"""
Method construtor models poke_abilities and set dataframe with return json. (df_pandas_poke)
"""


@app_pokemon.route('/pokemon', methods=['POST', 'GET'])
def pokemon():
    if request.method == "POST":
        try:
            if request.form['pokemon'] is not None:
                poke_dict = select_poke(request.form['pokemon'])
                print(poke_dict)
                resp = make_response(render_template("/pokemon/poke.html", pokemon=poke_dict["name"], pic=poke_dict["pic"],
                                                     ability=poke_dict["ability"]))

                resp.set_cookie("cookiePokemonDict", str(poke_dict))
                return resp

        except:
            pass

    return render_template('/pokemon/poke.html')


'''
Function insert a new pokemon in mongoDB
'''


@app_pokemon.route('/poke_add', methods=['POST', 'GET'])
def poke_add():
    try:
        df_json = df_pandas_poke(str(request.form['poke']).lower())  # Fuction return DataFrame and insert Pokemon in MongoDb
        poke_list = select_all_poke()
        user_dict = ast.literal_eval(request.cookies.get("cookieUsers"))  # used pck ast.literal at code for convert str to dict
        return render_template("/pokemon/index.html", user=user_dict["email"], table=poke_list.to_html(escape=False, index=False), message="Pokemon cadastrado!")
    except:
        return render_template("/pokemon/index.html", user=user_dict["email"], table=poke_list.to_html(escape=False, index=False), message="Pokemon not found!")

    return render_template('/pokemon/index.html')
