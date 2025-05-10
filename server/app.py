from flask import Flask, request, jsonify
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return "<h2> Formulario de login (en construccion) </h2>"
	else:
		data = request.get_json()
		username = data.get("Username")
		password = data.get("Password")

		if not username or not password:
			return jsonify({"ERROR": "Faltan campos"}), 400

		existing_user = User.query.filter_by(username=username).first()
		if existing_user:
			return jsonify({"ERROR": "Usuario exitente"}), 400

		user = User(username=username, password=password)
		db.session.add(user)
		db.session.commit()

		return jsonify({"MESSAGE": "Usuario registrado con exito"}), 201
	


@app.route("/login", methods=["POST"])
def login():
	data = request.get_json()
	username = data.get("username")
	password = data.get("password")

	user = User.query.filter_by(username=username, password=password).first()
	if not user:
		return jsonify({"ERROR": "Credenciales Incorrectas"}), 401

	return jsonify({"MESSAGE": "Login Successful"}), 200

@app.route("/", methods=["GET"])
def index():
	return "<h1> Servidor activo, PEPIN!</h1>"	

@app.route("/favicon.ico")
def favicon():
	return send_from_directory("static", "CyberSecurity.png")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
