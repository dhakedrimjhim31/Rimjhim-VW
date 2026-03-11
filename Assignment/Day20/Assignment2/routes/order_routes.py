from flask import Blueprint, request, jsonify
from models.order_model import db, Order

order_bp = Blueprint("order_bp", __name__)

# Add Order
@order_bp.route("/orders", methods=["POST"])
def add_order():

    data = request.json

    order = Order(
        product_name=data["product_name"],
        quantity=data["quantity"],
        price=data["price"]
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({"message": "Order added"})


# Display All Orders
@order_bp.route("/orders", methods=["GET"])
def get_orders():

    orders = Order.query.all()

    result = []

    for o in orders:
        revenue = o.price * o.quantity

        result.append({
            "id": o.id,
            "product_name": o.product_name,
            "quantity": o.quantity,
            "price": o.price,
            "revenue": revenue
        })

    return jsonify(result)


# Total Revenue
@order_bp.route("/orders/revenue")
def total_revenue():

    orders = Order.query.all()

    total = 0

    for o in orders:
        total += o.price * o.quantity

    return jsonify({"total_revenue": total})


# Orders where revenue > 2000
@order_bp.route("/orders/high")
def high_orders():

    orders = Order.query.all()

    result = []

    for o in orders:
        revenue = o.price * o.quantity

        if revenue > 2000:
            result.append({
                "product_name": o.product_name,
                "revenue": revenue
            })

    return jsonify(result)