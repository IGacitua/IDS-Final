import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    total_points = db.Column(db.Integer, nullable=False) # Todos los puntos que ganó el usuario, sin considerar gastos. Se usa para ver la etapa del juego
    spent_points = db.Column(db.Integer, nullable=False) # Los puntos que gastó el usuario. Usados para calcular puntos actuales
    lastclick = db.Column(db.Date, nullable=False) # Momento del ultimo clic. Se usa para calcular los puntos que deben dar las mejoras pasivas.
    trofeo=db.relationship('Trofeo', uselist=False,backref='user', lazy=True)
    # Agregar una columna para el tier de cada mejora

class Mejora(db.Model):
    __tablename__ = 'mejoras'
    id = db.Column(db.Integer, primary_key=True)
    nombre_interno = db.Column(db.String(255), nullable=False)
    efecto = db.Column(db.String(50), nullable=False)  # Puede ser 'suma', 'multi', 'pasivo', o 'potencia'

    # Valor y nombre de cada tier (No deberían existir mas de 5 por mejora)
    # Todos menos el primero pueden ser nulos
    valor_tier_1 = db.Column(db.Integer, nullable=False) 
    nombre_tier_1 = db.Column(db.String(255), nullable=False)
    valor_tier_2 = db.Column(db.Integer, nullable=True)
    nombre_tier_2 = db.Column(db.String(255), nullable=True)
    valor_tier_3 = db.Column(db.Integer, nullable=True)
    nombre_tier_3 = db.Column(db.String(255), nullable=True)
    valor_tier_4 = db.Column(db.Integer, nullable=True)
    nombre_tier_4 = db.Column(db.String(255), nullable=True)
    valor_tier_5 = db.Column(db.Integer, nullable=True)
    nombre_tier_5 = db.Column(db.String(255), nullable=True)
    
class Trofeo(db.Model):
    __tablename__ = 'trofeos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    time_seconds = db.Column(db.Integer, nullable=False)  # Tiempo en segundos, esto seria mejor tenerlo asi para contar en segundos
    obtained = db.Column(db.Date, nullable=False)  # Fecha en que se obtuvo el trofeo
    message = db.Column(db.String(255), nullable=False)  # Mensaje personalizado del usuario
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    
