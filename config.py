import os
from os import environ

class config(object):

    DEBUG=False
    TESTING= False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = "professor"

    UPLOADS= "/home/username/app/app/static/uploads"

    SESSION_COOKIE_SECURE =True

    DEFAULT_THEME =None


class DevelopmentConfig(config):
    DEBUG=True    
    SESSION_COOKIE_SECURE =True


class DebugConfig(Config):
    DEBUG = False
    