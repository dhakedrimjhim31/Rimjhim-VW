from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)
CORS(app)

# In-memory product storage
products = []

@app.route("/upload-products", methods=["POST"])
def upload_products():

    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['file']

    total_rows = 0
    products_added = 0
    failed_rows = 0

    stream = file.stream.read().decode("UTF8").splitlines()
    csv_reader = csv.DictReader(stream)

    for row in csv_reader:

        total_rows += 1

        name = row["name"]
        price = row["price"]
        stock = row["stock"]

        try:

            # Validation
            if not name.strip():
                raise ValueError("Invalid name")

            price = float(price)
            if price <= 0:
                raise ValueError("Invalid price")

            stock = int(stock)
            if stock < 0:
                raise ValueError("Invalid stock")

            # Store valid product
            product = {
                "name": name,
                "price": price,
                "stock": stock
            }

            products.append(product)
            products_added += 1

        except:
            failed_rows += 1

    return jsonify({
        "total_rows": total_rows,
        "products_added": products_added,
        "failed_rows": failed_rows
    })


# Optional: view stored products
@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


if __name__ == "__main__":
    app.run(debug=True)