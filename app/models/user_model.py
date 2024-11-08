# app/models/user_model.py
from flask_sqlalchemy import SQLAlchemy
from app import db
# Definir el modelo sin crear una instancia de db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cedula = db.Column(db.String(20), nullable=False, unique=True)
    nombres = db.Column(db.String(100), nullable=False)
    apellidos = db.Column(db.String(100), nullable=False)
    direccion_residencia = db.Column(db.String(255), nullable=False)
    latitud_residencia = db.Column(db.Float, nullable=False)
    longitud_residencia = db.Column(db.Float, nullable=False)
    direccion_trabajo = db.Column(db.String(255), nullable=False)
    latitud_trabajo = db.Column(db.Float, nullable=False)
    longitud_trabajo = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Users {self.nombres} {self.apellidos}>'
