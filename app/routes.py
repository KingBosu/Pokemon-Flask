from flask import request, render_template
import requests
from app.forms import PokemonSelector
from app import app
from app.forms import LoginForm
from app.forms import RegisterForm


@app.route("/")
def greeting():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/main', methods=['GET', 'POST'])
def main():
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
        return render_template('main.html',pokemon_data=pokemon_data,pokemon=pokemon, pokemon_ability=pokemon_ability, pokemon_base_exp=pokemon_base_exp, pokemon_sprites=pokemon_sprites, pokemon_hp=pokemon_hp, pokemon_defense=pokemon_defense, pokemon_attack=pokemon_attack,form=form)
    
    return render_template('main.html',form=form)


REGISTERED_USERS ={
    'Kingbosu':{
        'email':'William@thieves.com',
        'password':'password'
    }
}
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        username =form.username.data
        password = form.password.data
        if username in REGISTERED_USERS and REGISTERED_USERS[username]['password'] == password:
            return f'Hello, {username}! thanks for logging in'
        else:
            return 'Invalid Email or Password'
    else:
        print('Not Valid')
        return render_template('login.html', form=form)
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if request.method == 'POST' and form.validate_on_submit():
        
        username = form.username.data
        email = form.email.data.lower()
        password = form.password.data
        REGISTERED_USERS[username] = {
            'email':email,
            'password':password
        }
        return f'Welcome, {username}! thanks for signing up!'
    else:
        return render_template('signup.html', form=form)