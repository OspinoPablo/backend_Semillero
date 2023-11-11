from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from db.db import app

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    correo = db.Column(db.String(30), nullable=False)
    contraseña = db.Column(db.String(30), nullable=False)
    usuario = db.Column(db.String(30))
    nombre = db.Column(db.String(30))
    apellido = db.Column(db.String(30))
    telefono = db.Column(db.Integer, nullable=False)
    imagen_perfil = db.Column(db.String(300))

    def __init__(self, correo, contraseña, usuario, nombre, apellido, telefono, imagen_perfil):
        self.correo = correo
        self.contraseña = contraseña
        self.usuario = usuario
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.imagen_perfil = imagen_perfil

class UsuariosSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Usuarios

usuario_schema = UsuariosSchema()
usuarios_schema = UsuariosSchema(many=True)

with app.app_context():
    db.create_all()