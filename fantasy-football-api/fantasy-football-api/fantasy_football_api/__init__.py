"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import fantasy_football_api.views
