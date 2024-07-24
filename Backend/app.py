from flask import Flask, request, jsonify
from models import db, User, Trophy, Upgrade
from sqlalchemy.exc import IntegrityError
import datetime

app = Flask(__name__)
port = 5000
# Esta parte se debe cambiar la url de usar otra maquina
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://tomy_gomez:tomy_gomez@localhost:5432/mi_base_datos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def home():
    return """
    <html>
    <body>
    <h1>Welcome to Cubit API!</h1>
    </body>
    </html>
    """

# Listar todos los usuarios
@app.route("/usuarios/", methods=["GET"])
def usuarios():
    try:
        usuarios = User.query.all()
        usuarios_data = []
        for usuario in usuarios:
            usuario_data = {
                'id': usuario.id,
                'name': usuario.name,
                'total_points': usuario.total_points,
                'spent_points': usuario.spent_points,
                #'last_click': usuario.last_click
            }
            usuarios_data.append(usuario_data)
        return jsonify(usuarios_data)
    except Exception as error:
        print(error) #En caso de haber error lo imprimo
        return jsonify({"mensaje": "No hay usuarios."}) # Acá queda a deber que tipo de error queremos proporcionarle

@app.route("/usuarios/", methods=["POST"])
def nuevo_usuario():
    try:
        data = request.json
        nuevo_nombre = data.get('name')
       
        # Se definen valores predeterminados si no se proporcionan
        total_points = data.get('total_points', 0)
        spent_points = data.get('spent_points', 0)
        #lastclick = data.get('lastclick', None)  # Se establece que el usuario nuevo no tiene click
       
        # Si lastclick no se proporciona, se usará el valor por defecto en el modelo
        nuevo_usero = User(name=nuevo_nombre, total_points=total_points, spent_points=spent_points) #removido el last_click hasta resolver lo del horario
        db.session.add(nuevo_usero)
        db.session.commit()
        return jsonify({'usuario': {'id': nuevo_usero.id, 'name': nuevo_usero.name, 'total_points': nuevo_usero.total_points, 'spent_points': nuevo_usero.spent_points}}), 201
    except Exception as error:
        print(error)
        return jsonify({"mensaje": "No se pudo crear el usuario."}), 500 # Esto no deberia pasar nunca
    
@app.route("/usuarios/", methods=["PUT"])
def edit_user(user_id):
    try:
        usuario = User.query.get('name')
        if usuario:
            data=request.json
            if 'name' in data:
                usuario.name= data['name']
            if 'total_points' in data:
                usuario.total_points = data['total_points']
            if 'spent_points' in data:
                usuario.spent_points = data['spent_points']
            usuario.last_click = datetime.datetime.now()

            db.session.commit()
            return jsonify({"Mensaje": "Usuario actualizado"}), 200
        else:
            return jsonify({"Mensaje": "usuario no existe"}), 404
    except Exception as error:
        print(error)
        return jsonify({"mensaje": "Error al actualizar el usuario"}), 500



@app.route("/usuarios/<username>", methods=["GET"])
def get_by_name(username):
    try:
        user = User.query.filter_by(name=username).first()
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
            return jsonify({"mensaje": "usuario no encontrado."}), 404
    except Exception as error:
        print(error)
        return jsonify({"mensaje": "Error al obtener el usuario."}), 500


if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started...')


