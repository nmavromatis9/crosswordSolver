from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import flask_login
import os
from pydictionary import Dictionary

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods = ['POST', 'GET'])
def results():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", form=result['crossword'], path=url_for('index'))

def accessDict(word):
    dict=Dictionary("fix")
    print(dict)
    
if __name__ ==  "__main__":
    app.config['DEBUG'] = True
    accessDict("word")
    app.run()