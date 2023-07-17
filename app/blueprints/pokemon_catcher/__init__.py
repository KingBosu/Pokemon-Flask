from flask import Blueprint

pokemon_catcher = Blueprint('pokemon_catcher', __name__)

from . import routes