import os

class Config(object):
    SECRET_KEY = 'XMLZODSHE8N6NFOZDPZA2HULWSIYJU45K6N4ZO9M'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProdConfig(Config):
    DEBUG = False

class DevConfig(Config):
    DEBUG = None
