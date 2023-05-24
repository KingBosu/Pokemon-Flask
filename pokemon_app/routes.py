from flask import request, render_template
import requests
from pokemon_app.forms import PokemonSelector
from pokemon_app import app


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
