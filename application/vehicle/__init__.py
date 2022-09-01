from flask import Blueprint
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

vehicle_api_blueprint = Blueprint('vehicle_api', __name__)
from application.vehicle import routes
