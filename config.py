""" Configurations for local development and production """

class Config:
    """ Standard configurations """
    DEBUG = False

class DevelopmentConfig(Config):
    """ Configuration for local development """
    FLASK_PORT = 5000
    FLASK_HOST = '0.0.0.0'

class ProductionConfig(Config):
    """ Configuration for production """

class TestConfig(Config):
    """ Configuration for production """
    DEBUG = True
    FLASK_PORT = 5000
    FLASK_HOST = '0.0.0.0'

