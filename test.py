from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import flask_login
import os
import nltk
from nltk.corpus import words
import re

def main():
    accessDict("*a*ch** ")
    
def accessDict(text):
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
            print(e)

if __name__ ==  "__main__":
    main()