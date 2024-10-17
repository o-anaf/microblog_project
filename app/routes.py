from app import flask_app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm

from flask_login import current_user, login_user
import sqlalchemy as sa
from app import db
from app.models import User


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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == login_form.username.data))
        if user is None or not user.check_password(login_form.password.data)
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user, remember=login_form.remember_me.data)
    return render_template('login.html', title='Sign In' form=login_form)