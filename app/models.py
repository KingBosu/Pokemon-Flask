from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class PokemonCatcher(db.Model):
    """Adds the Pokemon to the User's team"""
    id = db.Column(db.Integer, primary_key=True)
    pokemon_name = db.Column(db.String)
    added_to_team_on = db.Column(db.DateTime, default=datetime.utcnow)


class PokemonTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon_catcher.id'))
    name = db.Column(db.String(255))
    ability = db.Column(db.String)
    sprite = db.Column(db.String)
    base_exp = db.Column(db.Integer)



class User(UserMixin, db.Model):
    """ Adds the user data to the database"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

    def hash_password(self, signup_password):
        return generate_password_hash(signup_password)

    def from_dict(self, user_data):
        """Adds user data for the following fields to the database
         Also hashes the password they input"""
        self.username = user_data['username']
        self.email = user_data['email']
        self.password = self.hash_password(user_data['password'])
