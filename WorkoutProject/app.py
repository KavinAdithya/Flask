from flask import Flask, render_template
from WorkoutProject.extensions import db
from sqlalchemy import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flaskuser:Kavin%403@localhost/flask_pushup'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

from WorkoutProject.main import main as main_blueprint
app.register_blueprint(main_blueprint)

from WorkoutProject.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

def data_base():
    from WorkoutProject.models import User
    db.create_all()
    print('Table Created...')

if __name__ == '__main__':
    with app.app_context():
        data_base()
        try:
            db.session.execute(text('SELECT 1'))
            print('Data base connected successfully...')
        except Exception as e:
            print(e)
        from sqlalchemy import inspect

        inspector = inspect(db.engine)
        if inspector.has_table('user'):
            print("User table exists!")
        else:
            print("User table does not exist!")

    app.run(debug = True)