import json

import pandas

from flask import Flask, render_template, request, redirect, url_for, jsonify

from utils.users_insert import insert_user

from utils.poke_df import df_pandas_poke

from models.users import Users

from utils.users_select import select_user_auth

from utils.poke_select import select_all_poke


'''
Author = Gustavo O. Cardozo
Email = gustavo.o.c@icloud.com
Linkedin = https://www.linkedin.com/in/gustavo-oliveira-cardozo-0258a993/
--------------------------------------------------------------------------
This application performs user authentication using MongoDB.
It allows registering the user and changing the password.
The user logging in has access to Pokemon research using the api (https://pokeapi.co/) we consume this api and treat the data using dataframes (Pandas) and finally registering in mongoDb with the pokemon's name, photo of the pokemon and its ability.
And we display a table of registered pokemon.
When we make the query in the api, it presents the information handled with Pandas in JSON format.

'''

user_name: str
poke_list:  pandas.DataFrame

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ok')
def ok():
    return render_template('poke.html')


"""
Method construtor class poke_abilities and set dataframe with return json. (df_pandas_poke)
"""


@app.route('/pokemon', methods=['POST', 'GET'])
def pokemon():
    if request.method == "POST":
        try:
            df_json = df_pandas_poke(str(request.form['poke']).lower()) # Fuction return DataFrame and insert Pokemon in MongoDb
            json_load = json.loads(df_json)
            global poke_list
            poke_list = select_all_poke()

            return jsonify(html="application/json",
                           message="ok",
                           data=json_load,
                           status=200
                           )
        except:
            return render_template("ok.html", user=f"Welcome! {user_name}", table=poke_list.to_html(escape=False, index=False), message="Pokemon not found!")

    return render_template('poke.html')


@app.route('/fail')
def fail():
    return render_template("fail.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    Method poke_all return a dict all pokemon in the mongodb
    """
    if request.method == "POST":
        try:
            usr = select_user_auth(request.form["email"], request.form["password"])
            global user_name
            global poke_list
            user_name = usr['name']
            poke_list = select_all_poke()
            return render_template("ok.html", user=f"Welcome! {usr['name']}", table=poke_list.to_html(escape=False, index=False))
        except:
            return render_template("login.html", message="Usuário/Password, error!")  # Ajustado

    return render_template('login.html')


@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == "POST":
        insert_user(Users(request.form["email"], request.form["name"], request.form["password"]))
        return render_template("index.html", message="Usuário cadastrado com sucesso.")
    return render_template("users.html")


if __name__ == '__main__':
    app.run(debug=True)
