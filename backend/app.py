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
