from datetime import datetime

from flask_login import UserMixin


from app import db
class User(db.Model, UserMixin):

    __table_args__ = {'extend_existing' : True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))
    workouts = db.relationship('Workouts', backref = 'user', lazy = True)

    def __init__(self, username = "", email = "", password = ""):
        self.password = password
        self.username = username
        self.email = email

class Workouts(db.Model):

    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable = False)
    comment = db.Column(db.Text, nullable =  False)
    date_time = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __init__(self, user_id , count , comment, date_time):
        self.count  = count
        self.user_id = user_id
        self.comment = comment
        self.date_time = date_time if date_time else datetime.utcnow()

