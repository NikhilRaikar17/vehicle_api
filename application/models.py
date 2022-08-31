from application import db


class Vehicle(db.Model):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer,primary_key=True)
    brand = db.Column(db.String(), unique=True)
    description = db.Column(db.String())
    year_of_manufacture = db.Column(db.Integer, nullable=False)
    ready_to_drive = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<brand {}>'.format(self.brand)