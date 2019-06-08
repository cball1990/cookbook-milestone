import os
from flask import Flask, render_template, redirect, request, session, url_for, Blueprint, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_login import LoginManager
from forms import recipeForm
from forms import loginForm
from forms import signupForm
import bcrypt



app = Flask(__name__)
app.config["MONGO_DBNAME"] = "book"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')



mongo = PyMongo(app)

@app.route('/')
@app.route('/login', methods=['POST'])
def login():
    loginform = loginForm()
    users = mongo.db.users
    loginuser = users.find_one({'username' : request.form['username']})
    
    if loginuser:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), loginuser['password'].encode('utf-8')) == loginuser['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('home'))
    
        return render_template("login.html", form = loginform)
    flash('Invalid username/password combination')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    signupform = signupForm()
    if request.method == 'POST':
        users = mongo.db.users
        existingUser = users.find_one({'username' : request.form['username']})
        if existingUser is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'username' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            flash('You are now signed in as' + session['user'])
            return redirect(url_for('home'))
        
        flash('That username already exists') 
    
    return render_template('signup.html', form = signupform)
    
#@app.route('/signup.html', methods=['POSTS')
#def signup_post():
    
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
    
    
@app.route('/home')
def home():
    if 'username' in session:
        return render_template("home.html",
            recipes=mongo.db.recipe.find()) 
    
@app.route('/addrecipe')
def addrecipe():
    form = recipeForm()
    return render_template("add_recipe.html", form = form)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipe
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('home'))
    
@app.route('/recipedetail/<recipe_id>')
def recipedetail(recipe_id):
    the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    ingredient = the_recipe["ingredients"]
    instruction = the_recipe["instructions"]
    allergen = the_recipe["allergens"]
    return render_template("recipedetail.html", recipe=the_recipe, ingredient=ingredient, instructions=instruction, allergens=allergen)
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('home'))
    
                           
                           
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 4444)),
            debug=True)