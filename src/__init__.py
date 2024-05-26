from flask import Flask
from flask_session import Session
import os


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_prefixed_env()
    app.config.from_pyfile('config.py', silent=True)

    app.config['SECRET_KEY'] = os.urandom(64)
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_FILE_DIR'] = './.flask_session/'

    Session(app)

    from .views.routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    return app
