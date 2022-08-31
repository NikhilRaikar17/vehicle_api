from flask import Blueprint

vehicle_api_blueprint = Blueprint('vehicle_api', __name__)

from . import routes
