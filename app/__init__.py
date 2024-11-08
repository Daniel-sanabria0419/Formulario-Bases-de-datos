# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.controllers.user_controller import user_blueprint

# Instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/proyecto_form'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Para evitar advertencias

    # Vincular la instancia de db con la app
    db.init_app(app)

    # Registrar el blueprint
    app.register_blueprint(user_blueprint)

    return app
