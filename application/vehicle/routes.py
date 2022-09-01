from flask import jsonify, request
import os
import sys
import json
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from application.vehicle import vehicle_api_blueprint
from application.models import Vehicle
from application.vehicle.service import vehicle_service
from flask_sqlalchemy import SQLAlchemy
from application import create_app,db

app = create_app()
db = SQLAlchemy(app)


@vehicle_api_blueprint.route('/status', methods=['GET'])
def status():
    """Checks whether the route is active"""
    return jsonify({'status':"Active!"})

@vehicle_api_blueprint.route('/vehicle', methods=['POST'])
def add_vehicle():
    """Adds a new vehicle"""
    try:
        name = request.form.get('vehicle_name')
        brand = request.form.get('vehicle_brand')
        description = request.form.get('vehicle_description')
        year_of_manufacture = request.form.get('year_of_manufacture', type=int)
        ready_to_drive = request.form.get('ready_to_drive', type=bool)

        error,message = vehicle_service.add(db,name,brand,description,year_of_manufacture,ready_to_drive)
        if error:
            raise Exception(message)

        return jsonify({
                        "status": 200,
                        "Error": False,
                        "message":message
                        })

    except Exception as e:
        message = e.args[0]
        db.session.rollback()
        db.session.flush()
        if message:
            return jsonify({
                    "status": 500,
                    "Error": True,
                    "message": message
                    })
        return jsonify({
                    "status": 500,
                    "Error": True,
                    "message":"Vehicle could not be created!"
                    })

@vehicle_api_blueprint.route('/vehicle/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    """Update vehicle details by vehicle identification number"""
    try:
        name = request.form.get('vehicle_name')
        brand = request.form.get('vehicle_brand')
        description = request.form.get('vehicle_description')
        year_of_manufacture = request.form.get('year_of_manufacture', type=int)
        ready_to_drive = request.form.get('ready_to_drive', type=bool)

        error,message = vehicle_service.update(db,vehicle_id,name,brand,description,year_of_manufacture,ready_to_drive)
        if error:
            raise Exception(message)

        return jsonify({
                        "status": 200,
                        "Error": False,
                        "message":"vehicle successfully updated!"
                        })

    except Exception as e:
        db.session.rollback()
        db.session.flush()
        message = e.args[0]
        if message:
            return jsonify({
                    "status": 500,
                    "Error": True,
                    "message":message
                    })
        return jsonify({
                "status": 500,
                "Error": True,
                "message":"Vehicle could not be updated!"
                })

@vehicle_api_blueprint.route('/vehicles', methods=['GET'])
def get_all_vehicles():
    """Gets all the vehicle information present"""
    all_vehicles = vehicle_service.get_vehicles()
    return json.dumps(Vehicle.serialize_list(all_vehicles))

@vehicle_api_blueprint.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_specific_vehicles(vehicle_id):
    """Gets single vehicle information """
    vehicle = vehicle_service.get_vehicle(vehicle_id)
    return json.dumps(Vehicle.serialize_list(vehicle))

@vehicle_api_blueprint.route('/search', methods=['GET'])
def search_vehicles():
    try:
        name = request.args.get('vehicle_name', default='').strip()
        brand = request.args.getlist('vehicle_brand')
        year_of_manufacture = request.args.getlist('year_of_manufacture', type=int)
        ready_to_drive = request.form.get('ready_to_drive', type=bool, default=False)

        error,message,vehicles = vehicle_service.search(name,brand,year_of_manufacture,ready_to_drive)
        if error:
            raise Exception(message)

        return json.dumps(Vehicle.serialize_list(vehicles.all()))


    except Exception as e:
        message = e.args[0]
        if message:
            return message
        return "Search functionality not working"