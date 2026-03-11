from flask import Flask, render_template, request, redirect, session
from config import Config
from models import db, User, Employee
from decorators import role_required
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
            return "Invalid login"

    return render_template("login.html")


@app.route("/employees")
@role_required("admin","manager")
def employees():

    if session["role"] == "admin":

        data = Employee.query.all()

    else:

        data = Employee.query.filter_by(manager_id=session["user_id"]).all()

    return render_template("employees.html", employees=data)


@app.route("/employee/<int:id>")
def view_employee(id):

    emp = Employee.query.get(id)

    return render_template("profile.html", emp=emp)


@app.route("/employee/<int:id>/edit", methods=["GET","POST"])
def edit_employee(id):

    emp = Employee.query.get(id)

    if session["role"] == "manager" and emp.manager_id != session["user_id"]:
        return "Access Denied"

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


@app.route("/add_user", methods=["GET","POST"])
@role_required("admin")
def add_user():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]
        role = request.form["role"]

        new_user = User(username=username,password=password,role=role)

        db.session.add(new_user)
        db.session.commit()

        return redirect("/employees")

    return render_template("add_user.html")


if __name__ == "__main__":
    app.run(debug=True)