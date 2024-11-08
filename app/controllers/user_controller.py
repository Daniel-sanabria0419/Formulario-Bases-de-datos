# app/controllers/user_controller.py
from flask import Blueprint, render_template, request

# Definir el blueprint
user_blueprint = Blueprint('user', __name__, url_prefix='/user')
@user_blueprint.route('/form', methods=['GET', 'POST'])
def home():
 return render_template('form.html')
@user_blueprint.route('/list')
def list_users():
    from app.models.user_model import db, User 
    # Obtener todos los usuarios de la base de datos
    users = User.query.all()
    return render_template('list_users.html', users=users) 
@user_blueprint.route('/create', methods=['GET', 'POST'])
def create_user():
    from app import db  # Importa 'db' desde app, asegurando que está disponible en esta función
    from app.models.user_model import User   # También importar el modelo aquí

    if request.method == 'POST':
        cedula = request.form['cedula']
        nombres = request.form['nombres']
        apellidos = request.form['apellidos']
        direccion_residencia = request.form['direccion_residencia']
        lat_residencia = request.form['lat_residencia']
        lng_residencia = request.form['lng_residencia']
        direccion_trabajo = request.form['direccion_trabajo']
        lat_trabajo = request.form['lat_trabajo']
        lng_trabajo = request.form['lng_trabajo']

        # Crear el usuario
        new_user = User(
            cedula=cedula,
            nombres=nombres,
            apellidos=apellidos,
            direccion_residencia=direccion_residencia,
            latitud_residencia=lat_residencia,
            longitud_residencia=lng_residencia,
            direccion_trabajo=direccion_trabajo,
            latitud_trabajo=lat_trabajo,
            longitud_trabajo=lng_trabajo
        )

        # Guardar en la base de datos
        db.session.add(new_user)
        db.session.commit()

    return render_template('form.html')
