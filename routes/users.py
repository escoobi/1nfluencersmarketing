from flask import Blueprint, request, render_template, make_response
from controllers.users_select import select_user_auth
from controllers.poke_select import select_all_poke
from controllers.users_insert import insert_user
from controllers.users_update import update_users
from models.users import Users
from models.users_form import form_users
from models.users_form_update import form_users_update
from models.login_form import form_login
import ast

app_user = Blueprint("user", __name__, url_prefix="/user")


@app_user.route("/", methods=['POST', 'GET'])
def index():
    my_form = form_login()

    if request.method == "POST":
        try:

            user_dict = select_user_auth(my_form.input_email.data, my_form.input_password.data)
            poke_list = select_all_poke()

            resp = make_response(render_template("/pokemon/index.html", form=my_form, user=user_dict["email"], table=poke_list.to_html(escape=False, index=False)))

            resp.set_cookie('cookiePokemon', str(poke_list))
            resp.set_cookie('cookieUsers', str(user_dict))

            return resp
        except:
            return render_template("/user/index.html", form=my_form, message="Usuário/Password, error!")  # Ajustado

    return render_template('/user/index.html', form=my_form)


@app_user.route('/users', methods=['POST', 'GET'])
def users():
    try:
        my_form = form_users()

        if request.method == "POST":
            # Class insert_user -> if user found -> update
            msg = insert_user(Users(my_form.input_email.data, my_form.input_name.data, my_form.input_password.data))
            return render_template("/user/users.html", form=my_form, message=msg)
        return render_template("/user/users.html", form=my_form, message="Novo cadastro.")
    except:
        return render_template("/user/index.html")


@app_user.route('/users_update', methods=['POST', 'GET'])
def users_update():
    try:
        my_form = form_users_update()
        if request.method == "POST":
            user_dict = ast.literal_eval(request.cookies.get("cookieUsers"))  # used pck ast.literal at code for convert str to dict
            if request.form["usr"] == "up":
                usrdict: dict = {}
                usrdict["password"] = my_form.input_password.data
                msg = update_users(usrdict,
                                   Users(user_dict["email"], user_dict["name"], user_dict["password"]))
                return render_template("/user/users_update.html", form=my_form, email=user_dict["email"], name=user_dict["name"], message=msg)
        return render_template("/user/users_update.html", form=my_form, email=user_dict["email"], name=user_dict["name"], message="Alterar cadastro.")

    except:
        return render_template("/user/index.html")
