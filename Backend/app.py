from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User, Upgrade, UserUpgrade
from editable import return_db_name


app = Flask(__name__)
CORS(app)
port = 5000
database = return_db_name()
# Esta parte se debe cambiar la url de usar otra maquina
app.config['SQLALCHEMY_DATABASE_URI'] = database
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
        return list_users()
    elif request.method == "POST":
        return create_user()
    else:
        return jsonify({"message": "Method not allowed."}), 405

def list_users():
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
        return jsonify({"Message": "No users found."}), 500 

def create_user():
    try:
        data = request.json
        nuevo_nombre = data.get('name')         
        # Se definen valores predeterminados si no se proporcionan
        total_points = data.get('total_points', 0)
        spent_points = data.get('spent_points', 0)
        new_user = User(name=nuevo_nombre, total_points=total_points, spent_points=spent_points) #removido el last_click hasta resolver lo del horario
        db.session.add(new_user)
        db.session.commit()

        new_upgrades = UserUpgrade(user_id=new_user.id)
        db.session.add(new_upgrades)
        db.session.commit()

        return jsonify({
            'user': {
                'id': new_user.id, 
                'name': new_user.name, 
                'total_points': new_user.total_points, 
                'spent_points': new_user.spent_points, 
                'upgrades': {
                    'pickaxe': new_upgrades.pickaxe,
                    'lantern': new_upgrades.lantern,
                    'assistant': new_upgrades.assistant,
                    'meals': new_upgrades.meals,
                    'housing': new_upgrades.housing,
                    'helmet': new_upgrades.helmet,
                    'cartographer': new_upgrades.cartographer
                }
            }
        }), 201
    except Exception as error:
            print(error)
            return jsonify({"message": "Couldn't create user."}), 500 # Esto no deberia pasar nunca


@app.route("/users/<user_id>/", methods=["GET", "PUT", "DELETE", "POST"])
def user_by_id(user_id):

    if request.method == "GET":
        return get_user(user_id)
    elif request.method == "PUT":
        return update_user(user_id)
    elif request.method == "DELETE":
        return delete_user(user_id)
    else:
        return jsonify({"message": "Method not allowed."}), 405
                   
#Funcion para obtener user segun id
def get_user(user_id):
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

#Funcion para cambiar data del user segun id
def update_user(user_id):               
    try:
        user = User.query.get(user_id)
        if user:
            data=request.json
            if 'name' in data:
                user.name= data['name']
            if 'total_points' in data:
                user.total_points = data['total_points']
            if 'spent_points' in data:
                user.spent_points = data['spent_points']
            if 'last_click' in data:
                user.last_click = data['last_click']
            db.session.commit()
            return jsonify({"Mensaje": f"User with id:{user_id} updated"}), 200
        else:
            return jsonify({"Mensaje": "User does not exist"}), 404
    
    except Exception as error:
        print(error)
        return jsonify({"mensaje": f"Error when updating user {user_id}"}), 500

#Funcion borrar user segun id
def delete_user(user_id):
    try:
        # Busca al usuario por ID
        user = User.query.get(user_id)
        if user:
            user_upgrade=UserUpgrade.query.filter_by(user_id=user.id).first()
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

        
@app.route("/users/<user_id>/upgrades/", methods=["GET", "POST", "PUT"])
def get_upgrades_by_id(user_id):
    if request.method == 'GET':
        return list_user_upgrades(user_id)
    elif request.method == 'PUT':
        return update_user_upgrades(user_id)
    else:
        return jsonify({"message": "Method not allowed."}), 405

def list_user_upgrades(user_id):
    try:
        upgrades = UserUpgrade.query.filter_by(user_id=user_id).first()
        if upgrades:
            user_upgrades = {
                "user_id": upgrades.user_id,
                "pickaxe": upgrades.pickaxe,
                "lantern": upgrades.lantern,
                "assistant": upgrades.assistant,
                "meals": upgrades.meals,
                "housing": upgrades.housing,
                "helmet": upgrades.helmet,
                "cartographer": upgrades.cartographer,
            }
            return jsonify(user_upgrades)
        else:
            return jsonify({"message": f"User {user_id} not found."}), 404
    except Exception as error:
        print(error)
        return jsonify({"message": f"Error when searching for user {user_id}."}), 500
   
def update_user_upgrades(user_id):
    try: #ver si cambiar el user_id para evitar confusiones
        upgrades=UserUpgrade.query.filter_by(user_id=user_id).first()
        if not upgrades:
            return jsonify({"message": f"User {user_id} not found."}), 404

        data=request.json
        upgrades.pickaxe=data.get('pickaxe', upgrades.pickaxe)
        upgrades.lantern=data.get('lantern',upgrades.lantern)
        upgrades.assistant=data.get('assistant',upgrades.assistant)
        upgrades.meals=data.get('meals',upgrades.meals)
        upgrades.housing=data.get('housing',upgrades.housing)
        upgrades.helmet=data.get('helmet',upgrades.helmet)
        upgrades.cartographer=data.get('cartographer',upgrades.cartographer)

        db.session.commit()
        return jsonify({"message": "Upgrades updated succesfully."}), 200
                
    except Exception as error:
        print(error)
        return jsonify({"message": "Couldn't update user upgrades."}), 500

        
@app.route("/upgrades/", methods=["GET"])
def get_all_upgrades():
    if request.method == "GET":
        return list_upgrades()
    else:
        return jsonify({"message": "Method not allowed."}), 405

def list_upgrades():
    try:
        upgrades = Upgrade.query.all()
        upgrades_data = []
        for upgrade in upgrades:
            upgrade_data = {
                'id': upgrade.id,
                'internal_name': upgrade.internal_name,
                'effect': upgrade.effect,
                'value_tier_1': upgrade.value_tier_1,
                'cost_tier_1': upgrade.cost_tier_1,
                'name_tier_1': upgrade.name_tier_1,
                'value_tier_2': upgrade.value_tier_2,
                'cost_tier_2': upgrade.cost_tier_2,
                'name_tier_2': upgrade.name_tier_2,
                'value_tier_3': upgrade.value_tier_3,
                'cost_tier_3': upgrade.cost_tier_3,
                'name_tier_3': upgrade.name_tier_3,
                'value_tier_4': upgrade.value_tier_4,
                'cost_tier_4': upgrade.cost_tier_4,
                'name_tier_4': upgrade.name_tier_4,
                'value_tier_5': upgrade.value_tier_5,
                'cost_tier_5': upgrade.cost_tier_5,
                'name_tier_5': upgrade.name_tier_5
            }
            upgrades_data.append(upgrade_data)
        return jsonify(upgrades_data)
    except Exception as error:
        print(error) #En caso de haber error lo imprimo
        return jsonify({"Message": "No upgrades found."}), 500


if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Server started!')

