import emoji
from flask import session, request
from flask.json import jsonify
from app import db


class Dialog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(80))
    user_id = db.Column(db.Integer)
    content = db.Column(db.Text)
    group_id = db.Column(db.String(255))
    delay = db.Column(db.Integer)
    
    def __init__(self, _customer, _user_id, _content, _group_id, _delay):
        self.customer = _customer
        self.user_id = _user_id
        self.content = _content
        self.group_id = _group_id
        self.delay = _delay

    def get_group_id(_customer):
        customer = Dialog.query.filter_by(customer=_customer).first()
        return customer.group_id

    # get all message according to username
    def get_all_message(_customer):
        all = Dialog.query.filter_by(customer=_customer).all()
        return all

    def add_message(_customer, _user_id, _content, _group_id, _delay):
        message = Dialog(_customer, _user_id, _content, _group_id, _delay)
        db.session.add(message)
        db.session.commit()
        return jsonify({"status": "Add Message successfully"}), 200

    def edit_message(_id, _customer, _user_id, _content, _group_id, _delay):
        message = Dialog.query.filter_by(id=_id, customer=_customer).first()
        message.user_id = _user_id
        message.content = _content
        message.group_id = _group_id
        message.delay = _delay

        db.session.commit()
        return jsonify({"status": "Update message successfully"}), 200

    def delete_all_message(_customer):
        Dialog.query.filter_by(customer=_customer).delete()
        db.session.commit()
        return jsonify({"status": "All of your messages were deleted"}), 200

    def delete_message(_id, _customer):
        Dialog.query.filter_by(customer=_customer, id=_id).delete()
        db.session.commit()
        return jsonify({"status": "Your message was deleted"}), 200
