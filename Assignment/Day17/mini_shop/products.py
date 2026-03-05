from flask import Blueprint, render_template, request, redirect, make_response
import json

products_bp = Blueprint("products", __name__, url_prefix="/products")

# Dummy Products
PRODUCT_LIST = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Headphones": 2000,
    "Mobile": 20000
}

@products_bp.route("/")
def show_products():
    return render_template("products.html", products=PRODUCT_LIST)


@products_bp.route("/add/<product>")
def add_to_cart(product):
    response = make_response(redirect("/cart"))

    cart_cookie = request.cookies.get("cart")

    if cart_cookie:
        cart = json.loads(cart_cookie)
    else:
        cart = {}
    
    cart[product] = cart.get(product, 0) + 1

   #if product in cart:
    #   cart[product] += 1
   #else:
    #   cart[product] = 1

    response.set_cookie("cart", json.dumps(cart))
    return response

