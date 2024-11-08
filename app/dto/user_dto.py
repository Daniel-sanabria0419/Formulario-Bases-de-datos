# app/dto/user_dto.py
class UserDTO:
    def __init__(self, cedula, nombres, apellidos, direccion_residencia, coordenadas_residencia, direccion_trabajo, coordenadas_trabajo):
        self.cedula = cedula
        self.nombres = nombres
        self.apellidos = apellidos
        self.direccion_residencia = direccion_residencia
        self.coordenadas_residencia = coordenadas_residencia
        self.direccion_trabajo = direccion_trabajo
        self.coordenadas_trabajo = coordenadas_trabajo
