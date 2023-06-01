from . import home
from flask import render_template

@home.route('/')
@home.route('/home')
def home():
    return render_template('home.html')
