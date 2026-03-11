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



    























###############################ASSIGNMENT 1:

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/task_manager"
SQLALCHEMY_TRACK_MODIFICATIONS = False



from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime)













    from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Task
import datetime

app = Flask(__name__)
app.config.from_pyfile("config.py")

db.init_app(app)
CORS(app)


# CREATE TASK
@app.route("/tasks", methods=["POST"])
def create_task():

    data = request.json

    task = Task(
        title=data["title"],
        priority=data["priority"],
        completed=False,
        created_at=datetime.datetime.now()
    )

    db.session.add(task)
    db.session.commit()

    return jsonify({"message":"Task Created"})


# VIEW + FILTER TASKS
@app.route("/tasks", methods=["GET"])
def get_tasks():

    priority = request.args.get("priority")
    completed = request.args.get("completed")

    query = Task.query

    if priority:
        query = query.filter_by(priority=priority)

    if completed:
        query = query.filter_by(completed=(completed=="true"))

    tasks = query.order_by(Task.created_at.desc()).all()

    result=[]

    for t in tasks:
        result.append({
            "id":t.id,
            "title":t.title,
            "priority":t.priority,
            "completed":t.completed,
            "created_at":t.created_at
        })

    return jsonify(result)


# TOGGLE TASK
@app.route("/tasks/<int:id>", methods=["PUT"])
def toggle_task(id):

    task = Task.query.get(id)

    task.completed = not task.completed

    db.session.commit()

    return jsonify({"message":"Updated"})


# DELETE TASK
@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):

    task = Task.query.get(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message":"Deleted"})


if __name__ == "__main__":
    app.run(debug=True)



















import axios from "axios";

const API = "http://localhost:5000";

export const getTasks = (params) => axios.get(`${API}/tasks`,{params});
export const createTask = (data) => axios.post(`${API}/tasks`,data);
export const toggleTask = (id) => axios.put(`${API}/tasks/${id}`);
export const deleteTask = (id) => axios.delete(`${API}/tasks/${id}`);








import {useState} from "react";
import {createTask} from "./api";

function TaskForm({reload}){

const [title,setTitle]=useState("");
const [priority,setPriority]=useState("Low");

const submit=async(e)=>{
e.preventDefault();

await createTask({title,priority});

setTitle("");

reload();
}

return(

<form onSubmit={submit}>

<input
value={title}
onChange={(e)=>setTitle(e.target.value)}
placeholder="Task Title"
/>

<select
value={priority}
onChange={(e)=>setPriority(e.target.value)}
>

<option>Low</option>
<option>Medium</option>
<option>High</option>

</select>

<button>Add Task</button>

</form>

)

}

export default TaskForm;


























function Filters({priority,setPriority,completed,setCompleted}){

return(

<div>

<select
value={priority}
onChange={(e)=>setPriority(e.target.value)}
>

<option value="">All Priority</option>
<option value="Low">Low</option>
<option value="Medium">Medium</option>
<option value="High">High</option>

</select>

<label>

<input
type="checkbox"
checked={completed}
onChange={(e)=>setCompleted(e.target.checked)}
/>

Completed

</label>

</div>

)

}

export default Filters;


























function TaskTable({tasks,toggleTask,deleteTask}){

return(

<table border="1">

<thead>
<tr>
<th>Title</th>
<th>Priority</th>
<th>Status</th>
<th>Action</th>
</tr>
</thead>

<tbody>

{tasks.map(t=>(
<tr key={t.id}>

<td>{t.title}</td>
<td>{t.priority}</td>

<td>
<input
type="checkbox"
checked={t.completed}
onChange={()=>toggleTask(t.id)}
/>
</td>

<td>
<button onClick={()=>deleteTask(t.id)}>Delete</button>
</td>

</tr>
))}

</tbody>

</table>

)

}

export default TaskTable;













import {useState,useEffect} from "react";
import TaskForm from "./TaskForm";
import TaskTable from "./TaskTable";
import Filters from "./Filters";
import {getTasks,toggleTask,deleteTask} from "./api";

function App(){

const [tasks,setTasks]=useState([]);
const [priority,setPriority]=useState("");
const [completed,setCompleted]=useState(false);

const loadTasks=async()=>{

const params={}

if(priority) params.priority=priority
if(completed) params.completed=true

const res=await getTasks(params)

setTasks(res.data)

}

useEffect(()=>{
loadTasks()
},[priority,completed])

return(

<div>

<h1>Task Manager</h1>

<TaskForm reload={loadTasks}/>

<Filters
priority={priority}
setPriority={setPriority}
completed={completed}
setCompleted={setCompleted}
/>

<TaskTable
tasks={tasks}
toggleTask={async(id)=>{
await toggleTask(id)
loadTasks()
}}
deleteTask={async(id)=>{
await deleteTask(id)
loadTasks()
}}
/>

</div>

)

}

export default App;








    
