from flask import Flask
from config import Config
from models.models import db
from routes.event_routes import event_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(event_bp)

if __name__ == "__main__":
    app.run(debug=True)