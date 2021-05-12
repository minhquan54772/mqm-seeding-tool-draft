from groups.model import Group
from werkzeug.utils import secure_filename
from app import check_and_join, getExcel, app
from flask import redirect, flash, session, request, url_for
from telethon.sync import TelegramClient
import os


@app.route("/deleteAllGroups")
def deleteAllGR():
    customer = session["username"]
    return Group.deleteAllGroup(customer)


@app.route("/uploadGroupFile", methods=["GET", "POST"])
def uploadGroupFile():
    if request.method == "POST":
        if "groupfile" not in request.files:
            flash("No file part")
            return redirect(request.url)

        groupfile = request.files["groupfile"]
        if groupfile.filename == "":
            flash("No selected file")
            return redirect(request.url)

        if groupfile:
            filename = secure_filename(groupfile.filename)
            path = app.config["UPLOAD_FOLDER"] + "/" + session["username"]
            # path = app.config["UPLOAD_FOLDER"] + "\\" + session["username"]
            groupfile.save(os.path.join(path, filename))

            filepath = path + "/" + filename
            # filepath = path + "\\" + filename

            grouplinks = getExcel(filepath)

            client = TelegramClient(
                "ToGetGroupID", 3845192, "ee3f76456f539941ef8c223d793c1187"
            )
            with client:
                for link in grouplinks:
                    group = check_and_join(client, link[0])
                    Group.addGroup(
                        session["username"],
                        group["group_id"],
                        group["group_title"],
                        link[0],
                    )
    return redirect(url_for("manageGroups"))


@app.route("/addGroup", methods=["GET", "POST"])
def addGroup():
    group_link = request.form["grouplink"]
    client = TelegramClient("ToGetGroupID", 4030475, "d8d57cfa02a809076c4106cafb5a02ca")
    with client:
        join = check_and_join(client, group_link)
        return Group.addGroup(
            session["username"], join["group_id"], join["group_title"], group_link
        )

@app.route("/deleteGroup/<id>")
def deleteGroup(id):
    customer = session["username"]
    return Group.deleteGroup(customer, id)
