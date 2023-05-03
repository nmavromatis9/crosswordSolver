from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import flask_login
import os
from nltk.corpus import words
import re

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST', 'GET'])
def results():
    if request.method == 'POST':
        result = request.form
        l=accessDict(result['crossword'])
        return render_template("result.html", form=l, path=url_for('index'))

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
    
if __name__ ==  "__main__":
    app.config['DEBUG'] = True
    app.run()