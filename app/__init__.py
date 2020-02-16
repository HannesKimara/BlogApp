from flask import Flask

from .main import main as main_blueprint
from config import config_options

def create_app(config_name):
    app = Flask(__name__)

    # Loading Configuration Options
    app.config.from_object(config_options[config_name])

    # Registering Blueprints
    app.register_blueprint(main_blueprint)

    return app
