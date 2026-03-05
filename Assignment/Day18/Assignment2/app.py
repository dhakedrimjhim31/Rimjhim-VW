from flask import Flask
from auth import auth_bp
from products import products_bp

app = Flask(__name__)

app.secret_key = "secret123"

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(products_bp)

if __name__ == "__main__":
    app.run(debug=True)