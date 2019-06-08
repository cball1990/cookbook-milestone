

@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    print(request.form['username'])
    loginuser = users.find_one({'username' : request.form['username']})
    if loginuser:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'), loginuser['password'].encode('utf-8')) == loginuser['password'].encode('utf-8'):
            session['username'] = request.form['username']
            return redirect(url_for('home'))
    
    flash('Invalid username/password combination')
    
     <form action="{{ url_for('login') }}" class="login-form" method=p ost>
                <p><input type="text" name="username"/></p>
                <p><input type="password" name="password"/></p>
                <p><input type="submit" value="Login"/></p>
                <p class="detail-minor-data">Dont have an account? Sign up <a href="{{ url_for('signup')}}">Here</a></p>
            </form>