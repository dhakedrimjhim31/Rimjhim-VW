

from flask import Flask
from config import Config
from models.book_model import db
from routes.book_routes import book_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


app.register_blueprint(book_bp)
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)