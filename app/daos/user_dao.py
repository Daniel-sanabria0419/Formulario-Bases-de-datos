# app/dao/user_dao.py
from app.models.user_model import User
from app import db

class UserDAO:
    def save_user(self, user_dto):
        new_user = User(
            cedula=user_dto.cedula,
            nombres=user_dto.nombres,
            apellidos=user_dto.apellidos,
            direccion_residencia=user_dto.direccion_residencia,
            coordenadas_residencia_lat=user_dto.coordenadas_residencia[0],
            coordenadas_residencia_long=user_dto.coordenadas_residencia[1],
            direccion_trabajo=user_dto.direccion_trabajo,
            coordenadas_trabajo_lat=user_dto.coordenadas_trabajo[0],
            coordenadas_trabajo_long=user_dto.coordenadas_trabajo[1]
        )
        db.session.add(new_user)
        db.session.commit()
