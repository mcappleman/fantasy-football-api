
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request_finished

class BaseController(object):
    """Base Controller to be extended by every other controller"""
    def __init__(self, *args):
        super().__init(self, *args)
