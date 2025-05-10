from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class ClientLog(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hostname = db.Column(db.String(100), nullable=False)
	client_ip = db.Column(db.String(100))
	timestamp = db.Column(db.DateTime, nullable=False)
	message = db.Column(db.String(200))
