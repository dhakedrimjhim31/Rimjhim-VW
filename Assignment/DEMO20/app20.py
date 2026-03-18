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



    
















###################################################################
Error:

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
11:18:19 PM [vite] (client) page reload web/index.html
11:18:19 PM [vite] (client) page reload index.html
11:18:19 PM [vite] vite.config.js changed, restarting server...
11:18:19 PM [vite] server restarted.
(!) Failed to run dependency scan. Skipping dependency pre-bundling. Error: The following dependencies are imported but could not be resolved:

  react (imported by C:/Users/Administrator/Desktop/P/src/App.jsx)
  react-dom/client (imported by C:/Users/Administrator/Desktop/P/src/main.jsx)
  react/jsx-dev-runtime (imported by C:/Users/Administrator/Desktop/P/src/App.jsx)

Are they installed?
    at file:///C:/Users/Administrator/Desktop/P/node_modules/vite/dist/node/chunks/node.js:31204:33
    at async file:///C:/Users/Administrator/Desktop/P/node_modules/vite/dist/node/chunks/node.js:23069:15

 *  History restored 

PS C:\Users\Administrator\Desktop\P> cd web
PS C:\Users\Administrator\Desktop\P\web> npm install

up to date, audited 153 packages in 2s

36 packages are looking for funding
  run `npm fund` for details

found 0 vulnerabilities
PS C:\Users\Administrator\Desktop\P\web> npm run dev

> p@0.0.0 dev
> vite

11:32:13 PM [vite] (client) Re-optimizing dependencies because vite config has changed

  VITE v8.0.0  ready in 611 ms

  ➜  Local:   http://localhost:5173/
  ➜  Network: use --host to expose
  ➜  press h + enter to show help
(!) Failed to run dependency scan. Skipping dependency pre-bundling. Error: The following dependencies are imported but could not be resolved:

  bootstrap/dist/css/bootstrap.min.css (imported by C:/Users/Administrator/Desktop/P/web/src/main.jsx)
  react-router-dom (imported by C:/Users/Administrator/Desktop/P/web/src/shared/layouts/Sidebar.jsx)
  prop-types (imported by C:/Users/Administrator/Desktop/P/web/src/shared/components/DataTable.jsx)
  axios (imported by C:/Users/Administrator/Desktop/P/web/src/core/api.js)
  lucide-react (imported by C:/Users/Administrator/Desktop/P/web/src/shared/layouts/Sidebar.jsx)

Are they installed?
    at file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:31204:33
    at async file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:23069:15
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "bootstrap/dist/css/bootstrap.min.css" from "src/main.jsx". Does the file exist?
  Plugin: vite:import-analysis
11:32:27 PM [vite] Internal server error: Failed to resolve import "bootstrap/dist/css/bootstrap.min.css" from "src/main.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/main.jsx:5:7
  3  |  import App from "./App";
  4  |  import { AppProvider } from "./core/store";
  5  |  import "bootstrap/dist/css/bootstrap.min.css";
     |          ^
  6  |  import "./styles.css";
  7  |  var _jsxFileName = "C:/Users/Administrator/Desktop/P/web/src/main.jsx";     
      at TransformPluginContext._formatLog (file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:30209:39)
      at TransformPluginContext.error (file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:30206:14)
      at normalizeUrl (file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:27496:18)
      at async file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:27559:30
      at async Promise.all (index 4)
      at async TransformPluginContext.transform (file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:27527:4)
      at async EnvironmentPluginContainer.transform (file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:29998:14)
      at async loadAndTransform (file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:24133:26)
      at async viteTransformMiddleware (file:///C:/Users/Administrator/Desktop/P/web/node_modules/vite/dist/node/chunks/node.js:24941:20)
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-rou
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/App.jsx". Does the file exist?
  Plugin: vite:import-analysis
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/features/auth/LoginPage.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/features/auth/LoginPage.jsx:2:34   
  1  |  import { useState } from "react";
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/features/auth/RegisterPage.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/features/auth/RegisterPage.jsx:2:3411:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/core/RequireAuth.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/core/RequireAuth.jsx:1:38
  1  |  import { Navigate, useLocation } from "react-router-dom";
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/shared/layouts/AppLayout.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/shared/layouts/AppLayout.jsx:3:23  
  1  |  import Sidebar from "./Sidebar";
  2  |  import Navbar from "./Navbar";
  3  |  import { Outlet } from "react-router-dom";
     |                          ^
  4  |  var _jsxFileName = "C:/Users/Administrator/Desktop/P/web/src/shared/layouts/AppLayout.jsx";
  5  |  import { jsxDEV as _jsxDEV } from "react/jsx-dev-runtime"; (x2)
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/core/router.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/core/router.jsx:1:36
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "prop-types" from "src/shared/components/DataTable.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/shared/components/DataTable.jsx:2:22
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/shared/layouts/Navbar.jsx". Does the file exist?
  Plugin: vite:import-analysis
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/shared/layouts/Sidebar.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/shared/layouts/Sidebar.jsx:1:25    
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/features/auth/RegisterPage.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/features/auth/RegisterPage.jsx:2:34  1  |  import { useState } from "react";
  2  |  import { Link, useNavigate } from "react-router-dom";
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/shared/layouts/AppLayout.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/shared/layouts/AppLayout.jsx:3:23  
  1  |  import Sidebar from "./Sidebar";
  2  |  import Navbar from "./Navbar";
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/features/auth/LoginPage.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/features/auth/LoginPage.jsx:2:34   
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/core/RequireAuth.jsx". Does the file exist?
  Plugin: vite:import-analysis
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "axios" from "src/core/api.js". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/core/api.js:1:18
  1  |  import axios from "axios";
     |                     ^
  2  |  const api = axios.create({
11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "lucide-react" from "src/shared/layouts/Sidebar.jsx". Does the file exist?
  Plugin: vite:import-analysis
  File: C:/Users/Administrator/Desktop/P/web/src/shared/layouts/Sidebar.jsx:8:7     
  1  |  import { NavLink } from "react-router-dom";
  2  |  import { useApp } from "../../core/useApp";
  3  |  import { LayoutDashboard, Package, ClipboardList, AlertCircle } from "lucide11:32:27 PM [vite] (client) Pre-transform error: Failed to resolve import "react-router-dom" from "src/shared/layouts/Navbar.jsx". Does the file exist?













###################################################################################
api error
PS C:\Users\Administrator\Desktop\P> cd api
PS C:\Users\Administrator\Desktop\P\api> python run.py
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\P\api\run.py", line 1, in <module>
    from app import create_app
  File "C:\Users\Administrator\Desktop\P\api\app\__init__.py", line 3, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'
PS C:\Users\Administrator\Desktop\P\api> flask run
Usage: flask run [OPTIONS]
Try 'flask run --help' for help.

Error: While importing 'app', an ImportError was raised:

Traceback (most recent call last):
  File "C:\Program Files\Python312\Lib\site-packages\flask\cli.py", line 245, in locate_app
    __import__(module_name)
  File "C:\Users\Administrator\Desktop\P\api\app\__init__.py", line 3, in <module>
    from dotenv import load_dotenv
ModuleNotFoundError: No module named 'dotenv'

PS C:\Users\Administrator\Desktop\P\api> 







##################################
error venv
Installing collected packages: python-dotenv, markupsafe, itsdangerous, colorama, blinker, werkzeug, jinja2, click, flask, flask-cors 
Successfully installed blinker-1.9.0 click-8.3.1 colorama-0.4.6 flask-3.1.3 flask-cors-6.0.2 itsdangerous-2.2.0 jinja2-3.1.6 markupsafe-3.0.3 python-dotenv-1.2.2 werkzeug-3.1.6

[notice] A new release of pip is available: 23.2.1 -> 26.0.1       
[notice] To update, run: python.exe -m pip install --upgrade pip   
(venv) PS C:\Users\Administrator\Desktop\P\api> python run.py
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\P\api\run.py", line 1, in <module>
    from app import create_app
  File "C:\Users\Administrator\Desktop\P\api\app\__init__.py", line 4, in <module>
    from flask_migrate import Migrate
ModuleNotFoundError: No module named 'flask_migrate'
(venv) PS C:\Users\Administrator\Desktop\P\api> 



