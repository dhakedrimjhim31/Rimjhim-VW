Python Full Stack Training
Day 20:


######## 1:
mysql> CREATE USER 'flaskuser'@'localhost' IDENTIFIED BY 'root';
Query OK, 0 rows affected (0.17 sec)
 
mysql> GRANT ALL PRIVILEGES ON fsd.* TO 'flaskuser'@'localhost';
Query OK, 0 rows affected (0.02 sec)
 
mysql> FLUSH PRIVILEGES;
Query OK, 0 rows affected (0.03 sec)

#############2:
APP.py:

from flask import Flask,session,render_template,jsonify,request,redirect,url_for,make_response,request
from flask_sqlalchemy import SQLAlchemy
 
app=Flask(__name__)
 
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://flaskuser:root@localhost/fsd"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
 
db=SQLAlchemy(app)
 
class Student(db.Model):
    __tablename__="students"
 
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))
    course=db.Column(db.String(100))
    email=db.Column(db.String(100),unique=True)
 
with app.app_context():
    db.create_all()
 
@app.route("/add",methods=["GET","POST"])
def add_student():
    if request.method=="POST":
        name=request.form["name"]
        course=request.form["course"]
        email=request.form["email"]
        student=Student(name=name,course=course,email=email)
        db.session.add(student)
        db.session.commit()
        return redirect("/")
    return render_template("add_student.html")
 
@app.route("/")
def index():
    students=Student.query.all()
    return render_template("index.html",students=students)
 
@app.route("/edit/<int:id>")
def edit_student(id):
    student=Student.query.get(id)
    return render_template("edit_student.html",student=student)
 
@app.route("/update/<int:id>",methods=["POST"])
def update_student(id):
    student=Student.query.get(id)
    student.name=request.form["name"]
    student.course=request.form["course"]
    student.email=request.form["email"]
    db.session.commit()
    return redirect("/")
@app.route("/delete/<int:id>")
def delete_student(id):
    student=Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect("/")
 
 
 
 
 
if __name__=="__main__":
    app.run(debug=True)
 
 
####
INDEX.HTML:
<a href="/add">Add student</a>
<table border="2">
    <tr>
        <th>Name</th>
        <th>Course</th>
        <th>Email</th>
        <th colspan="2">Action</th>
 
    </tr>
    {% for s in students %}
    <tr>
        <td>{{s.name}}</td>
        <td>{{s.course}}</td>
        <td>{{s.email}}</td>
        <td><a href="/edit/{{s.id}}">Edit</a></td>
        <td><a href="/delete/{{s.id}}">Delete</a></td>
    </tr>
    {% endfor %}
 
</table>
 

###
add_student.html:

<form method="post">
    <input type="text" name="name">
    <br>
    <input type="text" name="course">
    <br>
    Email:
    <input type="email" name="email">
    <br>
    <input type="submit" value="Add">
 
</form>


###
edit_student.html:

<form method="post" action="/update/{{student.id}}">
    <input type="text" name="name" value="{{student.name}}">
    <input type="text" name="course" value="{{student.course}}">
    <input type="email" name="email" value="{{student.email}}">
    <input type="submit" value="Update">
</form>







#############################ASSIGNMENT 1
class Config:
    SECRET_KEY = "secret123"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@localhost/employee_portal"

    SQLALCHEMY_TRACK_MODIFICATIONS = False



from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True)

    password = db.Column(db.String(100))

    role = db.Column(db.String(20))



class Employee(db.Model):

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100))

    department = db.Column(db.String(100))

    manager_id = db.Column(db.Integer, db.ForeignKey('users.id'))  




from functools import wraps
from flask import session, redirect, url_for


def role_required(*roles):

    def wrapper(func):

        @wraps(func)
        def decorated_function(*args, **kwargs):

            if "role" not in session:
                return redirect(url_for("login"))

            if session["role"] not in roles:
                return "Access Denied"

            return func(*args, **kwargs)

        return decorated_function

    return wrapper    





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






<form method="POST">

Username:
<input type="text" name="username">

Password:
<input type="password" name="password">

<button type="submit">Login</button>

</form>





<h2>Employee List</h2>

{% for e in employees %}

<p>

{{e.name}} - {{e.department}}

<a href="/employee/{{e.id}}">View</a>

<a href="/employee/{{e.id}}/edit">Edit</a>

<a href="/employee/{{e.id}}/delete">Delete</a>

</p>

{% endfor %}











<h2>Employee Profile</h2>

<p><b>Name:</b> {{ emp.name }}</p>
<p><b>Email:</b> {{ emp.email }}</p>
<p><b>Department:</b> {{ emp.department }}</p>
<p><b>Manager ID:</b> {{ emp.manager_id }}</p>

<a href="/employees">Back to Employees</a>








<h2>Edit Employee</h2>

<form method="POST">

Name:
<input type="text" name="name" value="{{ emp.name }}">
<br><br>

Email:
<input type="text" name="email" value="{{ emp.email }}">
<br><br>

Department:
<input type="text" name="department" value="{{ emp.department }}">
<br><br>

<button type="submit">Update</button>

</form>

<a href="/employees">Back</a>
