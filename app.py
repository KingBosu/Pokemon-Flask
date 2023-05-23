from flask import Flask, request, render_template
import requests

app = Flask(__name__)


@app.route("/")
def greeting():
    return "<h1>Welcome to the page!</h1>"


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/main', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
    
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}'
        response = requests.get(url)
        pokemon_ability = response.json()['abilities'][0]['ability']['name']
        pokemon_base_exp = response.json()['base_experience']
        pokemon_sprites = response.json()['sprites']['front_shiny']
        pokemon_data = {'Name of pokemon': pokemon, 'Pokemon Ability': pokemon_ability, 'Pokemon Base EXP': pokemon_base_exp, 'Pokemon Sprite': pokemon_sprites}
        return render_template('main.html',pokemon_data=pokemon_data,pokemon=pokemon, pokemon_ability=pokemon_ability, pokemon_base_exp=pokemon_base_exp, pokemon_sprites=pokemon_sprites)
    
    return render_template('main.html')

