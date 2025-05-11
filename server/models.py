from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(100), nullable=False)
	
class ClientLog(db.Model):
	id  = db.Column(db.Integer, primary_key=True)
	action = db.Column(db.String(50), nullable=False)
	username = db.Column(db.String(50), nullable=False)
	ip_address = db.Column(db.String(50), nullable=False)
	timestamp = db.Column(db.DateTime, default=datetime.utcnow)
