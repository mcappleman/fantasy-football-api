"""
The flask application package.
"""

from os import environ
from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object(environ.get('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import fantasy_football_api.views
from fantasy_football_api.controllers import TeamController

