from flask import Flask
from config import Config
from flask_login import LoginManager, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



login_manager = LoginManager()
db = SQLAlchemy()
migrate =Migrate()



def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    login_manager.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)

    from app.blueprints.home import home
    from app.blueprints.pokemon_selector import pokemon_selector
    from app.blueprints.auth import auth
    from app.blueprints.show_pokemon_team import show_pokemon_team

    app.register_blueprint(home)
    app.register_blueprint(pokemon_selector)
    app.register_blueprint(auth)
    app.register_blueprint(show_pokemon_team)

    return app
    
from app import models