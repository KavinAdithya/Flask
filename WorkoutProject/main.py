from flask import Blueprint, render_template
from flask_login import login_required, current_user


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profiles.html', name = current_user.username)

@main.route('/addpushup')
@login_required
def addpushup():
    return render_template("add_pushup.html")

@main.route('/listworkouts')
@login_required
def workouts():
    return render_template("workouts.html")