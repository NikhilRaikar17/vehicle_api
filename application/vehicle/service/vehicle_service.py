import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from vehicle.entities.vehicle_entities import ValidVehicle

def validate_vehicle(brand,description,year_of_manufacture,ready_to_drive):
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
