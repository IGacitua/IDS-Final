from flask import Flask, request, jsonify
from models import db, User, Trophy, Upgrade

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
    <h1>Welcome to Cubit!</h1>
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
                'current_points': usuario.current_points,
                'lastclick': usuario.lastclick
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
        current_points = data.get('current_points', 0)
        lastclick = data.get('lastclick', None)  # Se establece que el usuario nuevo no tiene clickc
       
        # Si lastclick no se proporciona, se usará el valor por defecto en el modelo
        nuevo_usuario = User(name=nuevo_nombre, total_points=total_points, current_points=current_points, lastclick=lastclick)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return jsonify({'usuario': {'id': nuevo_usuario.id, 'name': nuevo_usuario.name, 'total_points': nuevo_usuario.total_points, 'current_points': nuevo_usuario.current_points, 'lastclick': nuevo_usuario.lastclick}}), 201
    except Exception as error:
        print(error)
        return jsonify({"mensaje": "No se pudo crear el usuario."}), 500 # Esto no deberia pasar nunca

if __name__ == '__main__':
    print('Starting server...')
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', debug=True, port=port)
    print('Started...')


