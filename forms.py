from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, IntegerField, SelectField, DateField, PasswordField
from wtforms import validators, ValidationError
from datetime import time

class recipeForm(FlaskForm):
    name = TextField("Recipe Name",[validators.Required("Please enter The Recipe Name.")])
    img = TextField("Recipe Image",[validators.Required("Please enter A Valid URL."), validators.URL("Please enter A Valid URL.")])
    author = TextField("Author's Name",[validators.Required("Please enter The Recipe Creators Name.")])
    cuisine = TextField("Cusine Type",[validators.Required("Please enter The Cuisine Category")])
    time_taken = TextField("Cooking Time",[validators.Required("Please enter The Length Of Time It Take To Make The Recipe.")])
    date_added = TextField("Date Added",[validators.Required("Please enter Todays Date In The Format dd/mm/yyyy.")])
    desc = TextAreaField("Description",[validators.Required("Please enter A Description For The Recipe.")])
    ingredients = TextAreaField("List Of Ingredients",[validators.Required("Please enter The Ingredients Needed For The Recipe.")])
    instructions = TextAreaField("Recipe Instructions",[validators.Required("Please enter The Instructions For The Recipe.")])
    allergens = TextAreaField("Allergens")
    upvotes = IntegerField("Upvotes")
    submit = SubmitField("Send")
    
class signupForm(FlaskForm):
    username = TextField("Email Address", [validators.Required("Please Provide Your Email Address"), validators.Email("Please Provide Your Email Address")])
    password = PasswordField("Password", [validators.Required("Please Provide Your Password")])
    submit = SubmitField("Sign Up")


select_choices = [('1', 'name'), ('2', 'upvotes')]
class sortfield(FlaskForm):
    sortby = SelectField("Sort By", choices = select_choices)
    submit = SubmitField("Sort")