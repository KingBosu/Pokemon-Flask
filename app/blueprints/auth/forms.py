from wtforms import StringField, SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class PokemonSelector(FlaskForm):
    pokemon_name = StringField('Pokemon Name', validators=[DataRequired()])
    search_btn = SubmitField('Search', validators=[DataRequired()])

class LoginForm(FlaskForm):
    identifier= StringField('Username or Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    login_btn = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    register_btn = SubmitField('Register', validators=[DataRequired()])


