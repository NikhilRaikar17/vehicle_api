import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from vehicle.entities.vehicle_entities import ValidVehicle
from vehicle.helpers import vehicle_helpers

def validate_vehicle(brand,description,year_of_manufacture,ready_to_drive):
    """Validates whether the information sent conforms to proper vehicle"""
    try:        
        if not brand:
            raise Exception("Please add a brand name!")

        if not year_of_manufacture:
            raise Exception("Please add year_of_manufacturer!")
        
        if not ready_to_drive:
            raise Exception("Please add a ready to drive!") 

        if len(brand) < 4:
            raise Exception("Brand name is too short")
        
        if (1970 < year_of_manufacture > 2022):
            raise Exception("Year of manufacturer cannot be less than 1970 or greater than 2022!")
        

        if not isinstance(ready_to_drive, bool):
            raise Exception("Ready to drive needs to be a boolean")
        
        return False, None, ValidVehicle(brand,description,year_of_manufacture,ready_to_drive)
    except Exception as e:
        message = e.args[0]
        if message:
            return True, message, None
        return True, "The vehicle could not be added to the database!", None

def add(db,name,brand,description,year_of_manufacture,ready_to_drive):
    """Adds a new vehicle"""
    try:
        is_vehicle = vehicle_helpers.get_vehicle(name,brand,description,year_of_manufacture,ready_to_drive)
        if is_vehicle:
           raise Exception("Vehicle already exists!") 
        
        duplicate_vehicle = vehicle_helpers.get_duplicate_vehicle(name,brand,year_of_manufacture)
        if duplicate_vehicle:
            raise Exception("Same name,brand and manufacture year of vehicle exists")

        error,message,valid_vehicle = validate_vehicle(brand,description,year_of_manufacture,ready_to_drive)
        if error:
            raise Exception(message)

        new_vehicle = vehicle_helpers.create_vehicle(db, valid_vehicle)
        if not new_vehicle:
            raise Exception("Vehicle could not be added into the database")

        return None, "Vehicle successfully added!"
    except Exception as e:
        message = e.args[0]
        if message:
            return True, message
        return True, "The vehicle could not be added to the database!"

def update(db,vehicle_id,name,brand,description,year_of_manufacture,ready_to_drive):
    """Updates a vehicle"""
    try:
        old_vehicle = vehicle_helpers.get_vehicle_by_id(vehicle_id)
        if not old_vehicle:
            raise Exception("Vehicle not found!")
        
        duplicate_vehicle = vehicle_helpers.get_duplicate_vehicle(name,brand,year_of_manufacture)
        if duplicate_vehicle:
            raise Exception("Same name,brand and manufacture year of vehicle exists")
        
        error,message,valid_vehicle = validate_vehicle(db,brand,description,year_of_manufacture,ready_to_drive)
        if error:
            raise Exception(message)
        
        new_vehicle = vehicle_helpers.update_vehicle(db, valid_vehicle, old_vehicle)
        if not new_vehicle:
            raise Exception("Vehicle could not be added into the database")

        return None, "Vehicle successfully updated!"
    except Exception as e:
        message = e.args[0]
        if message:
            return True, message
        return True, "The vehicle could not be added to the database!"
    
