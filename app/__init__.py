""" This module configures and exports the flask application.
"""

from flask import Flask
import os

from .controllers.health import HEALTH
from .controllers.music import MUSIC

APP = Flask(__name__)

# Endpoints
APP.register_blueprint(HEALTH, url_prefix='/health')
APP.register_blueprint(MUSIC, url_prefix='/music')
