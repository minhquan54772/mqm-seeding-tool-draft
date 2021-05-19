from flask import request, render_template, session, flash
from app import app, admin_required
from customer.model import Customer
from datetime import datetime, timedelta
import hashlib


@app.route("/login", methods=["GET", "POST"])
def login():
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
    ):
        username = request.form["username"]
        password = request.form["password"]
        return Customer.login(username, password)
    return render_template("login.html", title="Đăng nhập | Telegram Seeding Tool")


@app.route("/logout")
def logout():
    return Customer.logout()


@app.route("/register", methods=["GET", "POST"])
@admin_required
def register():
    if (
        request.method == "POST"
        and "username" in request.form
        and "password" in request.form
        and "phone" in request.form
        and "vip_pack" in request.form
    ):
        fname = request.form["fname"]
        username = request.form["username"]
        password = request.form["password"]
        phone = request.form["phone"]
        vip_pack = request.form["vip_pack"]
        register_time = datetime.today()

        return Customer.register(
            fname, username, password, phone, vip_pack, register_time
        )
    elif request.method == "GET":
        return render_template(
            "register.html", title="Tạo tài khoản | Telegram Seeding Tool"
        )


@app.route("/changePassword", methods=["GET", "POST"])
def changePassword():
    customer = session["username"]
    currentPass = hashlib.md5(request.form["currentPass"].encode()).hexdigest()
    newPass = hashlib.md5(request.form["newPass"].encode()).hexdigest()
    newPassCf = hashlib.md5(request.form["newPassCf"].encode()).hexdigest()

    return Customer.changePassword(customer, currentPass, newPass, newPassCf)


@app.route("/setAdmin", methods=["GET", "POST"])
@admin_required
def setAdmin():
    if request.method == "GET":
        customer = Customer.getAllUser()
        admin = Customer.getAllAdmin()
        return render_template(
            "setadmin.html",
            customer=customer,
            admin=admin,
            title="Quản lý ADMIN | Telegram Seeding Tool",
        )
    elif request.method == "POST":
        username = request.form["setAdmin"]
        return Customer.setAdmin(username)


@app.route("/extend_vip_pack/<id>", methods=["GET", "POST"])
@admin_required
def extend_vip_pack(id):
    print(request.form["vip_pack"])
    vip_pack = request.form["vip_pack"]
    return Customer.extend_vip_pack(id, vip_pack)


@app.route("/revokeAdmin", methods=["GET", "POST"])
@admin_required
def revokeAdmin():
    username = request.form["revokeAdmin"]
    return Customer.revokeAdmin(username)


@app.route("/manageCustomer")
@admin_required
def manageCustomer():
    customer = Customer.getAllUser()
    return render_template(
        "manageCustomer.html",
        customer=customer,
        title="Quản lý khách hàng | Telegram Seeding Tool",
    )


@app.route("/deleteCustomer/<id>")
@admin_required
def deleteCustomer(id):
    return Customer.delete_customer(id)
