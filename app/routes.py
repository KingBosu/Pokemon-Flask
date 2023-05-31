from app import app , db
from flask import request, render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
import requests
from app.blueprints.auth.forms import LoginForm, RegisterForm, PokemonSelector
from app.models import User
from werkzeug.security import check_password_hash



@app.route("/")
def greeting():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/pokemon_selector', methods=['GET', 'POST'])
@login_required
def pokemon_selector():
    form = PokemonSelector()
    if request.method == 'POST':
        pokemon = form.pokemon_name.data
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}'
        response = requests.get(url)
        pokemon_ability = response.json()['abilities'][0]['ability']['name']
        pokemon_base_exp = response.json()['base_experience']
        pokemon_sprites = response.json()['sprites']['front_shiny']
        pokemon_hp = response.json()['stats'][1]['base_stat']
        pokemon_defense = response.json()['stats'][3]['base_stat']
        pokemon_attack = response.json()['stats'][2]['base_stat']
        pokemon_data = {'Name of pokemon': pokemon, 'Pokemon Ability': pokemon_ability, 'Pokemon Base EXP': pokemon_base_exp, 'Pokemon Sprite': pokemon_sprites}
        return render_template('pokemon_selector.html',pokemon_data=pokemon_data,pokemon=pokemon, pokemon_ability=pokemon_ability, pokemon_base_exp=pokemon_base_exp, pokemon_sprites=pokemon_sprites, pokemon_hp=pokemon_hp, pokemon_defense=pokemon_defense, pokemon_attack=pokemon_attack,form=form)
    
    return render_template('pokemon_selector.html',form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username =form.username.data
        password = form.password.data
        user = User.query.filter(User.username == username).first()
        print(user)
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash(f'Hello, {user}! thanks for logging in', 'success')
            return redirect(url_for('home'))
        else:
            return 'Invalid Email or Password'
    else:
        
        return render_template('login.html', form=form)
    
@app.route('/signup', methods=['GET', 'POST'])
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
        return redirect(url_for('login'))
    else:
        return render_template('signup.html', form=form)
    
@app.route('/signout')
def signout():
    logout_user()
    return redirect(url_for('login'))