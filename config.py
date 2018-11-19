import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    APP_NAME = "DASH"
    SECRET_KEY = os.environ['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Google OAuth Authorization
    CLIENT_ID = os.environ['CLIENT_ID']
    CLIENT_SECRET = os.environ['CLIENT_SECRET']
    AUTH_URI = 'https://accounts.google.com/o/oauth2/auth'
    TOKEN_URI = 'https://accounts.google.com/o/oauth2/token'
    USER_INFO = 'https://www.googleapis.com/userinfo/v2/me'
    SCOPE = ['profile', 'email']

class ProductionConfig(Config):
    DEBUG = False
    # OAuth Authorization
    REDIRECT_URI = 'https://dash.jahvon.me/auth/gCallback'

class SandboxConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # OAuth Authorization
    REDIRECT_URI = 'https://dash-sandbox.jahvon.me/auth/gCallback'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    # OAuth Authorization
    REDIRECT_URI = 'https://localhost:5000/auth/gCallback'

class TestingConfig(Config):
    TESTING = True
