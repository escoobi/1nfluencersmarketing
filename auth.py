import json

import pandas

from flask import Flask, render_template, request, jsonify

from utils.users_insert import insert_user

from utils.poke_df import df_pandas_poke

from utils.poke_update import update_poke

from models.poke_abilites import PokeAbiliteis

from models.users import Users

from forms.users_form import form_users
from forms.login_form import form_login

from utils.users_select import select_user_auth

from utils.poke_select import select_all_poke, select_poke

import os


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
poke_list: pandas.DataFrame
poke_dict: dict

app = Flask(__name__, template_folder='templates')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


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
            if request.form['pokemon'] is None:
                df_json = df_pandas_poke(str(request.form['poke']).lower())  # Fuction return DataFrame and insert Pokemon in MongoDb
                json_load = json.loads(df_json)
                global poke_list
                poke_list = select_all_poke()

                return jsonify(html="application/json",
                               message="ok",
                               data=json_load,
                               status=200
                               )
            else:

                global poke_dict

                poke_dict = select_poke(request.form['pokemon'])

                return render_template("poke.html", pokemon=poke_dict["name"], pic=poke_dict["pic"],
                                       ability=poke_dict["ability"])
        except:
            return render_template("ok.html", user=f"Welcome! {user_name}", table=poke_list.to_html(escape=False, index=False), message="Pokemon not found!")

    return render_template('poke.html')


@app.route('/poke', methods=['POST', 'GET'])
def poke():
    if request.method == "POST":
        try:

            poke_dict["ability"] = request.form["ability"]

            poke_update = PokeAbiliteis(poke_dict["name"], poke_dict["pic"], poke_dict["ability"])

            update_poke(poke_update)  # Realiza o update no mongoDb

            global poke_list

            poke_list = select_all_poke()

            return render_template("ok.html", user=f"Welcome! {user_name}", table=poke_list.to_html(escape=False, index=False), message="List Pokemon update!")
        except:
            pass
    return render_template("poke.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    Method poke_all return a dict all pokemon in the mongodb
    """

    my_form = form_login()

    if request.method == "POST":
        try:
            usr = select_user_auth(my_form.input_email.data, my_form.input_password.data)
            global user_name
            global poke_list
            user_name = usr['name']
            poke_list = select_all_poke()
            return render_template("ok.html", form= my_form, user=f"Welcome! {user_name}", table=poke_list.to_html(escape=False, index=False))
        except:
            return render_template("login.html", form= my_form, message="Usuário/Password, error!")  # Ajustado

    return render_template('login.html', form= my_form)


@app.route('/users', methods=['POST', 'GET'])
def users():

    my_form = form_users()

    if request.method == "POST":
        msg = insert_user(Users(my_form.input_email.data, my_form.input_name.data, my_form.input_password.data))
        return render_template("users.html", form=my_form, message=msg)
    return render_template("users.html", form=my_form)

if __name__ == '__main__':
    app.run(debug=True, port=6543)
