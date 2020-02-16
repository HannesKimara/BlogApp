from secrets import token_hex

class Config:
    SECRET_KEY = token_hex(16)

class DevConfig(Config):
    SEND_FILE_MAX_AGE_DEFAULT = 0
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False

config_options = {
    'development': DevConfig,
    'production': ProdConfig
}