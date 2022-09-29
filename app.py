from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# APP CONFIG
app = Flask(__name__)
app.secret_key = "SH%07%$b76Q2##@"
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URL") or 'sqlite:///my_database.db'

# DB Init
db = SQLAlchemy(app)

# Login Instance
login = LoginManager(app)
login.login_view = 'login'

import routes, models


db.create_all()