import os
import pandas as pd
import asyncio
import emoji
import _thread

from datetime import datetime, timedelta
from telethon.tl.functions.channels import JoinChannelRequest
from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import Flask, render_template, redirect, session, request, url_for, flash
from functools import wraps
from flask.helpers import send_file
from telethon.sync import TelegramClient
from telethon.tl.types import ChatInvite, ChatInviteAlready
from telethon.tl.functions.messages import (
    CheckChatInviteRequest,
    ImportChatInviteRequest,
)
from tornado.platform.asyncio import AnyThreadEventLoopPolicy

asyncio.set_event_loop_policy(AnyThreadEventLoopPolicy())


# Decorators
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "loggedin" in session:
            return f(*args, **kwargs)
        else:
            return redirect("/login")

    return wrap


def admin_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if session["isAdmin"] == 1:
            return f(*args, **kwargs)
        else:
            return redirect("/index")

    return wrap


# FLASK ROUTES ------------------------------------------------------------------------------------------
try:
    UPLOAD_FOLDER = "uploaded_files"
except:
    os.makedirs("uploaded_files")
    UPLOAD_FOLDER = "uploaded_files"

app = Flask(__name__)
app.secret_key = b"\xa3\x92.\x8b\\\x06\x17\x9e1\x1c4\xb6\xf2\xff}\xfb"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root" "@localhost/mqm_seeding_tool"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=1)

db = SQLAlchemy(app)
sched = BackgroundScheduler(daemon=True)
sched.start()


from dialog.model import Dialog
from groups.model import Group
from clone.model import Clone
from customer.model import Customer

# DATABASE FUNCTIONS -----------------
# get data from Excel file
def getExcel(file):
    data = pd.read_excel(file)
    val = data.values.tolist()
    return val


# end database functions -------------

# -------------------------------------------------------------------
async def interact(client, group_id, content):
    try:
        me = await client.get_me()
        await client.send_message(group_id, content)
        print(
            me.phone,
            "sent to {} -->".format(group_id),
            content,
        )
    except:
        print(
            "Something happend with this interact, the clone may die, please check again!"
        )
        pass


def check_and_join(client, group_link):
    try:
        hash = group_link[22:]
        check = client(CheckChatInviteRequest(hash))
        if isinstance(check, ChatInvite):
            join = client(ImportChatInviteRequest(hash=hash))
            print(client.get_me().phone, "not join", join.chats[0].id)
            if len(str(join.chats[0].id)) == 10:
                group_title = join.chats[0].title
                group_id = "-100" + str(join.chats[0].id)
                return {"group_id": group_id, "group_title": group_title}
            else:
                group_title = join.chats[0].title
                group_id = "-" + str(join.chats[0].id)
                return {"group_id": group_id, "group_title": group_title}
        elif isinstance(check, ChatInviteAlready):
            print(client.get_me().phone, "joined", check.chat.id)
            if len(str(check.chat.id)) == 10:
                group_title = check.chat.title
                group_id = "-100" + str(check.chat.id)
                return {"group_id": group_id, "group_title": group_title}
            else:
                group_title = check.chat.title
                group_id = "-" + str(check.chat.id)
                return {"group_id": group_id, "group_title": group_title}
    except:
        check = client(JoinChannelRequest(channel=group_link))
        print(client.get_me().phone, "join channel", check.chats[0].id)
        if len(str(check.chats[0].id)) == 10:
            group_title = check.chats[0].title
            group_id = "-100" + str(check.chats[0].id)
            return {"group_id": group_id, "group_title": group_title}
        else:
            group_title = check.chats[0].title
            group_id = "-" + str(check.chats[0].id)
            return {"group_id": group_id, "group_title": group_title}


def check_expired_time(register_time, total_delays_seconds, day_left):
    now = datetime.today()
    check_days = register_time + timedelta(days=day_left)
    if now > check_days:
        print("Service time expired, please buy more!!", check_days)
        return False
    elif now + timedelta(seconds=total_delays_seconds) > check_days:
        print(
            "Converstation time is exceeding service time limit, please change delays time."
        )
        return False
    else:
        return True


def check_all_condition(username):
    dialogue = Dialog.get_all_message(username)
    (
        register_time,
        sentences_per_day,
        clone_limit,
        effective_days,
        _,
        _,
    ) = Customer.return_value(username)
    total_delays_seconds = 0
    clone_number = set()
    group_number = set()
    for dial in dialogue:
        total_delays_seconds += dial.delay  # 15
        clone_number.add(dial.user_id)
        group_number.add(dial.group_id)
    time_check = datetime.now()
    used_sentences = len(dialogue)
    if len(clone_number) <= clone_limit:
        print(">> 1. First check: Clone number is less than clone limit: Success!")
    else:
        return str(
            "Số lượng Clone vượt quá giới hạn dịch vụ. Vui lòng kiểm tra lại Clone tại Quản lý hội thoại."
        )

    if len(group_number) < 2:
        print(">> 2. Second check: Only one Group: Success!")
    else:
        return str(
            "Chỉ có thể thực hiện cuộc hội thoại trong một nhóm duy nhất. Vui lòng kiểm tra lại Group ID tại Quản lý hội thoại."
        )

    # Caculate service time expired and clone limit  -----------------------------------------------------
    if check_expired_time(register_time, total_delays_seconds, effective_days) == True:
        print(">> 3. Third check: In time of service: Success!")
    else:
        return str("Dịch vụ đã hết hạn. Xin vui lòng mua thêm.")
    # Caculate number of sentences left --------------------------------------------------------------
    if Customer.update_sentences(username, used_sentences) == True:
        print(">> 4. Fourth check: Sentences is in number of service: Success!")
    else:
        return str(
            "Số lượng câu thoại vượt quá giới hạn. Vui lòng kiểm tra lại số lượng câu tại Quản lý hội thoại."
        )

    return True, [used_sentences, total_delays_seconds]


def main_function(username):
    dialogue = Dialog.get_all_message(username)
    for dial in dialogue:
        user = Clone.getCloneWithID(dial.user_id)
        print(user.phone)
        group_id = int(dial.group_id)
        grouplinks = Group.getGroupWithID(group_id)
        client = TelegramClient(
            session="{}".format(user.phone[2::]),
            api_id=int(user.api_id),
            api_hash=user.api_hash,
        )

        with client:
            print("thread", _thread.get_ident())
            check_and_join(client, grouplinks.group_link)
            client.loop.run_until_complete(
                interact(client, group_id, emoji.emojize(dial.content))
            )
        sleep(dial.delay)


# ---------------------------


@app.route("/")
def main():
    return redirect(url_for("login"))


@app.route("/index")
@login_required
def index():
    # check admin pack
    Customer.admin_pack()
    username = session["username"]
    # try:
    # group_id = Dialog.get_group_id(username)
    (
        register_time,
        sentences_per_day,
        clone_limit,
        effective_days,
        vip_pack,
        effective_days,
    ) = Customer.return_value(username)
    print(
        register_time,
        sentences_per_day,
        clone_limit,
        effective_days,
        vip_pack,
        effective_days,
    )
    sentences_left = Customer.sentences_check(username)
    groups = Group.getAllGroup(session["username"])

    return render_template(
        "index.html",
        groups=groups,
        username=username,
        sentences_left=sentences_left,
        register_time=register_time.date(),
        sentences_per_day=sentences_per_day,
        clone_limit=clone_limit,
        effective_days=effective_days,
        vip_pack=vip_pack,
    )
    # except:
    #     print("pass")
    #     pass
    #     return render_template("index.html")


@app.route("/manageCloneAccount")
@admin_required
def manageCloneAccount():
    users = Clone.getAllClone()
    return render_template(
        "clone.html", users=users, title="Manage clone account | Telegram Seeding Tool"
    )


@app.route("/manageGroups")
def manageGroups():
    groups = Group.getAllGroup(session["username"])
    return render_template(
        "manageGroup.html", title="Groups | MQM Seeding Tool", groups=groups
    )


@app.route("/manageScenario")
def manageScenario():
    dialog = Dialog.get_all_message(session["username"])
    return render_template(
        "manageScenario.html", title="Scenario | MQM Seeding Tool", dialog=dialog
    )


@app.route("/download_dialog")
def download_dialog():
    path = "download/dialog.xlsx"
    return send_file(path, as_attachment=True)


@app.route("/download_groups")
def download_groups():
    path = "download/groups.xlsx"
    return send_file(path, as_attachment=True)


@app.route("/download_users")
@admin_required
def download_users():
    path = "download/users.xlsx"
    return send_file(path, as_attachment=True)


@app.route("/start")
def start():
    username = session["username"]
    checker = check_all_condition(username)
    if checker[0] is True:
        flash("Đang thực hiện hội thoại. . . ")
        _thread.start_new_thread(main_function, (username,))
    else:
        flash(checker)
    return redirect(url_for("index"))


@app.route("/schedule-tasks", methods=["GET", "POST"])
def scheduler():
    username = session["username"]
    checker = check_all_condition(username)
    if checker[0] is True:
        date = request.form["datepicker"]
        time = request.form["timepicker"]
        datetime_str = date + " " + time + ":00"
        datetime_dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
        flash("Cuộc hội thoại đã được lên lịch thành công!")
        scheduled = _thread.start_new_thread(
            wait,
            (
                username,
                datetime_dt,
            ),
        )
        return render_template(
            "index.html",
            datetime_dt=datetime_dt,
            used_sentences=checker[1][0],
            total_delays_seconds=checker[1][1],
        )
    else:
        flash(checker)
        return redirect("/index")


def wait(username, dt):
    now = datetime.now()
    sleep((dt - now).total_seconds())
    main_function(username)


from groups import routes
from dialog import routes
from clone import routes
from customer import routes

# end flask routes ------------
