from app import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    address_street = db.Column(db.String(80), nullable=False)
    address_city = db.Column(db.String(80), nullable=False)
    address_country = db.Column(db.String(80), nullable=False)


class Child(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    nickname = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String, nullable=False)
    language = db.Column(db.String, nullable=False)
    activity1 = db.Column(db.String, nullable=False)
    activity2 = db.Column(db.String, nullable=False)
    activity3 = db.Column(db.String, nullable=False)


class Activity(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    activity = db.Column(db.String, nullable=False)
    business = db.Column(db.String, nullable=False)
    business_link = db.Column(db.String, nullable=False)
