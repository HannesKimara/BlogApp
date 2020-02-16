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
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True

class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG = False

class TestConfig(Config):
    '''
    Test configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("TEST_DATABASE_URI")

config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}