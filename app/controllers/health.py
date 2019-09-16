""" Responds healthy if the service is healthy.
"""

import json
from flask import Blueprint
from flask import Response

HEALTH = Blueprint('health', __name__)

@HEALTH.route('', methods=['GET'])
def health():
    """ Return statement stating the service is healthy if the service
    is running. """
    return Response("{'status':'healthy'}", status=200, mimetype='application/json')
