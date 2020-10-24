from flask_wtf import FlaskForm, Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import  DataRequired, Email



class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired("please enter your name")])
    last_name = StringField('Last Name', validators=[DataRequired("please enter your last name")])
    email = StringField('Email', validators=[DataRequired("please enter a valid email address"), Email("please enter valid email format")])
    password = PasswordField('Password', validators=[DataRequired("Passwords must be 6 chars")])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter your email address.")])
    password = PasswordField('Password', validators=[DataRequired("Please enter a password.")])
    submit = SubmitField("Log in")