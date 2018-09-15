from rami import db
from datetime import datetime

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255))
    creation_date = db.Column(db.DateTime)


    def __init__(self, message):
        self.message = message
        self.creation_date = datetime.utcnow()


class Forms(db.Model):
    __tablename__ = 'forms'
    id = db.Column(db.Integer, primary_key=True)
    formtype = db.Column(db.String(20))