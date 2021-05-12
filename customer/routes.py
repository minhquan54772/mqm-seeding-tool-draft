from flask import request, render_template, session, flash
from app import app, admin_required
from customer.model import Customer
from datetime import datetime, timedelta
import hashlib

@app.route('/login', methods = ['GET', 'POST']) 
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        return Customer.login(username, password)
        flash("Login Sucessfully!")
    return render_template('login.html', title='Login | Telegram Seeding Tool') 

@app.route('/logout')
def logout():
    return Customer.logout()

@app.route('/register', methods = ['GET', 'POST'])
@admin_required
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form \
                                and 'phone' in request.form and 'vip_pack' in request.form:
        fname = request.form['fname']
        username = request.form['username']
        password = request.form['password']
        phone = request.form['phone']
        vip_pack = request.form['vip_pack']
        register_time = datetime.today()
        flash("Account have been created ucessfully !")
        return Customer.register(fname, username, password, phone, vip_pack, register_time)
    elif request.method == 'GET':
        return render_template('register.html', title="Create new account | Telegram Seeding Tool")


@app.route('/changePassword', methods = ['GET', 'POST'])
def changePassword():
    customer = session['username']
    currentPass = hashlib.md5(request.form['currentPass'].encode()).hexdigest()
    newPass = hashlib.md5(request.form['newPass'].encode()).hexdigest()
    newPassCf = hashlib.md5(request.form['newPassCf'].encode()).hexdigest()

    return Customer.changePassword(customer, currentPass, newPass, newPassCf)

@app.route('/setAdmin', methods=['GET', 'POST'])
@admin_required
def setAdmin():
    if request.method == 'GET':
        customer = Customer.getAllUser()
        admin = Customer.getAllAdmin()
        return render_template('setadmin.html', customer = customer, admin = admin, title='Set ADMIN account | Telegram Seeding Tool')
    elif request.method == 'POST':
        username = request.form['setAdmin']
        return Customer.setAdmin(username)

@app.route('/revokeAdmin', methods=['GET', 'POST'])
@admin_required
def revokeAdmin():
    username = request.form['revokeAdmin']
    return Customer.revokeAdmin(username)
