import json
import ast
from flask import Blueprint, request, render_template, jsonify, make_response
from blueprints.pokemon.Class.poke_abilites import PokeAbiliteis
from utils.poke_update import update_poke
from utils.poke_select import select_all_poke, select_poke
from utils.poke_df import df_pandas_poke  # Colcoar na pasta pokemon

app_pokemon = Blueprint("pokemon", __name__, url_prefix="/pokemon")


@app_pokemon.route("/")
def index():
    return f"Page people."


@app_pokemon.route("/poke", methods=['POST', 'GET'])
def poke():
    if request.method == "POST":
        try:

            poke_dict = ast.literal_eval(request.cookies.get("cookiePokemonDict"))
            user_dict = ast.literal_eval(request.cookies.get("cookieUsers"))

            poke_dict["ability"] = request.form["ability"]
            poke_update = PokeAbiliteis(poke_dict["name"], poke_dict["pic"], poke_dict["ability"])
            update_poke(poke_update)  # Realiza o update no mongoDb
            poke_list = select_all_poke()
            return render_template("ok.html", user=user_dict["email"], table=poke_list.to_html(escape=False, index=False), message="List Pokemon update!")
        except:
            pass
    return render_template("index.html")


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
    return render_template("index.html")


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
                resp = make_response(render_template("poke.html", pokemon=poke_dict["name"], pic=poke_dict["pic"],
                                                     ability=poke_dict["ability"]))

                resp.set_cookie("cookiePokemonDict", str(poke_dict))

                return resp

        except:
            pass

    return render_template('poke.html')


"""
Function insert a new pokemon in mongoDB
"""


@app_pokemon.route('/poke_add', methods=['POST', 'GET'])
def poke_add():
    try:
        global poke_list
        df_json = df_pandas_poke(str(request.form['poke']).lower())  # Fuction return DataFrame and insert Pokemon in MongoDb
        poke_list = select_all_poke()

        # json_load = json.loads(df_json)

        return render_template("ok.html", user=user_dict["email"], table=poke_list.to_html(escape=False, index=False), message="Pokemon cadastrado!")
        # return jsonify(html="application/json",
        #               message="ok",
        #               data=json_load,
        #               status=200
        #               )
    except:
        return render_template("ok.html", user=user_dict["email"], table=poke_list.to_html(escape=False, index=False), message="Pokemon not found!")

    return render_template('index.html')
