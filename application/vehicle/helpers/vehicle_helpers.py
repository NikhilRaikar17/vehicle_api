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

def get_vehicles_by_name(vehicle_query,name):
    """Get vehicles from name"""
    vehicles_by_name = vehicle_query.filter(
                                            Vehicle.name==name
                                            )
    return vehicles_by_name

def get_vehicles_by_brands(vehicle_query,brand):
    """Get vehicles from brands"""
    vehicles_by_brands = vehicle_query.filter(
                                            Vehicle.brand.in_(brand)
                                            )
    return vehicles_by_brands

def get_vehicles_by_manufacturer_year(vehicle_query,year_of_manufacture):
    """Get vehicles from year of manufacturer"""
    vehicles_by_manufacturer_year = vehicle_query.filter(
                                            Vehicle.year_of_manufacture.in_(year_of_manufacture)
                                            )
    return vehicles_by_manufacturer_year

def get_vehicles_by_ready_to_drive(vehicle_query,ready_to_drive):
    """Get vehicles from year of ready_to_drive"""
    vehicles_by_ready_to_drive = vehicle_query.filter(
                                                    Vehicle.ready_to_drive == ready_to_drive
                                                    )
    return vehicles_by_ready_to_drive

def get_all_vehicles():
    """Get all vehicles"""
    return Vehicle.query

def get_vehicle_by_id(vehicle_id):
    """Get a vehicle object from id"""
    vehicle = Vehicle.query.filter_by(
                                    id=vehicle_id,
                                    ).first()
    if vehicle:
        return vehicle

    return False

def get_duplicate_vehicle(vehicle_id,name,brand,year_of_manufacture):
    """Get a vehicle object from id"""
    vehicle = Vehicle.query.filter_by(
                                    name=name,
                                    brand=brand,
                                    year_of_manufacture=year_of_manufacture
                                    ).first()
    if vehicle and vehicle.id != vehicle_id:
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
        if old_vehicle.name != valid_vehicle.name:
            old_vehicle.name = valid_vehicle.name

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
        print(e)
        db.session.rollback()
        db.session.flush()
        return False


