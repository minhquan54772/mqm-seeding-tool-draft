from werkzeug.utils import secure_filename
from app import admin_required, app, getExcel
from flask import request, redirect, flash, session, url_for
import os
from clone import model


@app.route("/uploadUsersFile", methods=["GET", "POST"])
def uploadUsersFile():
    if request.method == "POST":
        if "usersfile" not in request.files:
            flash("No file part")
            return redirect(request.url)

        usersfile = request.files["usersfile"]
        if usersfile.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if usersfile:
            filename = secure_filename(usersfile.filename)
            path = app.config["UPLOAD_FOLDER"] + "/" + session["username"]
            # path = app.config["UPLOAD_FOLDER"] + "\\" + session["username"]
            usersfile.save(os.path.join(path, filename))

            # filepath = path + "\\" + filename # Windows
            filepath = path + "/" + filename  # Ubuntu
            users = getExcel(filepath)

            for user in users:
                model.Clone.addClone(user[0], user[1], user[2], user[3], user[4])
                # Corresponding with Excel's columns file
                # (user[0], user[1],    user[2],    user[3],    user[4])
                #  STT      api_id      api_hash    name        sdt         

    return redirect(url_for("manageCloneAccount"))


@app.route("/addUser", methods=["GET", "POST"])
@admin_required
def addUser():
    api_id = request.form["api_id"]
    api_hash = request.form["api_hash"]
    username = request.form["username"]
    phone = request.form["phone"]
    return model.Clone.addClone(api_id, api_hash, username, phone)


@app.route("/deleteAllUsers", methods=["GET", "POST"])
@admin_required
def deleteAllUsers():
    return model.Clone.deleteAllClone()


@app.route("/deleteClone/<_api_id>", methods=["GET", "POST"])
@admin_required
def deleteClone(_api_id):
    return model.Clone.deleteClone(_api_id)


@app.route("/editClone/<_id>", methods=["GET", "POST"])
@admin_required
def editUser(_id):
    api_id = request.form["edit_api_id"]
    api_hash = request.form["edit_api_hash"]
    username = request.form["edit_username"]
    phone = request.form["edit_phone"]

    return model.Clone.editClone(_id, api_id, api_hash, username, phone)