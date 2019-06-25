import os
from flask import Flask, render_template, redirect, request, session, url_for, Blueprint, flash
from flask_pymongo import PyMongo
from pymongo import ReturnDocument 
from bson.objectid import ObjectId
from flask_login import LoginManager
from forms import recipeForm
from forms import loginForm
from forms import signupForm
from forms import editRecipeForm
import bcrypt



app = Flask(__name__)
app.config["MONGO_DBNAME"] = "book"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')
app.secret_key = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')



mongo = PyMongo(app)

@app.route('/')

    
@app.route('/login', methods=['POST', 'GET'])
def login():
    loginform = loginForm()
    if request.method == 'POST':
        users = mongo.db.users
        loginuser = users.find_one({'username' : request.form['username']})
        
        if loginuser:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), loginuser['password']) == loginuser['password']:
                session['username'] = request.form['username']
                return redirect(url_for('home'))
            else: flash('Invalid username/password combination')
            
        if session.get('username'):
             return redirect(url_for('home'))
    return render_template("login.html", form = loginform)


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
            return redirect(url_for('home'))
        
        flash('That username already exists') 
    
    return render_template('signup.html', form = signupform)
    
    
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
    form.upvotes.data = 0
    return render_template("add_recipe.html", form = form)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipe
    dict_values = request.form.to_dict()
    dict_values['upvotes'] = 1
    recipes.insert_one(dict_values)
    return redirect(url_for('home'))
    
@app.route('/recipedetail/<recipe_id>')
def recipedetail(recipe_id):
    the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    return render_template("recipedetail.html", recipe=the_recipe)

@app.route('/upvote/<recipe_id>', methods=['POST'])
def upvote(recipe_id):
    the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    the_recipe.update({'$inc': {'upvotes': 1}})
    return render_template("recipedetail.html", recipe=the_recipe)
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('home'))
    
@app.route('/editrecipe/<recipe_id>')
def editrecipe(recipe_id):
     edit_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
     form = editRecipeForm()
     form.upvotes.data = 0
     return render_template('editrecipe.html', recipe = edit_recipe,
                           form = form)
                           
@app.route('/updaterecipe/<recipe_id>', methods=['POST'])
def updaterecipe(recipe_id):
    if request.method == 'POST':
        updateRecipe = mongo.db.recipe
        updateRecipe.update( 
        {"_id": ObjectId(recipe_id)},   
            {'name':request.form.get('name'),
            'img':request.form.get('img'),
            'author': request.form.get('author'),
            'cuisine': request.form.get('cuisine'),
            'date_added':request.form.get('date_added'),
            'time_taken':request.form.get('time_taken'),
            'desc':request.form.get('desc'),
            'ingredients':request.form.get('ingredients'),
            'instructions':request.form.get('instruction'),
            'allergens':request.form.get('allergens')}
        )
        return redirect(url_for('home'))
                           
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 4444)),
            debug=True)