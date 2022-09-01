from application.models import Vehicle

def get_vehicle(brand,description,year_of_manufacture,ready_to_drive):
    """Get a vehicle object from the database"""
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
    """Get a vehicle object from brand name"""
    vehicle = Vehicle.query.filter_by(
                                    brand=brand,
                                    ).first()
    if vehicle:
        return True

    return False

def create_vehicle(db,valid_vehicle):
    """Create a new vehicle object"""
    try:
        new_vehicle = Vehicle(**vars(valid_vehicle))
        db.session.add(new_vehicle)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        db.session.flush()
        return False


