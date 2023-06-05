from flask import request, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from app.blueprints.auth.forms import LoginForm, RegisterForm
from app.models import User
from werkzeug.security import check_password_hash
from app import db


@auth.route('/login', methods=['GET', 'POST'])

def login():
    
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        identifier = form.identifier.data
        password = form.password.data
        user = User.query.filter((User.username == identifier) | (User.email == identifier)).first()


        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f'Hello, {user.username}! thanks for logging in', 'success')
            return redirect(url_for('home.home'))
        else:
            return 'Invalid  Username or Email or Password'
    else:
        
        return render_template('login.html', form=form)
    
@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        user = User()
        username = form.username.data
        email = form.email.data.lower()
        password = form.password.data
        user_data = {'username':username,'email':email, 'password':password}
        user.from_dict(user_data)
        db.session.add(user)
        db.session.commit()
        flash(f'Welcome, {username}! thanks for signing up!', 'success')
        return redirect(url_for('auth.login'))
    else:
        return render_template('signup.html', form=form)
    
@auth.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('auth.login'))