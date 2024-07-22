import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    total_points = db.Column(db.Integer, nullable=False) # Todos los puntos que ganó el usuario, sin considerar gastos. Se usa para ver la etapa del juego
    spent_points = db.Column(db.Integer, nullable=False) # Los puntos que gastó el usuario. Usados para calcular puntos actuales
    last_click = db.Column(db.Date, nullable=False) # Momento del ultimo clic. Se usa para calcular los puntos que deben dar las mejoras pasivas.
    trofeo=db.relationship('Trophy', uselist=False,backref='user', lazy=True)
    # Agregar una columna para el tier de cada mejora

class Upgrade(db.Model):
    __tablename__ = 'mejoras'
    id = db.Column(db.Integer, primary_key=True)
    internal_name = db.Column(db.String(255), nullable=False)
    effect = db.Column(db.String(50), nullable=False)  # Puede ser 'ADD', 'MULTIPLY', 'PASSIVE', o 'EXPONENT'

    # Valor y nombre de cada tier (No deberían existir mas de 5 por mejora)
    # Todos menos el primero pueden ser nulos
    value_tier_1 = db.Column(db.Integer, nullable=False) 
    name_tier_1 = db.Column(db.String(255), nullable=False)
    value_tier_2 = db.Column(db.Integer, nullable=True)
    name_tier_2 = db.Column(db.String(255), nullable=True)
    value_tier_3 = db.Column(db.Integer, nullable=True)
    name_tier_3 = db.Column(db.String(255), nullable=True)
    value_tier_4 = db.Column(db.Integer, nullable=True)
    name_tier_4 = db.Column(db.String(255), nullable=True)
    value_tier_5 = db.Column(db.Integer, nullable=True)
    name_tier_5 = db.Column(db.String(255), nullable=True)
    
class Trophy(db.Model):
    __tablename__ = 'trofeos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    time_seconds = db.Column(db.Integer, nullable=False)  # Tiempo en segundos, esto seria mejor tenerlo asi para contar en segundos
    date_obtained = db.Column(db.Date, nullable=False)  # Fecha en que se obtuvo el trofeo
    custom_message = db.Column(db.String(255), nullable=False)  # Mensaje personalizado del usuario
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    
