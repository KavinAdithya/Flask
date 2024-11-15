from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return render_template('signin.html')

@auth.route('/signup', methods = ['post'])
def signup_post():
    from app import db
    from WorkoutProject.models import User

    name : str = request.form.get('name')
    email : str = request.form.get('email')
    password : str = request.form.get('password')
    user = User(username=name, email = email, password = password)
    db.session.add(user)
    db.session.commit()
    print (name, email, password)

    return redirect(url_for('main.index'))

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods = ['post'])
def login_post():
    from WorkoutProject.models import  User

    email : str = request.form.get('name')
    password : str = request.form.get('password')
    remember : bool = True if request.form.get('remember') else False

    user = User.query.filter_by(email = email).first()

    if not user or not user.password == password:
        return  redirect('auth.login')

    login_user(user, remember = remember)
    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('logout.html')