from flask import render_template
from flask_login import login_required, current_user
from models import PokemonTeam
from . import show_pokemon_team

@show_pokemon_team.route('/pokemon_team')
@login_required
def show_pokemon_team():

    PokemonTeam.query()

    return render_template('pokemon_team.html')
