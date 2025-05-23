from flask import Flask
from app import db, app

app = Flask(__name__)

# ✅ ESTA CONFIGURACIÓN ES OBLIGATORIA
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clients.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# ✅ Inicializamos db DESPUÉS de configurar la app
db.init_app(app)

with app.app_context():
    db.create_all()
    print("Database created successfully.")
