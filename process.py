import sys
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

def main():
    finSearch('chi**')

def finSearch(text):
    with open("goodWords.txt", "r") as g:
        words=[lin.strip() for lin in g]  
    text=text.lower()
    fixedString="^"
    for ch in text:
        if(ch=="*" or ch==" "):
            fixedString=fixedString + ".{1}"
        else:
            fixedString=fixedString+ch
    fixedString+="$"
    for w in words:
        z=re.match(fixedString, w)
        if z:
            print(w)

    
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
    print(word_list)
    word_list=[word.lower() for word in word_list]
    for e in word_list:
        z=re.match(fixedString, e)
        if z:
            print(e)

def accessText(text):
    text=text.lower()
    l=[]
    f=open("goodWords.txt", "w")
    with open('words.txt', 'r') as filestream:
        w=filestream.readline().split(', ')
        l=[x.replace('\'', '') for x in w]
        l=[x.replace('[', '') for x in l]
        l=[x.replace(']', '') for x in l]
    for i in l:
        f.write(i+'\n')

    with open("goodWords.txt", "r") as g:
        words=[line.strip() for line in g]

    
def makeData():
    word_list = words.words()
    new_list=[]
    for w in word_list:
        w=str.lower(w)
        new_list.append(w)

    file = open('words.txt','w')
    file.write(str((new_list)))

if __name__ ==  "__main__":
    main()