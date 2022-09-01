from flask import jsonify, request
import os
import sys
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

@vehicle_api_blueprint.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    try:
        brand = request.form.get('vehicle_brand')
        description = request.form.get('vehicle_description')
        year_of_manufacture = request.form.get('year_of_manufacture', type=int)
        ready_to_drive = request.form.get('ready_to_drive', type=bool)

        error,message,valid_vehicle = vehicle_service.validate_vehicle(brand,description,year_of_manufacture,ready_to_drive)
        if error:
            raise Exception(message)

        new_vehicle = Vehicle(**vars(valid_vehicle))
        db.session.add(new_vehicle)
        db.session.commit()
        return jsonify({
                        "status": 200,
                        "Error": False,
                        "message":"vehicle successfully created!"
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

