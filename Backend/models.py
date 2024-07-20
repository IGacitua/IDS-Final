import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    total_points = db.Column(db.Integer, nullable=False)
    current_points = db.Column(db.Integer, nullable=False)
    lastclick = db.Column(db.Date, nullable=False)
    trofeo=db.relationship('Trofeo', uselist=False,backref='user', lazy=True)
    
class Mejora(db.Model):
    __tablename__ = 'mejoras'
    id = db.Column(db.Integer, primary_key=True)
    nombre_comun = db.Column(db.String(255), nullable=False)
    efecto = db.Column(db.String(50), nullable=False)  # Puede ser 'suma', 'multi', 'pasivo'
    valor = db.Column(db.Integer, nullable=False)  # Valor del efecto, en caso de pasivo, qubits por segundo
    efecto_tier = db.Column(db.Integer, nullable=False)  # Cuánto afecta el valor cada tier
    nombre_tier_1 = db.Column(db.String(255), nullable=False)
    nombre_tier_2 = db.Column(db.String(255), nullable=False)
    #Acá se añadirian mas tiers de ser necesarias
    
class Trofeo(db.Model):
    __tablename__ = 'trofeos'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    time_seconds = db.Column(db.Integer, nullable=False)  # Tiempo en segundos, esto seria mejor tenerlo asi para contar en segundos
    obtained = db.Column(db.Date, nullable=False)  # Fecha en que se obtuvo el trofeo
    message = db.Column(db.String(255), nullable=False)  # Mensaje personalizado del usuario
    user_id=db.Column(db.Integer, db.ForeignKey('users.id'), unique=True, nullable=False)
    
