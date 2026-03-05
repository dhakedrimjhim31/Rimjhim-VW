from flask import Flask
from products import products_bp
from cart import cart_bp
from orders import orders_bp

app = Flask(__name__)
app.secret_key = "secret"

app.register_blueprint(products_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(orders_bp)

if __name__ == "__main__":
    app.run(debug=True)

