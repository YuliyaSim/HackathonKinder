from flask import Flask
import random

from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = random._urandom(56)
    app.config['DEBUG'] = True

    # Database Connection
    db_info = {'host': 'localhost',
               'database': 'kinder',
               'user': 'Yulelechka',
               'port': ' '}

    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://{db_info['user']}@{db_info['host']}/{db_info['database']}"
    app.config['SQLALCHEMY_TACK_MODIFICATIONS'] = False  # without this line we will receive warnings
    Bootstrap(app)
    return app

app = create_app()

# Database Representation
db = SQLAlchemy(app)  # defines Database from the app
login_manager = LoginManager()
login_manager.init_app(app)
migrate = Migrate(app, db)  # apply all changes inside the app

from app import models
from app import routes