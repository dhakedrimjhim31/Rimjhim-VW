from flask import Flask,session,render_template,jsonify,request,redirect,url_for,make_response,request
import os
from admin import admin
import time
from datetime import datetime,timedelta
app=Flask(__name__) #Initializing flask app
 
products=[
    {"id":1,"name":"laptop","price":50000},
    {"id":2,"name":"Phone","price":20000}
]
@app.route("/api/products",methods=["GET"])
def get_products():
    return jsonify(products),200
 
@app.route("/api/products/<int:product_id>",methods=["GET"])
def get_product(product_id):
    for p in products:
        if p["id"]==product_id:
            return jsonify(p),200
    return jsonify({"error":"Product not found"}),404
 
@app.route("/api/products",methods=["POST"])
def create_product():
    data=request.get_json()
    if "name" not in data or "price" not in data:
        return jsonify({"error":"Invalid input"}),400
    new_id=len(products)+1
    new_product={
        "id":new_id,
        "name":data["name"],
        "price":data["price"]
 
    }
    products.append(new_product)
    return jsonify(new_product),201
 
@app.route("/api/products/<int:product_id>",methods=["PUT"])
def update_product(product_id):
    data=request.get_json()
    for p in products:
        if p["id"]==product_id:
            if "name" in data:
                p["name"]=data["name"]
            if "price" in data:
                p["price"]=data["price"]
            return jsonify(p),200
    return jsonify({"error":"Product not found"}),404
@app.route("/api/products/<int:product_id>",methods=["DELETE"])
def delete_product(product_id):
    for p in products:
        if p["id"]==product_id:
            products.remove(p)
            return jsonify({"message":"Product deleted"}),200
    return jsonify({"error":"Product not found"}),404
 
 
 
 
if __name__=='__main__':
    app.run(debug=True)