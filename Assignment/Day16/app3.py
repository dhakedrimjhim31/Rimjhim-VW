from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def show_students():
    students = [
        {"name": "John", "marks": 80},
        {"name": "amit", "marks": 70},
        {"name": "zara", "marks": 40},
    ]
    return render_template("student.html", students=students)

if __name__ == "__main__":
    app.run(debug=True)