from app import db
from flask import jsonify

class Group(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    customer = db.Column(db.String(80))
    group_id = db.Column(db.String(255))
    group_title = db.Column(db.Text)
    group_link = db.Column(db.Text)

    def __init__(self, _customer, _group_id, _group_title, _group_link ):
        self.customer = _customer
        self.group_id = _group_id
        self.group_title = _group_title
        self.group_link = _group_link
    
    def getAllGroup(_customer):
        all = Group.query.filter_by(customer = _customer).all()
        return all
    
    def getGroupWithID(_group_id):
        group = Group.query.filter_by(group_id = _group_id).first()
        return group

    def addGroup(_customer, _group_id, _group_title, _group_link):
        check = Group.checkExist(_customer, _group_link)
        if check:
            return jsonify({'error' : 'Group existed'}), 400
        else:
            group = Group(_customer, _group_id, _group_title, _group_link)
            db.session.add(group)
            db.session.commit()
            return jsonify({'status' : 'Add group successfully'}), 200

    def deleteAllGroup(_customer):
        Group.query.filter_by(customer = _customer).delete()
        db.session.commit()
        return jsonify({'status' : 'All of your groups were deleted'}), 200

    def deleteGroup(_customer, _group_id):
        Group.query.filter_by(customer = _customer, group_id = _group_id).delete()
        db.session.commit()
        return jsonify({'status' : 'Your group was deleted'}), 200

    def checkExist(_customer,_grouplink):
        check = Group.query.filter_by(customer = _customer, group_link = _grouplink).first()
        if check:
            return True, jsonify({'error' : 'Group existed'})
        else:
            return False