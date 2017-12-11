from fantasy_football_api import app, db
from fantasy_football_api.models import BaseModel
from flask_sqlalchemy import SQLAlchemy

class Team(BaseModel, db.Model):
    """Team class to store the different teams"""

    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return '<Team %s, id %s>' % (self.name, self.id)

