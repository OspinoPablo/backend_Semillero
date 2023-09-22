from Models.users_model import db, ma
from db.db import app

class GunsType(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(300))

    def __init__(self, nombre):
        self.nombre = nombre

class GunsTypeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = GunsType

gun_type_schema = GunsTypeSchema()
guns_type_schema = GunsTypeSchema(many=True)

with app.app_context():
    db.create_all()