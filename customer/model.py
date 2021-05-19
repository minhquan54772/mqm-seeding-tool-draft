from flask import jsonify
from flask import session, redirect
from hmac import compare_digest

from flask.helpers import flash
from app import db, app
from datetime import datetime, timedelta

import hashlib
import re
import os

# import numpy


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    fname = db.Column(db.String(255))
    phone = db.Column(db.String(255))
    isAdmin = db.Column(db.Boolean)
    vip_pack = db.Column(db.String(10), default="")
    register_time = db.Column(db.DateTime, default="")
    sentences_per_day = db.Column(db.Integer, default=0)
    clone_limit = db.Column(db.Integer, default=0)
    effective_days = db.Column(db.Integer, default=0)
    expired_date = db.Column(db.DateTime)
    remaining_days = db.Column(db.Integer)

    def __init__(
        self,
        _username,
        _password,
        _fname,
        _phone,
        _isAdmin,
        _vip_pack,
        _register_time,
        _sentences_per_day,
        _clone_limit,
        _effective_days,
    ):
        self.username = _username
        self.fname = _fname
        self.phone = _phone
        self.isAdmin = _isAdmin
        password_hash = hashlib.md5(_password.encode())
        self.password = password_hash.hexdigest()

        self.vip_pack = _vip_pack
        self.register_time = _register_time
        self.sentences_per_day = _sentences_per_day
        self.clone_limit = _clone_limit
        self.effective_days = _effective_days
        self.expired_date = _register_time + timedelta(days=_effective_days)
        self.remaining_days = (
            _register_time.date()
            + timedelta(days=_effective_days)
            - datetime.now().date()
        ).days

    def scheduler(_username):
        customer = Customer.query.filter_by(username=_username).first()

    def return_value(_username):
        customer = Customer.query.filter_by(username=_username).first()
        return (
            customer.register_time,
            customer.sentences_per_day,
            customer.clone_limit,
            customer.effective_days,
            customer.vip_pack,
            customer.expired_date.date(),  # ngày hết hạn
            customer.remaining_days,  # số ngày còn lại
        )

    def sentences_check(_username):
        customer = Customer.query.filter_by(username=_username).first()
        return customer.sentences_per_day

    def update_sentences(_username, _used_sentences):
        customer = Customer.query.filter_by(username=_username).first()
        sentences_left = customer.sentences_per_day

        if _used_sentences > int(sentences_left):
            print(
                "You have run over your converstations! Converstations left: ",
                sentences_left,
            )
            return False
        else:
            sentences_left = sentences_left - _used_sentences
            print("** Sentences_per_day left after this action: ", sentences_left)
            customer.sentences_per_day = sentences_left
            db.session.commit()
            return True

    def register(_fname, _username, _password, _phone, _vip_pack, _register_time):
        existed = Customer.query.filter_by(username=_username).first()
        # Vip pack is avalable from now: _vip_pack
        if existed:
            return jsonify({"error": "Username existed"}), 400
        elif not re.match(r"[A-Za-z0-9]+", _username):
            return (
                jsonify({"error": "Tên đăng nhập chỉ bao gồm chữ và số"}),
                400,
            )
        elif not re.match(r"[A-Za-z ]+", _fname):
            return (
                jsonify({"error": "Họ và tên chỉ bao gồm chữ và khoảng trắng"}),
                400,
            )
        elif not re.match(r"^(\+84)+([1-9]{1})+([0-9]{8})", _phone):
            return (
                jsonify({"error": 'Số điện thoại phải có dạng "+84xxxxxxxxx"'}),
                400,
            )
        else:
            # Define vip pack
            if _vip_pack == "":
                sentences_per_day = 0
                clone_limit = 0
                effective_days = 0
            if _vip_pack == "Vip1":
                sentences_per_day = 1200
                clone_limit = 4
                effective_days = 30
            if _vip_pack == "Vip2":
                sentences_per_day = 3600
                clone_limit = 12
                effective_days = 30
            if _vip_pack == "Vip3":
                sentences_per_day = 9000
                clone_limit = 30
                effective_days = 30

            customer = Customer(
                _username,
                _password,
                _fname,
                _phone,
                0,
                _vip_pack,
                _register_time,
                sentences_per_day,
                clone_limit,
                effective_days,
            )
            try:
                # create new folders to store user's uploaded files
                new_folder = os.path.join(app.config["UPLOAD_FOLDER"], _username)
                os.makedirs(new_folder)
            except OSError:
                print("Folder existed")
                pass
            db.session.add(customer)
            db.session.commit()
            flash("Tài khoản {} đã được tạo thành công".format(_username))
            return jsonify({"status": "Tạo tài khoản mới thành công"}), 200

    def login(_username, _password):
        customer = Customer.query.filter_by(username=_username).first()
        password = hashlib.md5(_password.encode()).hexdigest()
        if customer:
            # if customer.remaining_days <= 0:
            #     flash("Tài khoản của bạn đã hết hạn")
            #     # return redirect("/login")

            if compare_digest(password, customer.password):
                session["loggedin"] = True
                session["username"] = customer.username
                session["fname"] = customer.fname
                session["phone"] = customer.phone
                session["isAdmin"] = customer.isAdmin
                return jsonify({"status": "Login successfully"}), 200
            else:
                return jsonify({"error": "Mật khẩu không đúng"}), 401
        else:
            return jsonify({"error": "Tên đăng nhập không tồn tại"}), 401

    def logout():
        session.clear()
        return redirect("/login")

    def changePassword(_username, _currentPass, _newPass, _newPassCf):
        customer = Customer.query.filter_by(username=_username).first()

        if compare_digest(_currentPass, customer.password):
            if compare_digest(_newPass, _newPassCf):
                customer.password = _newPassCf
                db.session.commit()
                return jsonify({"status": "Thay đổi mật khẩu thành công"}), 200
            else:
                return jsonify({"error": "Mật khẩu không giống nhau"}), 400
        else:
            return jsonify({"error": "Mật khẩu cũ không đúng"}), 400

    def setAdmin(_username):
        user = Customer.query.filter_by(username=_username).first()
        if user:
            user.isAdmin = 1
            db.session.commit()
            return jsonify({"status": "Promote user successfully"}), 200
        else:
            return jsonify({"error": "Username does not exist"}), 400

    def revokeAdmin(_username):
        user = Customer.query.filter_by(username=_username).first()
        if user:
            user.isAdmin = 0
            user.register_time = datetime.today().date()
            user.vip_pack = "None"
            user.sentences_per_day = 0
            user.clone_limit = 0
            user.effective_days = 0
            db.session.commit()
            return jsonify({"status": "Revoke successfully"}), 200
        else:
            return jsonify({"error": "Username does not exist"}), 400

    def getAllUser():
        user = Customer.query.filter_by(isAdmin=0).all()
        return user

    def getAllAdmin():
        admin = Customer.query.filter_by(isAdmin=1).all()
        return admin

    def admin_pack():
        all = Customer.query.all()
        for customer in all:
            if customer.isAdmin is True:
                customer.register_time = datetime.today().date()
                customer.vip_pack = "Vipad"
                customer.sentences_per_day = 9999
                customer.clone_limit = 9999
                customer.effective_days = 9999
                db.session.commit()

    def update_remaining_days(_username):
        customer = Customer.query.filter_by(username=_username).first()
        today = datetime.now().date()
        customer.remaining_days = (
            customer.register_time.date()
            + timedelta(days=customer.effective_days)
            - today
        ).days
        if customer.remaining_days <= 0:
            flash("Tài khoản của bạn đã hết hạn. Vui lòng liên hệ ADMIN để gia hạn")
            return redirect("/login")
        elif customer.remaining_days <= 5:
            flash(
                "Tài khoản của bạn sắp hết hạn (còn {} ngày). Vui lòng liên hệ ADMIN để gia hạn".format(
                    customer.remaining_days
                )
            )
        db.session.commit()

    def extend_vip_pack(_id, _vip_pack):
        customer = Customer.query.filter_by(id=_id).first()
        print(customer)
        customer.vip_pack = _vip_pack
        if _vip_pack == "Vip1":
            customer.sentences_per_day += 1200
            customer.clone_limit = 4

        elif _vip_pack == "Vip2":
            customer.sentences_per_day += 3600
            customer.clone_limit = 12

        elif _vip_pack == "Vip3":
            customer.sentences_per_day += 9000
            customer.clone_limit = 30

        customer.remaining_days += 30
        customer.expired_date += timedelta(days=30)
        db.session.commit()
        flash(
            "Gia hạn thành công tài khoản {}, gói {}".format(
                customer.username, _vip_pack
            )
        )
        return redirect("/setAdmin")

    def delete_customer(_id):
        Customer.query.filter_by(id=_id).delete()
        db.session.commit()
        flash("Xoá tài khoản thành công")
        return redirect("/manageCustomer")
