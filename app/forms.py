from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import InputRequired, Length, data_required, Email


class RegisterForm(FlaskForm):
    first_name = StringField('First Name:', validators=[data_required(), Length(min=4, max=20)])
    last_name = StringField('Last Name:', validators=[data_required(), Length(min=4, max=20)])
    username = StringField('Username:', validators=[data_required()])
    email = StringField('Email:', validators=[data_required(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password:', validators=[data_required()])
    address_street = StringField('Street:', validators=[data_required(), Length(min=4, max=20)])
    address_city = StringField('City:', validators=[data_required(), Length(min=4, max=20)])
    address_country = StringField('Country:', validators=[data_required(), Length(min=4, max=20)])


class AddChild(FlaskForm):
    nickname = StringField('Nickname:', validators=[data_required(), Length(min=4, max=20)])
    age = IntegerField('Age:', validators=[data_required()])
    gender = StringField('Gender:', validators=[data_required()])
    language = StringField('Language:', validators=[data_required(), Length(min=4, max=20)])
    activity1 = StringField('Activity:', validators=[data_required(), Length(min=4, max=20)])
    activity2 = StringField('Activity:', validators=[data_required(), Length(min=4, max=20)])
    activity3 = StringField('Activity:', validators=[data_required(), Length(min=4, max=20)])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[data_required(), Length(min=4, max=20)])
    password = PasswordField('Password', validators=[data_required()])