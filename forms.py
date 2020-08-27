from flask_wtf import FlaskForm
from wtforms import TextField, SubmitField, SelectField, PasswordField, validators, ValidationError
from datetime import time

class signupForm(FlaskForm):
    username = TextField("Email Address", [validators.Required("Please Provide Your Email Address"), validators.Email("Please Provide Your Email Address")])
    password = PasswordField("Password", [validators.Required("Please Provide Your Password")])
    submit = SubmitField("Sign Up")


select_choices = [('1', 'name'), ('2', 'upvotes')]
class sortfield(FlaskForm):
    sortby = SelectField("Sort By", choices = select_choices)
    submit = SubmitField("Sort")