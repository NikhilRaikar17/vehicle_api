from application.models import Vehicle

def get_vehicle(brand,description,year_of_manufacture,ready_to_drive):
    vehicle = Vehicle.query.filter_by(
                                    brand=brand,
                                    description=description,
                                    year_of_manufacture=year_of_manufacture,
                                    ready_to_drive=ready_to_drive
                                    ).first()
    if vehicle:
        return True
        
    return False

def get_vehicle_brand(brand):
    vehicle = Vehicle.query.filter_by(
                                    brand=brand,
                                    ).first()
    if vehicle:
        return True

    return False
