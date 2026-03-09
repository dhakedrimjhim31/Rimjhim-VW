from flask import Flask
from config import Config
from models.order_model import db
from routes.order_routes import order_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(order_bp)

if __name__ == "__main__":
    app.run(debug=True)