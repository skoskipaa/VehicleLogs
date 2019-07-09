from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from flask_user import roles_required

from application import app, db, bcrypt
from application.auth.models import User, Role
from application.auth.forms import LoginForm, UserForm
from sqlalchemy.exc import IntegrityError


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/loginform.html", form=form)

    user_found = User.query.filter_by(username=form.username.data).first()

    if user_found:
        auth_user = bcrypt.check_password_hash(user_found.password,
                                               form.password.data)
        if not auth_user:
            flash("No such username or password", category="danger")
            return render_template("auth/loginform.html", form=form)
    
        login_user(user_found)
        return redirect(url_for("index"))

    flash("No such username or password", category="danger")
    return render_template("auth/loginform.html", form=form)


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    flash("You have been logged out!", category="success")
    return redirect(url_for("index"))


@app.route("/auth/register", methods=["GET", "POST"])
@roles_required('ADMIN')
def users_create():
    if request.method == "GET":
        return render_template("auth/userform.html", form=UserForm())

    form = UserForm(request.form)

    if not form.validate():
        flash("Please, check your input!", category="warning")
        return render_template("auth/userform.html", form=form)
    
    if not form.password.data == form.password_conf.data:
        flash("Passwords not equal!", category="warning")
        return render_template("auth/userform.html", form=form)

    try:
        name = form.name.data
        username = form.username.data
        password = form.password.data
        r = form.role.data

        u = User(name, username, password)
        u.roles.append(Role(name=r))
        db.session().add(u)
        db.session().commit()

        flash("New user account created successfully!", category="success")
        return redirect(url_for("index"))

    except IntegrityError:
        flash("Username already taken!", category="warning")
        return render_template("auth/userform.html", form=form)
        

@app.route("/auth/list")
@roles_required('ADMIN')
def users_index():
    us = User.query.all()
    return render_template("auth/list.html", users=us)
