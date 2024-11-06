from flask import Flask, render_template

app = Flask(__name__)

from WorkoutProject.main import main as main_blueprint
app.register_blueprint(main_blueprint)

from WorkoutProject.auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
