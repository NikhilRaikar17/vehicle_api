from application.models import Vehicle

def get_vehicle(name,brand,description,year_of_manufacture,ready_to_drive):
    """Get a vehicle object from the database"""
    vehicle = Vehicle.query.filter_by(
                                    name=name,
                                    brand=brand,
                                    description=description,
                                    year_of_manufacture=year_of_manufacture,
                                    ready_to_drive=ready_to_drive
                                    ).first()
    if vehicle:
        return True
        
    return False

def get_vehicle_by_brand(brand):
    """Get a vehicle object from brand name"""
    vehicle = Vehicle.query.filter_by(
                                    brand=brand,
                                    ).first()
    if vehicle:
        return True

    return False

def get_vehicle_by_id(vehicle_id):
    """Get a vehicle object from id"""
    vehicle = Vehicle.query.filter_by(
                                    id=vehicle_id,
                                    ).first()
    if vehicle:
        return True

    return False

def get_duplicate_vehicle(name,brand,year_of_manufacture):
    """Get a vehicle object from id"""
    vehicle = Vehicle.query.filter_by(
                                    name=name,
                                    brand=brand,
                                    year_of_manufacture=year_of_manufacture
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

def update_vehicle(db,valid_vehicle,old_vehicle):
    """Check and update proper vehicle attribute"""
    try:
        if old_vehicle.brand != valid_vehicle.brand:
            old_vehicle.brand = valid_vehicle.brand
        
        if old_vehicle.description != valid_vehicle.description:
            old_vehicle.description = valid_vehicle.description
        
        if old_vehicle.year_of_manufacture != valid_vehicle.year_of_manufacture:
            old_vehicle.year_of_manufacture = valid_vehicle.year_of_manufacture
        
        if old_vehicle.ready_to_drive != valid_vehicle.ready_to_drive:
            old_vehicle.ready_to_drive = valid_vehicle.ready_to_drive
        
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        db.session.flush()
        return False


