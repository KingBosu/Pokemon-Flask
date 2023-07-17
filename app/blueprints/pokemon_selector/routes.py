from flask import request, render_template, url_for, flash, redirect
from flask_login import login_required, current_user
from .import pokemon_selector
import requests
from app.blueprints.auth.forms import PokemonSelector
from app.models import PokemonTeam
from app import db

@pokemon_selector.route('/pokemon_selector', methods=['GET', 'POST'])
@login_required
def pokemon_selector():
    
    form = PokemonSelector()

    if request.method == 'POST' and form.pokemon_name.data:
        
        pokemon = form.pokemon_name.data
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}'
        response = requests.get(url)

        if response.status_code == 200:
            
            pokemon_ability = response.json()['abilities'][0]['ability']['name']
            pokemon_base_exp = response.json()['base_experience']
            pokemon_sprites = response.json()['sprites']['front_shiny']
            pokemon_hp = response.json()['stats'][1]['base_stat']
            pokemon_defense = response.json()['stats'][3]['base_stat']
            pokemon_attack = response.json()['stats'][2]['base_stat']
            pokemon_data = {
                'pokemon_name': pokemon,
                'pokemon_ability': pokemon_ability,
                'pokemon_base_exp': pokemon_base_exp,
                'pokemon_sprite': pokemon_sprites
            }


             # Pass the API data to the form as hidden fields
            form.pokemon_ability.data = pokemon_ability
            form.pokemon_base_exp.data = pokemon_base_exp
            form.pokemon_sprite.data = pokemon_sprites

            return render_template('pokemon_selector.html', pokemon_data=pokemon_data, pokemon=pokemon, pokemon_ability=pokemon_ability, pokemon_base_exp=pokemon_base_exp, pokemon_sprites=pokemon_sprites, pokemon_hp=pokemon_hp, pokemon_defense=pokemon_defense, pokemon_attack=pokemon_attack, form=form )
        else:
            flash('Invalid Pokemon')
            return render_template('pokemon_selector.html')

    return render_template('pokemon_selector.html', form=form)
