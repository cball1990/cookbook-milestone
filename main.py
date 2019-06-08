from flask import Flask, render_template, redirect, request, url_for, Blueprint
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html",
            recipes=mongo.db.recipe.find()) 
    
@main.route('/addrecipe')
def addrecipe():
    form = recipeForm()
    return render_template("add_recipe.html", form = form)

@main.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipe
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('home'))
    
@main.route('/recipedetail/<recipe_id>')
def recipedetail(recipe_id):
    the_recipe =  mongo.db.recipe.find_one({"_id": ObjectId(recipe_id)})
    ingredient = the_recipe["ingredients"]
    instruction = the_recipe["instructions"]
    allergen = the_recipe["allergens"]
    return render_template("recipedetail.html", recipe=the_recipe, ingredient=ingredient, instructions=instruction, allergens=allergen)
    
@main.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('home'))