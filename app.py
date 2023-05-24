from flask import Flask
import sys
from flask import *
from flask_bootstrap import Bootstrap
from flask_login import *
import flask_login
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
#from flask_login import current_user, login_user
import os
import re
from nltk.corpus import words
import sqlite3

locate_python = sys.exec_prefix
print(locate_python)

app = Flask(__name__)
Bootstrap(app)

app.secret_key = 'super secret string'  # Change this!
login_manager = flask_login.LoginManager()

login_manager.init_app(app)

@app.route('/', methods = ['POST', 'GET'])
def index():
    return render_template('index.html', path=url_for('index'))

@app.route('/results', methods = ['POST', 'GET'])
def results():
    result = request.form
    l=accessDict(result['crossword'])
    return render_template("result.html", form=l, path=url_for('index'))

@app.route('/about', methods=['GET', 'POST'])
def about():   
    return render_template('about.html', path=url_for('index'))

@app.route('/logins', methods=['GET', 'POST'])
def login():
    try:
        con = sqlite3.connect("DB/login.db")
        cur=con.cursor()
    except:
        print("BAD CONNECTION")
    if request.method == 'GET':
        return render_template("login.html", path=url_for('index'))
    
    name = request.form['email']
    passwo=request.form['password']

    cur.execute("SELECT email from users WHERE (email=? AND password=?)", (name, passwo))
    if cur.fetchone(): 
        user = User()
        user.id = name
        flask_login.login_user(user)
        # return redirect('https://coding.csel.io/user/nima6629/proxy/5000/protected')
        return redirect(url_for('protected'))
        
    return render_template("bad_login.html", path=url_for('index'))

@app.route('/protected')
@flask_login.login_required
def protected():
    print(flask_login.current_user.id)
    return render_template("logged_in.html", usr=flask_login.current_user.id, path=url_for('index'))

@app.route('/logout')
def logout():
    flask_login.logout_user()
    return render_template("logged_out.html", path=url_for('index'))

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template("signup.html", path=url_for('index'))
    
    name = request.form['signupE']
    passwo=request.form['signupP']
    #if email in users and request.form['password'] == users[email]['password']:
    try:
        con = sqlite3.connect("DB/login.db")
        cur=con.cursor()
    except:
        print("BAD CONNECTION")
        
    cur.execute("SELECT email from users WHERE (email=?)", (name,))
    if cur.fetchone(): 
        return "User Already Exists! Try Again"
    else:
        try:
            addUser(name, passwo)
        except Exception as e:
            return str(e)
        return render_template("user_added.html", usr=name, path=url_for('index'))
#Functions################################################################################
def accessDict(text):
    l=[]
    text=text.lower()
    fixedString="^"
    for ch in text:
        if(ch=="*" or ch==" "):
            fixedString=fixedString + ".{1}"
        else:
            fixedString=fixedString+ch
    fixedString+="$"
    
    print(fixedString)
    word_list = words.words()
    word_list=[word.lower() for word in word_list]
    for e in word_list:
        z=re.match(fixedString, e)
        if z:
            l.append(e)
    return l

#Function to add new user to db file
def addUser(name, passw):
    if ((type(name) is not str)):
        raise ValueError
    if ((type(passw) is not str)):
        raise ValueError
    usr = re.match(r'^[a-zA-Z0-9]{1,25}$', name)
    pwd = re.match(r'^[a-zA-Z0-9!@#$%^&*()]{5,25}$', passw)
    if usr == None:
        raise ValueError('Your username name must only contain alphanumeric characters and maximum length is 25 characters, minimum is 1')
    elif pwd == None:
        raise ValueError('Your password must only contain alphanumeric characters or one of the following special characters: !@#$%^&*(). Maximum length is 25 characters, minimum is 5')
    else:
        con = sqlite3.connect("DB/login.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES (?,?);",(name, passw))
        con.commit()
        con.close()
        

################################################################################

#Functions to login. uses many inherited member vars from flask_login module

class User(flask_login.UserMixin):
    pass

@login_manager.user_loader
def user_loader(email2):
    con = sqlite3.connect("DB/login.db")
    cur = con.cursor()
    cur.execute("SELECT email from users WHERE (email=?)", (email2,))
    if not cur.fetchone():
        return

    user = User()
    user.id = email2
    return user

@login_manager.request_loader
def request_loader(request):
    name = request.form.get('email')
    con = sqlite3.connect("DB/login.db")
    cur = con.cursor()
    cur.execute("SELECT email from users WHERE (email=?)", (name,))
    if not cur.fetchone(): 
        return

    user = User()
    user.id = name
    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401

    
if __name__ ==  "__main__":
    app.config['DEBUG'] = True
    app.run()