from flask import jsonify
from . import vehicle_api_blueprint


@vehicle_api_blueprint.route('/', methods=['GET'])
def status():
    return jsonify({'status':"Active!"})
