from telethon.tl.types import Dialog
import os
from werkzeug.utils import secure_filename
from app import getExcel, app
from flask import redirect, flash, session, request, url_for
from dialog.model import Dialog
import emoji


@app.route("/deleteAllContent")
def deleteAllContent():
    username = session["username"]
    return Dialog.delete_all_message(username)
    

@app.route("/uploadContentFile", methods=["GET", "POST"])
def uploadContentFile():
    if request.method == "POST":
        if "contentfile" not in request.files:
            flash("No file part")
            return redirect(request.url)

        contentfile = request.files["contentfile"]
        if contentfile.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if contentfile:
            filename = secure_filename(contentfile.filename)
            path = app.config["UPLOAD_FOLDER"] + "/" + session["username"]
            # path = app.config["UPLOAD_FOLDER"] + "\\" + session["username"]
            contentfile.save(os.path.join(path, filename))

            filepath = path + "/" + filename
            # filepath = path + "\\" + filename
            dialog = getExcel(filepath)

            for dia in dialog:
                dia[1] = emoji.demojize(dia[1])
                Dialog.add_message(session["username"], dia[0], dia[1], dia[2], dia[3])

    return redirect(url_for("manageScenario"))


@app.route("/addContent", methods=["GET", "POST"])
def addContent():
    customer = session["username"]
    speaker = request.form["addSpeaker"]
    group_id = request.form["addGroupID"]
    message = emoji.demojize(request.form["addMessage"])
    delay = request.form["addDelay"]
    print(request.form.to_dict())

    return Dialog.add_message(customer, speaker, message, group_id, delay)


@app.route("/editMessage/<id>", methods=["GET", "POST"])
def editContent(id):
    customer = session["username"]
    speaker = request.form["editSpeaker" + id]
    group_id = request.form["editGroupID" + id]
    message = emoji.demojize(request.form["editMessage" + id])
    delay = request.form["editDelay" + id]

    return Dialog.edit_message(id, customer, speaker, message, group_id, delay)


@app.route("/deleteMessage/<id>")
def deleteMessage(id):
    customer = session["username"]
    return Dialog.delete_message(id, customer)
