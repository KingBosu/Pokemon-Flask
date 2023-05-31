from flask import Blueprint

pokemon_selector = Blueprint('pokemon_selector',__name__)

from .import routes

