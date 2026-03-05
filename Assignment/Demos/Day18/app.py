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

////
let promise=new Promise(function(resolve,reject){
                let success=true;
                if(success){
                    resolve("Operation success")
                }else{
                    reject("Operation failed")
                }
            })
 
            promise.then(function(result){
                console.log(result)
 
            }).catch(function(err){
                console.log(err)
            })




////
fetch('http://localhost:5000/api/products',{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({
                name:"Tablet",
                price:20000
            })
         })
         .then(resp=>{
            console.log("Response",resp)
            return resp.json()
         })
         .then(data=>{
            console.log("Created",data)
         })
         .catch(err=>console.log(err))
 
 
 
            </script>



/////
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>

////
axios.get('http://localhost:5000/api/products')
.then(resp=>console.log(resp.data))
.catch(err=>console.log(err))
            </script>

////
axios.post('http:localhost:5000/api/products',{
    name:"Headphones",
    price:2000
}).then(resp=>{
    console.log("Created",resp.data)
}).catch(err=>console.log(err))




5///////
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

products = [
    {"id":1, "name":"Laptop", "price":50000},
    {"id":2, "name":"Mobile", "price":20000},
    {"id":3, "name":"Headphones", "price":2000}
]

@app.route("/api/products")
def get_products():
    return jsonify(products)

if _name_ == "_main_":
    app.run(debug=True)

6////////////
<!DOCTYPE html>
<html>
<body>

<h2>Products API</h2>
<button onclick="loadProducts()">Get Products</button>

<script>

async function loadProducts(){

let response = await fetch("http://127.0.0.1:5000/api/products");

let data = await response.json();

console.log(data);   // Shows whole API response

data.forEach(product => {
console.log(product.name + " - " + product.price);
});

}

</script>

</body>
</html>







7////////////
name,price,stock
Laptop,70000,10
Mouse,500,100
Keyboard,1200,50
Laptop,,10
Mouse,abc,20
Keyboard,1200,-5

8/////////////////
from flask import Flask, request, jsonify
from flask_cors import CORS
import csv

app = Flask(_name_)
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


if _name_ == "_main_":
    app.run(debug=True)




9///////////
<!DOCTYPE html>
<html>
<body>

<h2>Upload Product CSV</h2>

<input type="file" id="fileInput">
<button onclick="uploadFile()">Upload</button>

<script>

async function uploadFile(){

let file = document.getElementById("fileInput").files[0];

let formData = new FormData();
formData.append("file", file);

let response = await fetch("http://127.0.0.1:5000/upload-products", {
method: "POST",
body: formData
});

let data = await response.json();

console.log(data);   // console output
alert(JSON.stringify(data)); // popup output

}

</script>

</body>
</html>


10//////////////
from flask import Blueprint

auth_bp = Blueprint('auth', _name_)

from . import routes

11////////////
from flask import request, session, jsonify
from . import auth_bp

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")

    if not username:
        return jsonify({"error": "Username required"}), 400

    session['username'] = username

    return jsonify({
        "message": f"{username} logged in successfully"
    })


12/////////////////
from flask import Blueprint

products_bp = Blueprint('products', _name_)

from . import routes

13//////////////
from flask import jsonify, request, session, make_response
from . import products_bp

products = [
    {"id":1,"name":"Laptop","price":70000},
    {"id":2,"name":"Mouse","price":500},
    {"id":3,"name":"Keyboard","price":1200}
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


14////////////////
from flask import Flask
from auth import auth_bp
from products import products_bp

app = Flask(_name_)

app.secret_key = "secret123"

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(products_bp)

if _name_ == "_main_":
    app.run(debug=True)




