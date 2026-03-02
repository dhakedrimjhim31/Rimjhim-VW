from flask import Flask, render_template

app = Flask(__name__)

@app.route("/add/<int:num1>/<int:num2>")
def show_names():
    names = ['arun', 'amit', 'priya']
    return render_template("index.html", names = names)


if __name__ == "__main__":
    app.run(debug=True)

