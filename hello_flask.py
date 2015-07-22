#!/usr/bin/env python
import pymongo
from flask import Flask, render_template
from pymongo import MongoClient
client = MongoClient()
db = client.tutDbs


# Create the application.
APP = Flask(__name__)

user = {'nickname':'abhinav tripathi'} #fake user
@APP.route('/')
def index():
    
    return render_template('index.html',
        user=user,
        title="Home",
        posts = [{
                'author':'test1',
                'content':'lorem lipsum'
                }]
        )


@APP.route('/hello/')
def hello():
   return render_template('hello.html')

@APP.route('/posts/')
def posts():
    cursor = db.post.find()
    return render_template('posts.html',
        posts = cursor
        )  

if __name__ == '__main__':
    APP.debug=True
    APP.run()

