from flask import Blueprint, render_template, request, redirect, make_response
import json

cart_bp = Blueprint("cart", __name__, url_prefix="/cart")


PRODUCT_LIST = {
    "Laptop": 50000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Headphones": 2000,
    "Mobile": 20000
}

@cart_bp.route("/")
def view_cart():
    cart_cookie = request.cookies.get("cart")

    if not cart_cookie:
        return render_template("cart.html", cart={}, prices=PRODUCT_LIST, total =0,)
    
    cart = json.loads(cart_cookie)
    total = sum(PRODUCT_LIST[item] * qty for item, qty in cart.items())

    return render_template("cart.html", cart=cart, prices=PRODUCT_LIST,total=total)


@cart_bp.route("/update", methods=["POST"])
def update_cart():
    cart_cookie = request.cookies.get("cart")
    cart = json.loads(cart_cookie)

    item = request.form.get("item")
    qty = int(request.form.get("quantity"))


    if qty == 0:
        del cart[item]
    else:
        cart[item] = qty

    response = make_response(redirect("/cart"))

    if cart:
        response.set_cookies("cart", json.dumps(cart))
    else:
        response.delete_cookie("cart")
    
    return response

@cart_bp.route("/clear")
def clear_cart():
    response = make_response(redirect("/cart"))
    response.delete_cookie("cart")
    return response

                                      
                               