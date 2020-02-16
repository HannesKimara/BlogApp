from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .main import main as main_blueprint
from config import config_options

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    # Loading Configuration Options
    app.config.from_object(config_options[config_name])

    # Initialize Extensions
    db.init_app(app)
    
    # Registering Blueprints
    app.register_blueprint(main_blueprint)

    return app
