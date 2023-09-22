from Models.users_model import db, ma
from db.db import app

class CrimesType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(300))

    def __init__(self, nombre):
        self.nombre = nombre

class CrimesTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = CrimesType

crime_type_schema = CrimesTypeSchema()
crimes_type_schema = CrimesTypeSchema(many=True)

with app.app_context():
    db.create_all()