from flask import Blueprint, render_template

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('home.html')

@main.route('/profile')
def profile():
    return render_template('profiles.html')