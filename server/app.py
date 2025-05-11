from flask import Flask, request, jsonify, redirect, url_for, render_template, send_from_directory
from models import db, User, ClientLog
import os

app = Flask(__name__)

BASE_DIR=os.path.dirname(os.path.abspath(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'clients.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/register", methods=["GET", "POST"])
def register():
	if request.method == "GET":
		return render_template("register.html")

	username=request.form["username"]
	password=request.form["password"]

	existing_user = User.query.filter_by(username=username).first()

	if existing_user:
		return "El usuario ya existe"

	new_user = User(username=username, password=password)
	db.session.add(new_user)
	db.session.commit()

	log = ClientLog(
		action="register",
		username=username,
		ip_address=request.remote_addr
	)
	db.session.add(log)
	db.session.commit()
	
	return render_template("success.html")



@app.route("/login", methods=["GET", "POST"])
def login():
	if request.method == "GET":
		return render_template("login.html")

	username=request.form["username"]
	password=request.form["password"]

	user = User.query.filter_by(username=username, password=password).first()
	
	if user:
		log = ClientLog(
			action="login",
			username=username,
			ip_address=request.remote_addr
		)
		db.session.add(log)
		db.session.commit()

		return f"<h2>WELCOME, {username}!!!</h2><p>Login Exitoso.</p>"

	else:
		log = ClientLog(
			action="Fail",
			username=username,
			ip_address=request.remote_addr
		)
		db.session.add(log)
		db.session.commit()

		return "<h2>Credenciales incorrectas</h2><a href='/login'><button>Reintentar</button></a>", 401


@app.route("/", methods=["GET"])
def index():
	return render_template("index.html")	

@app.route("/favicon.ico")
def favicon():
	return send_from_directory("static", "CyberSecurity.png")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000, debug=True)
