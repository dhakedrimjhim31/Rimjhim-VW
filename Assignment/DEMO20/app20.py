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



    

