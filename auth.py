import json
from flask import Flask, render_template, request, redirect, url_for, jsonify
from utils.users_select import select_user_auth, select_user
from utils.users_insert import insert_user
from utils.poke_df import df_pandas_poke
from models.users import Users
from utils.poke_select import select_all_poke

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ok')
def ok():
    return render_template('poke.html')


@app.route('/pokemon', methods=['POST', 'GET'])
def pokemon():
    if request.method == "POST":
        try:
            """
            Method construtor class poke_abilities and set dataframe with return json. (df_pandas_poke)
            """
            df_json = df_pandas_poke(request.form['poke'])
            json_load = json.loads(df_json)

            return jsonify(html="application/json",
                           message="ok",
                           data=json_load,
                           status=200
                           )
        except:
            return render_template("fail.html", message="pokemon not found!")

    return render_template('poke.html')


@app.route('/fail')
def fail():
    return render_template("fail.html")


@app.route('/login', methods=['POST', 'GET'])
def login():

    if request.method == "POST":
        try:
            usr_dict: dict = select_user_auth(request.form["email"], request.form["password"])
            usr: Users = Users(usr_dict["email"], usr_dict["name"], usr_dict["password"])
            if usr.name is not None:
                return render_template("ok.html", user=f"Welcome! {usr.name},", tables=[select_all_poke().to_html(classes='data')], titles=select_all_poke().columns.name)
        except:
            return render_template("fail.html", message="Auth error!")
    return render_template('login.html')


@app.route('/users', methods=['POST', 'GET'])
def users():
    if request.method == "POST":
        insert_user(Users(request.form["email"], request.form["name"], request.form["password"]))
        return redirect(url_for("ok.html"))
    return render_template("users.html")


if __name__ == '__main__':
    app.run(debug=True)
