from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application.vehicles.models import Vehicle
from application.vehicles.forms import VehicleForm


@app.route("/vehicles/new/")
@login_required
def vehicles_form():
    return render_template("vehicles/new.html", form=VehicleForm())


@app.route("/vehicles/", methods=["GET"])
def vehicles_index():
    vehicles = Vehicle.query.all()
    return render_template("vehicles/list.html", vehicles=vehicles)


@app.route("/vehicles/", methods=["POST"])
@login_required
def vehicles_create():
    form = VehicleForm(request.form)

    if not form.validate():
        return render_template("vehicles/new.html", form=form)

    plate = form.plate.data
    name = form.nickname.data
    make = form.make.data
    model = form.model.data
    year = form.year.data
    kms = form.kilometers.data

    v = Vehicle(plate, name, make, model, year, kms)
    db.session().add(v)
    db.session().commit()
    return redirect(url_for('vehicles_index'))
