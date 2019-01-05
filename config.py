import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    APP_NAME = "DASH"
    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Google OAuth Configs
    GOOGLE_AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
    GOOGLE_TOKEN_URI = "https://accounts.google.com/o/oauth2/token"
    GOOGLE_USER_INFO = "https://www.googleapis.com/userinfo/v2/me"
    GOOGLE_SCOPE = ["profile", "email"]

class ProductionConfig(Config):
    DEBUG = False
    # Google OAuth Authorization
    GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
    GOOGLE_CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]
    GOOGLE_REDIRECT_URI = "https://dash.jahvon.me/auth/gCallback"

class StagingConfig(Config):
    DEBUG = True
    # Google OAuth Authorization
    GOOGLE_CLIENT_ID = os.environ["GOOGLE_CLIENT_ID"]
    GOOGLE_CLIENT_SECRET = os.environ["GOOGLE_CLIENT_SECRET"]
    GOOGLE_REDIRECT_URI = "https://dash-sandbox.jahvon.me/auth/gCallback"

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
