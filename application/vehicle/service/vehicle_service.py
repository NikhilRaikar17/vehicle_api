from vehicle.helpers import vehicle_helpers
from vehicle.entities.vehicle_entities import ValidVehicle
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


def validate_vehicle_info(name, brand, description, year_of_manufacture, ready_to_drive):
    """Validates whether the information sent conforms to proper vehicle"""
    try:
        if not name:
            raise Exception("Please add a vehicle name!")

        if not brand:
            raise Exception("Please add a brand name!")

        if not year_of_manufacture:
            raise Exception("Please add year_of_manufacturer!")

        if not ready_to_drive:
            raise Exception("Please add a ready to drive!")

        if len(brand) < 4:
            raise Exception("Brand name is too short")

        if (1970 < year_of_manufacture > 2022):
            raise Exception(
                "Year of manufacturer cannot be less than 1970 or greater than 2022!")

        if not isinstance(ready_to_drive, bool):
            raise Exception("Ready to drive needs to be a boolean")

        return False, None, ValidVehicle(name, brand, description, year_of_manufacture, ready_to_drive)
    except Exception as e:
        message = e.args[0]
        if message:
            return True, message, None
        return True, "The vehicle could not be added to the database!", None


def add(db, name, brand, description, year_of_manufacture, ready_to_drive):
    """Adds a new vehicle"""
    try:
        is_vehicle = vehicle_helpers.get_vehicle(
            name, brand, description, year_of_manufacture, ready_to_drive)
        if is_vehicle:
            raise Exception("Vehicle already exists!")

        duplicate_vehicle = vehicle_helpers.get_duplicate_vehicle(
            name, brand, year_of_manufacture)
        if duplicate_vehicle:
            raise Exception(
                "Same name,brand and manufacture year of vehicle exists")

        error, message, valid_vehicle = validate_vehicle_info(
            name, brand, description, year_of_manufacture, ready_to_drive)
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


def update(db, vehicle_id, name, brand, description, year_of_manufacture, ready_to_drive):
    """Updates a vehicle"""
    try:
        old_vehicle = vehicle_helpers.get_vehicle_by_id(vehicle_id)
        if not old_vehicle:
            raise Exception("Vehicle not found!")

        duplicate_vehicle = vehicle_helpers.get_duplicate_vehicle(
            vehicle_id, name, brand, year_of_manufacture)
        if duplicate_vehicle:
            raise Exception(
                "Same name,brand and manufacture year of vehicle exists")

        error, message, valid_vehicle = validate_vehicle_info(
            name, brand, description, year_of_manufacture, ready_to_drive)
        if error:
            raise Exception(message)

        new_vehicle = vehicle_helpers.update_vehicle(
            db, valid_vehicle, old_vehicle)
        if not new_vehicle:
            raise Exception("Vehicle could not be added into the database")

        return None, "Vehicle successfully updated!"
    except Exception as e:
        print(e)
        message = e.args[0]
        if message:
            return True, message
        return True, "The vehicle could not be added to the database!"


def search(name, brand, year_of_manufacture, ready_to_drive):
    try:
        vehicles_query = vehicle_helpers.get_all_vehicles()
        if name:
            vehicles_query = vehicle_helpers.get_vehicles_by_name(
                vehicles_query, name)

        if brand:
            vehicles_query = vehicle_helpers.get_vehicles_by_brands(
                vehicles_query, brand)

        if year_of_manufacture:
            vehicles_query = vehicle_helpers.get_vehicles_by_manufacturer_year(
                vehicles_query,
                year_of_manufacture
            )
        if ready_to_drive:
            vehicles_query = vehicle_helpers.get_vehicles_by_ready_to_drive(
                vehicles_query,
                ready_to_drive
            )

        return False, '', vehicles_query
    except Exception as e:
        return True, 'Search function is not working properly', None


def get_vehicles():
    """Get all vehicles present"""
    return vehicle_helpers.get_all_vehicles().all()


def get_vehicle(vehicle_id):
    """Get single vehicle"""
    return vehicle_helpers.get_all_vehicles().filter_by(id=vehicle_id).all()
