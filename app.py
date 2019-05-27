import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


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
    return render_template("add_recipe.html")
                           
                           
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT', 4444)),
            debug=True)