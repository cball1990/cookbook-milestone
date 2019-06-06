import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from forms import recipeForm



app = Flask(__name__)
app.config["MONGO_DBNAME"] = "book"
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)



@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html",
            recipes=mongo.db.recipe.find()) 
    
@app.route('/addrecipe')
def addrecipe():
    form = recipeForm()
    return render_template("add_recipe.html", form = form)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes =  mongo.db.recipe
    instructions = instruction.split(".  ")
    recipes.insert_one(request.form.to_dict(instructions))
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