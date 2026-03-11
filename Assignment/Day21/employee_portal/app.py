from flask import Flask, render_template, request, redirect, session
from models import db, User, Employee
from decorators import role_required
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)



@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]

        password = request.form["password"]

        user = User.query.filter_by(username=username,password=password).first()

        if user:

            session["user_id"] = user.id

            session["role"] = user.role

            return redirect("/employees")

        else:

            return "Invalid Login"

    return render_template("login.html")



@app.route("/employees")
@role_required("admin","manager")
def employees():

    data = Employee.query.all()

    return render_template("employees.html", employees=data)



@app.route("/employee/<int:id>")
def view_employee(id):

    emp = Employee.query.get(id)

    return render_template("profile.html", emp=emp)



@app.route("/employee/<int:id>/edit", methods=["GET","POST"])
def edit_employee(id):

    emp = Employee.query.get(id)

    if request.method == "POST":

        emp.name = request.form["name"]

        emp.email = request.form["email"]

        emp.department = request.form["department"]

        db.session.commit()

        return redirect("/employees")

    return render_template("edit_employee.html", emp=emp)



@app.route("/employee/<int:id>/delete")
@role_required("admin")
def delete_employee(id):

    emp = Employee.query.get(id)

    db.session.delete(emp)

    db.session.commit()

    return redirect("/employees")



if __name__ == "__main__":
    app.run(debug=True)





