
from app import flask_app
from flask import render_template

@flask_app.route('/')
@flask_app.route('/index')



def index():
    user = {'username':'Adlène'}
    posts = [
        {'author':{'username':'user1'}, 'body':'just testing the app'},
        {'author':{'username':'user2'}, 'body':'working fine here'}
    ]
    return render_template('index.html', title='Home', user = user, posts=posts)
