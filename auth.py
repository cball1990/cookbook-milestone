from flask import Flask, render_template, redirect, request, url_for, Blueprint

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template("login.html")
    

    
#@auth.route('/login', methods=['POST'])
 #   def login_post():
 
@auth.route('/signup')
def signup():
    return render_template('signup.html')
    
#@auth.route('/signup.html', methods=['POSTS')
#def signup_post():
    
@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))