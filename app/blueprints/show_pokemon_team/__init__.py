from flask import Blueprint

show_pokemon_team = Blueprint('show_pokemon_team', __name__)

from . import routes