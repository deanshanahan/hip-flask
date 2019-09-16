""" This module starts the Flask server. """

import sys, os
import config
from app import APP

if __name__ == '__main__':
    """ Setup environment and execute the flask application
    """

    # If no environment is provided, assume 'dev' environment
    ENV = sys.argv[1] if len(sys.argv) > 2 else 'dev'

    # Local development settings
    if ENV == 'dev':
        Config = config.DevelopmentConfig
        port = Config.FLASK_PORT
        host = Config.FLASK_HOST
        debug = Config.DEBUG

    # Production server settings
    elif ENV == 'prod':
        Config = config.ProductionConfig
        port = os.environ.get('FLASK_PORT') # These should be set as system variables
        host = os.environ.get('FLASK_HOST') # These should be set as system variables
        debug = Config.DEBUG

    # Local test settings
    elif ENV == 'test':
        Config = config.TestConfig
        port = Config.FLASK_PORT
        host = Config.FLASK_HOST
        debug = Config.DEBUG

    else:
        raise ValueError('Invalid enviroment name provided')

    # Start the application
    APP.run(host=host, port=int(port), debug=debug)
