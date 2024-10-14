from app import flask_app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {'username':'Adlène'}
    posts = [
        {'author':{'username':'user1'}, 'body':'just testing the app'},
        {'author':{'username':'user2'}, 'body':'working fine here'}
    ]
    return render_template('index.html', title='Home', user = user, posts=posts)


@flask_app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        flash('Login resquested for user {}, remember_me={}'.format(
            login_form.username.data, login_form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', form=login_form)