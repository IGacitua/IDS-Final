import time
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    total_points = db.Column(db.Integer, default=0) # Todos los puntos que ganó el usuario, sin considerar gastos. Se usa para ver la etapa del juego
    spent_points = db.Column(db.Integer, default=0) # Los puntos que gastó el usuario. Usados para calcular puntos actuales
    last_click = db.Column(db.Integer, default=int(time.time())) # Momento del ultimo clic. Se usa para calcular los puntos que deben dar las mejoras pasivas.
    upgrades=db.relationship('UserUpgrade', uselist=False, backref='User', lazy=True) # Uselist relaciona uno-uno
    # Agregar una columna para el tier de cada mejora
    
                
class UserUpgrade(db.Model):
    __tablename__ = 'user_upgrades'
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique = True, primary_key = True)
    # Añadir una columna INT para el tier de cada mejora
    # EL NOMBRE DE LA COLUMNA DEBE SER EXACTAMENTE IGUAL A INTERNAL_NAME EN UPGRADE
    pickaxe = db.Column(db.Integer, nullable=False, default=0)
    lantern = db.Column(db.Integer, nullable=False, default=0)
    assistant = db.Column(db.Integer, nullable = False, default = 0)
    meals = db.Column(db.Integer, nullable = False, default = 0)
    housing = db.Column(db.Integer, nullable = False, default = 0)
    helmet = db.Column(db.Integer, nullable = False, default = 0)
    cartographer = db.Column(db.Integer, nullable = False, default = 0)
    winning_condition = db.Column(db.Integer, nullable = False, default = 0)

class Upgrade(db.Model):
    __tablename__ = 'upgrades'
    id = db.Column(db.Integer, primary_key=True)
    internal_name = db.Column(db.String(255), nullable=False)
    effect = db.Column(db.String(50), nullable=False)  # Puede ser 'ADD', 'MULTIPLY', 'PASSIVE', o 'EXPONENT'

    # Valor y nombre de cada tier (No deberían existir mas de 5 por mejora)
    # Todos menos el primero pueden ser nulos
    # Nulo significa que no tiene ese tier

    # Tier 1
    value_tier_1 = db.Column(db.Float, nullable=False) 
    cost_tier_1 = db.Column(db.Integer, nullable = False)
    name_tier_1 = db.Column(db.String(255), nullable=False)
    description_tier_1 = db.Column(db.String(255), nullable = False)
    # Tier 2
    value_tier_2 = db.Column(db.Float, nullable=True)
    cost_tier_2 = db.Column(db.Integer, nullable = True)
    name_tier_2 = db.Column(db.String(255), nullable=True)
    description_tier_2 = db.Column(db.String(255), nullable = True)
    # Tier 3
    value_tier_3 = db.Column(db.Float, nullable=True)
    cost_tier_3 = db.Column(db.Integer, nullable = True)
    name_tier_3 = db.Column(db.String(255), nullable=True)
    description_tier_3 = db.Column(db.String(255), nullable = True)
    # Tier 4
    value_tier_4 = db.Column(db.Float, nullable=True)
    cost_tier_4 = db.Column(db.Integer, nullable = True)
    name_tier_4 = db.Column(db.String(255), nullable=True)
    description_tier_4 = db.Column(db.String(255), nullable = True)
    # Tier 5
    value_tier_5 = db.Column(db.Float, nullable=True)
    cost_tier_5 = db.Column(db.Integer, nullable = True)
    name_tier_5 = db.Column(db.String(255), nullable=True)
    description_tier_5 = db.Column(db.String(255), nullable = True)
