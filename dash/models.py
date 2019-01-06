from datetime import datetime, timedelta

from dash import app
from dash.helpers import Admin
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    avatar = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    last_login = db.Column(db.DateTime)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def __init__(self, username, password, email):
        self.username = username
        self.set_password(password)
        self.email = email

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def login(self):
        self.last_login = datetime.utcnow()
        return self

    def get_id(self):
        return self.id

    @property
    def is_active(self):
        return self.active

    @property
    def is_authenticated(self):
        now = datetime.utcnow()
        return now-timedelta(hours=24) <= self.last_login <= now
    
    @property
    def is_anonymous(self):
        return not self.is_authenticated
    
    @property
    def is_admin(self):
        return Admin.is_admin(self.email)
