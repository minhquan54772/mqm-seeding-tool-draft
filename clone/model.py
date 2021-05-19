from flask import jsonify
from app import db


class Clone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_id = db.Column(db.String(255), unique=True)
    api_hash = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255))
    phone = db.Column(db.String(255))

    def __init__(self, _id, _api_id, _api_hash, _username, _phone) -> None:
        self.id = _id
        self.api_id = _api_id
        self.api_hash = _api_hash
        self.username = _username
        self.phone = _phone

    def addClone(_id, _api_id, _api_hash, _username, _phone):
        existed = Clone.checkExist(_api_id)
        if existed:
            return jsonify({"error": "Clone account existed"}), 400
        else:
            acc = Clone(_id, int(_api_id), _api_hash, _username, _phone)
            db.session.add(acc)
            db.session.commit()
            return jsonify({"status": "Add clone account successfully"}), 200

    def deleteClone(_api_id):
        Clone.query.filter_by(api_id=_api_id).delete()
        db.session.commit()
        return jsonify({"status": "Clone account was deleted"}), 200

    def deleteAllClone():
        Clone.query.delete()
        db.session.commit()
        return jsonify({"status": "All clone accounts were deleted"}), 200

    def editClone(_id, _api_id, _api_hash, _username, _phone):
        acc = Clone.query.filter_by(id=_id).first()
        acc.api_id = _api_id
        acc.api_hash = _api_hash
        acc.username = _username
        acc.phone = _phone

        db.session.commit()
        return jsonify({"status": "Update clone info successfully"}), 200

    def checkExist(_api_id):
        check = Clone.query.filter_by(api_id=_api_id).first()
        if check:
            return True
        else:
            return False

    def getAllClone():
        all = Clone.query.all()
        return all

    def getCloneWithID(_id):
        clone = Clone.query.filter_by(id=_id).first()
        return clone
