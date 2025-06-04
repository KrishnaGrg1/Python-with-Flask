from flask import Flask,request,redirect,url_for,session,Response

app=Flask(__name__)
app.secret_key="secretkey"

@app.route('/', methods=["GET","POST"])
def login():
    if request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        
        if username== "admin" and password=="123":
            session["user"]=username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid crendtials. Try again",mimetype="text/plain")
    
    return '''
    <html>
        <body>
            <h1>Login Page</h1>
            <form method="Post"/>
                Username: <input type="text" name="username"/> <br>
                Password: <input type="password" name="password"/> <br>
                <input type="submit" value="Login" />
            </form>
        </body>
    </html>
'''


@app.route('/welcome', methods=["POST","GET"])
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome ,{session['user']}!</h2>
        <a href={url_for('logout')}>Logout </a>
    '''
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop("user")
    return redirect(url_for("login")) 