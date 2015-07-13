#!/usr/bin/env python

from flask import Flask, render_template


# Create the application.
APP = Flask(__name__)


@APP.route('/')
def index():
    user = {'nickname':'abhinav tripathi'} #fake user
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
    """ Displays the page greats who ever comes to visit it.
    """
    return render_template('hello.html')

if __name__ == '__main__':
    APP.debug=True
    APP.run()

