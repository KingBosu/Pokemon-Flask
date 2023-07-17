from flask import request, render_template, url_for, flash, redirect
from flask_login import login_required, current_user
from .import pokemon_catcher
import requests
from app.blueprints.auth.forms import PokemonSelector
from app.models import PokemonTeam
from app import db


@pokemon_catcher.route('/catch_pokemon' , methods =['POST'])
@login_required
def catch_pokemon():
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