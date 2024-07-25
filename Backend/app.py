from flask import Flask, request, jsonify
from models import db, User, Upgrade, UserUpgrade
import time
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
port = 5000
# Esta parte se debe cambiar la url de usar otra maquina
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://licha:1234@localhost:5432/mi_base'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def home():
    return """
    <html>
    <body>
    <h1>Welcome to Qubit Miner API!</h1>
    </body>
    </html>
    """

# Listar todos los usuarios
@app.route("/users/", methods=["GET", "POST"])
def all_users():

    if request.method == "GET":
        try:
            usuarios = User.query.all()
            usuarios_data = []
            for usuario in usuarios:
                usuario_data = {
                    'id': usuario.id,
                    'name': usuario.name,
                    'total_points': usuario.total_points,
                    'spent_points': usuario.spent_points,
                    'last_click': usuario.last_click
                }
                usuarios_data.append(usuario_data)
            return jsonify(usuarios_data)
        except Exception as error:
            print(error) #En caso de haber error lo imprimo
            return jsonify({"Message": "No users found."}) # Acá queda a deber que tipo de error queremos proporcionarle
        
    elif request.method == "POST":
        try:
            data = request.json
            nuevo_nombre = data.get('name')         
            # Se definen valores predeterminados si no se proporcionan
            total_points = data.get('total_points', 0)
            spent_points = data.get('spent_points', 0)
            #lastclick = data.get('lastclick', None)  # Se establece que el usuario nuevo no tiene cl        
            # Si lastclick no se proporciona, se usará el valor por defecto en el modelo
            nuevo_user = User(name=nuevo_nombre, total_points=total_points, spent_points=spent_points) #removido el last_click hasta resolver lo del horario
            db.session.add(nuevo_user)
            db.session.commit()
            return jsonify({'user': {'id': nuevo_user.id, 'name': nuevo_user.name, 'total_points': nuevo_user.total_points, 'spent_points': nuevo_user.spent_points, 'last_click': nuevo_user.last_click}}), 201
        except Exception as error:
            print(error)
            return jsonify({"message": "Couldn't create user."}), 500 # Esto no deberia pasar nunca

    else:
        return jsonify({"message": "Method not allowed."}), 405
        
@app.route("/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def user_by_id(user_id):

    if request.method == "PUT":
        try:
            usuario = User.query.get(user_id)

            if usuario:
                data=request.json
                if 'name' in data:
                    usuario.name= data['name']
                if 'total_points' in data:
                    usuario.total_points = data['total_points']
                if 'spent_points' in data:
                    usuario.spent_points = data['spent_points']
                db.session.commit()
                return jsonify({"Mensaje": f"User with id:{user_id} updated"}), 200
            
            else:
                return jsonify({"Mensaje": "User does not exist"}), 404
            
        except Exception as error:
            print(error)
            return jsonify({"mensaje": f"Error when updating user {user_id}"}), 500

    elif request.method == "DELETE":
        try:
            # Busca al usuario por ID
            user = User.query.get(user_id)

            if user:
                user_upgrade=UserUpgrade.query.filter_by(user_id==user.id).first()
                if user_upgrade:
                    db.session.delete(user_upgrade)               
                db.session.delete(user)
                db.session.commit()
                return jsonify({"Message": "User succesfully eliminated."}), 200
            
            else:
                return jsonify({"Message": "User not found."}), 404
            
        except Exception as error:
            print(error) 
            return jsonify({"message": "Error when deleting user."}), 400
            
    elif request.method == "GET":
        try:
            user = User.query.get(user_id)

            if user:
                user_data = {
                    'id': user.id,
                    'name': user.name,
                    'total_points': user.total_points,
                    'spent_points': user.spent_points,
                    'last_click': user.last_click
                }
                return jsonify(user_data)
            
            else:
                return jsonify({"mensaje": f"User {user_id} not found."}), 404
            
        except Exception as error:
            print(error)
            return jsonify({"message": f"Error when searching for user {user_id}."}), 500

    else:
        return jsonify({"message": "Method not allowed."}), 405


@app.route("/users/<user_id>/upgrades",methods=["GET", "POST", "PUT"])
def get_upgrades_by_id(user_id):

    if request.method=='GET':
        try:
            upgrades = UserUpgrade.query.get(user_id)
            if upgrades:
                user_upgrades = {
                    "example": upgrades.exampleUpgrade
                }
                return jsonify(user_upgrades)
            else:
                return jsonify({"message": f"User {user_id} not found."}), 404
        except Exception as error:
            print(error)
            return jsonify({"message": f"Error when searching for user {user_id}."}), 500
        
    #elif request.method=='POST':
    
if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Server started!')


