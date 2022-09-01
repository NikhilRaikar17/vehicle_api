from application import db
from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {each: getattr(self, each) for each in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(list_):
        return [element.serialize() for element in list_]

class Vehicle(db.Model,Serializer):
    __tablename__ = 'vehicle'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(),nullable=False)
    brand = db.Column(db.String(),nullable=False)
    description = db.Column(db.String())
    year_of_manufacture = db.Column(db.Integer, nullable=False)
    ready_to_drive = db.Column(db.Boolean, nullable=False)

    __table_args__ = (db.UniqueConstraint('name', 'brand','year_of_manufacture'),)

    def __repr__(self):
        return '<name {}>'.format(self.name)