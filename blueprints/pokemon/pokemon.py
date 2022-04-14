import json
from flask import Blueprint, request, render_template, jsonify
from blueprints.pokemon.Class.poke_abilites import PokeAbiliteis
from utils.poke_update import update_poke
from utils.poke_select import select_all_poke
from utils.poke_df import df_pandas_poke  # Colcoar na pasta pokemon

app_pokemon = Blueprint("pokemon", __name__, url_prefix="/pokemon")


@app_pokemon.route("/")
def index():
    return f"Page people."


@app_pokemon.route("/poke", methods=['POST', 'GET'])
def poke():
    if request.method == "POST":
        try:
            poke_list = select_all_poke()
            poke_dict = dict(request.cookies.get("cookiePokemonDict"))
            print(poke_dict)
            user_dict = dict(request.cookies.get("cookieUsers"))
            print(type(user_dict))

            poke_dict["ability"] = request.form["ability"]
            poke_update = PokeAbiliteis(poke_dict["name"], poke_dict["pic"], poke_dict["ability"])
            update_poke(poke_update)  # Realiza o update no mongoDb
            resp = make_response(render_template("ok.html", user=user_dict["email"], table=poke_list.to_html(escape=False, index=False), message="List Pokemon update!"))
            #resp.set_cookie('cookiePokemon', str(poke_list))
            return resp
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
