from flask import Blueprint

release_pokemon = Blueprint('release_pokemon', __name__)

from . import routes