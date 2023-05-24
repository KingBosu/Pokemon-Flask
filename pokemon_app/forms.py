from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm

class PokemonSelector(FlaskForm):
    pokemon_name = StringField('Pokemon Name', validators=[DataRequired()])
    search_btn = SubmitField('Search', validators=[DataRequired()])
