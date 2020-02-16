from secrets import token_hex
import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = token_hex(16)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")

class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SEND_FILE_MAX_AGE_DEFAULT = 0
    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = False

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}