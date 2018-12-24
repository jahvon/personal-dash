from datetime import datetime, timedelta

from dash import app
from dash.helpers import Admin
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=True)
    avatar = db.Column(db.String(200))
    active = db.Column(db.Boolean, default=True)
    tokens = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    last_login = db.Column(db.DateTime)

    def __repr__(self):
        return '<Google User %r>' % self.email

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

# class FInancialTransaction(db.Model):
#     __tablename__ = 'financial_transaction'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     amount = db.Column(db.Float, nullable=False)
#     threshold = db.Column(db.Float, nullable=False)

# class SavingGoal(db.Model):
#     __tablename__ = 'saving_goals'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     amount = db.Column(db.Float, nullable=False)
#     threshold = db.Column(db.Float, nullable=False)

# class Budget(db.Model):
#     __tablename__ = 'saving_goals'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     amount = db.Column(db.Float, nullable=False)
