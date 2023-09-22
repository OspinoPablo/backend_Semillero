from Models.users_model import db, ma
from db.db import app

class Reportes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    barrio = db.Column(db.String(300))
    estrato = db.Column(db.Integer)
    municipio = db.Column(db.String(200))
    coordenadas = db.Column(db.String(200))
    fecha = db.Column(db.Date)
    hora = db.Column(db.Time)
    direccion = db.Column(db.String(255))
    afectados = db.Column(db.Integer)
    genero_victima = db.Column(db.String(20))
    tipo_zona = db.Column(db.String(30))
    archivo_evidencia = db.Column(db.String(255))
    descripcion = db.Column(db.Text)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))  # Usar 'usuarios.id' en lugar de 'Usuarios.id'
    usuario_rel = db.relationship('Usuarios', backref='reportes')

    def __init__(self, barrio, estrato, municipio, coordenadas, fecha, hora, direccion, afectados, genero_victima, descripcion, tipo_arma, id_modalidad_delito, id_usuario):
        self.barrio = barrio
        self.estrato = estrato
        self.municipio = municipio
        self.coordenadas = coordenadas
        self.fecha = fecha
        self.hora = hora
        self.direccion = direccion
        self.afectados = afectados
        self.genero_victima = genero_victima
        self.descripcion = descripcion
        self.tipo_arma = tipo_arma
        self.id_modalidad_delito = id_modalidad_delito
        self.id_usuario = id_usuario

class ReportesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Reportes

reporte_schema = ReportesSchema()
reportes_schema = ReportesSchema(many=True)

with app.app_context():
    db.create_all()