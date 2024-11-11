from flask import Blueprint, render_template, request, redirect, url_for

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('signin.html')

@auth.route('/signup', methods = ['post'])
def sign():
    from .app import db
    from WorkoutProject.models import User
    name : str = request.form.get('name')
    email : str = request.form.get('email')
    password : str = request.form.get('password')
    user = User(username=name, email = email, password = password)
    db.session.add(user)
    db.session.commit()
    print (name, email, password)

    return redirect(url_for('main.profile'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods = ['post'])
def log():
    name : str = request.form.get('name')
    password : str = request.form.get('password')

    print(name, password)
    return redirect(url_for('main.profile'))

@auth.route('/logout')
def logout():
    return render_template('logout.html')