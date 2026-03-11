from flask import Flask, render_template, request

app = Flask(__name__)

#Sample employee data
employees = [
    {"name": "John", "department": "IT", "salary": 60000},
    {"name": "Amit", "department": "HR", "salary": 50000},
    {"name": "Zara", "department": "Manager", "salary": 90000},
]

@app.route("/dashboard")
def dashboard():
    role = request.args.get("role", "employee").lower()

    return render_template(
        "dashboard.html",
        role= role,
        employees=employees
    )

if __name__ == "__main__":
    app.run(debug=True,port=5000)