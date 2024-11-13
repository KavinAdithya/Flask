from datetime import datetime
from flask import Blueprint, render_template, request, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import redirect



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
def add_push_up():
    return render_template("add_pushup.html")

@main.route('/addpushup', methods = ['POST'])
@login_required
def add_push_up_post():
    from WorkoutProject.models import Workouts
    from app import db

    count: int = int(request.form.get('count'))
    comment: str = request.form.get('comment')
    date_time: datetime = datetime.strptime(request.form.get('datetime'), '%Y-%m-%dT%H:%M')
    # date_time = request.form.get('datetime')
    print('Count : ', count)
    print('Comment : ', comment)
    print('Date Time : ', date_time)

    work_out: Workouts = Workouts(count=count, comment=comment, date_time=date_time, user_id=current_user.id)
    db.session.add(work_out)
    db.session.commit()

    flash(current_user.username + " New Workout Added Successfully...", 'success')

    return redirect(url_for('main.workouts', page = 1))

@main.route('/listworkouts')
@login_required
def workouts():
    from WorkoutProject.models import  Workouts

    page = request.args.get('page', 1, type = int)
    per_page = 1

    name = Workouts.query.paginate(page = page, per_page = per_page)
    return render_template("workouts.html", name = name)

@main.route('/update_push_up/<int:workout_id>/update', methods = ['GET', 'POST'])
@login_required
def update_push_up(workout_id):
    from WorkoutProject.models import Workouts
    from app import db

    if request.method == 'POST':
        count : int = int(request.form.get('count'))
        comment : str = request.form.get('comment')
        date_time : datetime = datetime.strptime(request.form.get('datetime'), '%Y-%m-%dT%H:%M')

        workouts = Workouts.query.get(workout_id)
        workouts.count = count
        workouts.comment = comment
        workouts.date_time = date_time
        db.session.commit()

        flash('You Workout Has Been Updated !')
        return redirect(url_for('main.workouts',page = 1))
    return render_template('updateworkout.html', workout_id = workout_id)

@main.route('/delete/<int:workout_id>/delete_workout')
@login_required
def delete_workout(workout_id):
    from WorkoutProject.models import Workouts
    from app import db
    workout = Workouts.query.get(workout_id)
    db.session.delete(workout)
    db.session.commit()

    flash('Your Workour has been deleted successfully...', 'danger')
    return redirect(url_for('main.workouts', page = 1))