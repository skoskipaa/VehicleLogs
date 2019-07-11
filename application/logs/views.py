from application import app, db
from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from flask_user import roles_required

from application.logs.models import Log
from application.logs.forms import LogForm
from application.vehicles.models import Vehicle
from application.auth.models import User


@app.route("/logs/")
@roles_required('ADMIN')
def logs_index():
    logs = Log.query.order_by(Log.vehicle_id.asc()).all()
    return render_template("logs/list.html", logs=logs, name="All")


@app.route("/logs/<vehicle_id>/new/")
def logs_form(vehicle_id):
    veh = Vehicle.query.get(vehicle_id)
    last_log = Log.query.filter_by(vehicle_id=vehicle_id).order_by(Log.odometer.desc()).first()
    last_odo = last_log.odometer
    return render_template("logs/new.html", form=LogForm(), vehicle_id=veh.id,
                           name=veh.plate, last_odo=last_odo)


@app.route("/logs/<vehicle_id>", methods=["GET"])
@roles_required('ADMIN')
def logs_for_vehicle(vehicle_id):
    logs = Log.query.filter_by(vehicle_id=vehicle_id).all()
    v = Vehicle.query.get_or_404(vehicle_id)
    return render_template("logs/list.html", logs=logs, name=v.plate)


@app.route("/logs/<vehicle_id>", methods=["POST"])
@login_required
def logs_create(vehicle_id):
    form = LogForm(request.form)

    if not form.validate():
        flash("Please, check your input!", category="warning")
        return render_template("logs/new.html", form=form, vehicle_id=vehicle_id)

    log_type = form.log_type.data
    odometer = form.odometer.data

    last_log = Log.query.filter_by(vehicle_id=vehicle_id).order_by(Log.odometer.desc()).first()
    last_odo = last_log.odometer

    if last_odo > odometer:
        flash("Check odometer reading. (Must be greater or equal than last.)",
              category="warning")
        return render_template("logs/new.html", form=form,
                               vehicle_id=vehicle_id, last_odo=last_odo)

    driver_id = current_user.id

    l = Log(log_type, odometer, driver_id, vehicle_id)
    l.cost = form.cost.data
    l.details = form.details.data

    db.session().add(l)
    db.session().commit()

    return redirect(url_for("vehicles_index"))

@app.route("/logs/user/")
@login_required
def logs_for_user():

    logs = Log.query.filter_by(driver_id=current_user.id).all()
    u = User.query.get_or_404(current_user.id)

    return render_template("logs/list.html", logs=logs, name=u.name)
