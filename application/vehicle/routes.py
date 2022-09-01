from flask import jsonify
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from application.vehicle import vehicle_api_blueprint


@vehicle_api_blueprint.route('/status', methods=['GET'])
def status():
    return jsonify({'status':"Active!"})
