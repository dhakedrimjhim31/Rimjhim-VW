from flask import jsonify, request, session, make_response
from . import products_bp

products = [
    {"id":1,"name":"Laptop","price":70000},
    {"id":2,"name":"Mouse","price":500},
    {"id":3,"name":"Keyboard","price":1200},
    {"id":4,"name":"Monitor","price":10000},
    {"id":5,"name":"Speaker","price":3000},
    {"id":6,"name":"Headphones","price":2000}
]


# API 2 - Get all products
@products_bp.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)


# API 3 - View product
@products_bp.route('/product/<int:product_id>', methods=['GET'])
def view_product(product_id):

    if 'username' not in session:
        return jsonify({"error":"Login required"}), 401

    product = next((p for p in products if p["id"] == product_id), None)

    if not product:
        return jsonify({"error":"Product not found"}), 404

    recent = request.cookies.get('recent_products')

    if recent:
        recent_list = recent.split(',')
    else:
        recent_list = []

    pid = str(product_id)

    if pid in recent_list:
        recent_list.remove(pid)

    recent_list.insert(0, pid)

    if len(recent_list) > 5:
        recent_list = recent_list[:5]

    resp = make_response(jsonify(product))
    resp.set_cookie('recent_products', ','.join(recent_list))

    return resp


# API 4 - Recently viewed products
@products_bp.route('/recent-products', methods=['GET'])
def recent_products():

    recent = request.cookies.get('recent_products')

    if not recent:
        return jsonify([])

    ids = recent.split(',')

    result = []

    for pid in ids:
        for p in products:
            if str(p["id"]) == pid:
                result.append({
                    "id": p["id"],
                    "name": p["name"]
                })

    return jsonify(result)





