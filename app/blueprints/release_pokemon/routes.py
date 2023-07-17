from flask import Blueprint, redirect, url_for, flash,render_template
from flask_login import login_required
from app.models import PokemonTeam
from app import db
from . import release_pokemon

@release_pokemon.route('/release_pokemon/<int:pokemon_id>', methods=['POST', 'GET'])

@login_required
def release_pokemon(pokemon_id):
    pokemon = PokemonTeam.query.get(pokemon_id)
    if "POST":
        db.session.delete(pokemon)
        db.session.commit()

        flash(f"You've released {pokemon.name} back into the wild!")
    else:
        flash(f"You can't release a Pokemon you haven't caught!")
        render_template('pokemon_team.html')

    return redirect(url_for('show_pokemon_team.show_pokemon_team'))
