from flask import Flask, render_template, request

app = Flask(__name__)

#In-memory product list
products_data = [
    {"name": "Laptop", "category": "Electronics", "price": 50000, "available": True},
    {"name": "Phone", "category": "Electronics", "price": 20000, "available": False},
    {"name": "Shoes", "category": "Fashion", "price": 3000, "available": True},
    {"name": "Watch", "category": "Fashion", "price": 5000, "available": True},
    {"name": "Tablet", "category": "Electronics", "price": 25000, "available": True},
]

@app.route("/products")
def products():

    #Get query parameters
    category = request.args.get("category")
    available = request.args.get("available")
    sort = request.args.get("sort")

    filtered_products = products_data

    #Filter by category
    if category:
        filtered_products = [
            p for p in filtered_products
            if p["category"].lower() == category.lower()
        ]

    #Filter by Availability
    if available:
        if available.lower() == "true":
            filtered_products = [p for p in filtered_products if p["available"]]
        elif available.lower() == "false":
            filtered_products = [p for p in filtered_products if not p["available"]]
    
    #Sort by Price
    if sort == "low":
        filtered_products = sorted(filtered_products, key= lambda x: x["price"])
    elif sort == "high":
        filtered_products = sorted(filtered_products, key=lambda x: x["price"], reverse=True)

    
    total_count = len(filtered_products)

    return render_template("products.html", 
                           products=filtered_products,
                           total=total_count)

if __name__ == "__main__":
    app.run(debug=True,port=3000)
