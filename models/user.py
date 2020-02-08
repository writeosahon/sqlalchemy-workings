""" File module definitions for User flask-sqlalchemy database model """

__version__ = '0.1 (2020-02-08)'
__author__ = 'OSAHON OKUNGBOWA'

import flask_sqlalchemy as fsql

flask_app = None
flask_database = None

def config(app, database):
    global flask_app, flask_database
    flask_app = app
    flask_database = database


class User(flask_database.Model):
    __tablename__ = "users"
    id = flask_database.Column(flask_database.Integer, primary_key=True)
    username = flask_database.Column(flask_database.String(64), unique=True, index=True)
