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
            return render_template('pokemon_selector.html', pokemon_data=pokemon_data, pokemon=pokemon, pokemon_ability=pokemon_ability, pokemon_base_exp=pokemon_base_exp, pokemon_sprites=pokemon_sprites, pokemon_hp=pokemon_hp, pokemon_defense=pokemon_defense, pokemon_attack=pokemon_attack, form=form )
        else:
            flash('Invalid Pokemon')
            return render_template('pokemon_selector.html')
    if request.method == 'POST' and request.form.get('pokemon_name'):
       
        pokemon_name = request.form.get('pokemon_name')
        pokemon_ability = request.form.get('pokemon_ability')
        pokemon_base_exp = request.form.get('pokemon_base_exp')
        pokemon_sprite = request.form.get('pokemon_sprite')

       
        existing_pokemon = PokemonTeam.query.filter_by(name=pokemon_name).first()
        if existing_pokemon:
            
            existing_pokemon.ability = pokemon_ability
            existing_pokemon.base_exp = pokemon_base_exp
            existing_pokemon.sprite = pokemon_sprite
            db.session.commit()
            flash('Pokemon data updated')
        else:
            pokemon_data = PokemonTeam(name=pokemon_name, ability=pokemon_ability, base_exp=pokemon_base_exp, sprite=pokemon_sprite)
            db.session.add(pokemon_data)
            db.session.commit()
            flash('Successfully added Pokemon to Team')

       
        return redirect(url_for('show_pokemon_team.show_pokemon_team'))

    return render_template('pokemon_selector.html', form=form)
