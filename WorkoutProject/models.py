from WorkoutProject.app import db
class User(db.Model):
    __table_args__ = {'extend_existing' : True}
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, username = "", email = "", password = ""):
        self.password = password
        self.username = username
        self.email = email

