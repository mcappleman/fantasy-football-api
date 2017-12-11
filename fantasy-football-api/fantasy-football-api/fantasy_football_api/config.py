"""
Config File
"""

from os import environ, path
BASEDIR = path.abspath(path.dirname(__file__))

class Config(object):
    """Base Config to be inherited from"""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = environ.get('DB_URL', 'postgres://localhost/fantasy_football')


class ProductionConfig(Config):
    """Production Config settings"""
    DEBUG = False;


class StagingConfig(Config):
    """Staging Config settings"""
    DEVELOPMENT = True
    DEBUG = True


class DevConfig(Config):
    """Development Config settings"""
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    """Testing Config settings"""
    TESTING = True
