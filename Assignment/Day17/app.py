from flask import Flask, request, make_response, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")


@app.route("/welcome", methods = ["POST"])
def welcome():
    username = request.form.get("username")

    if not username:
        return "Name cannot be empty"
    
    count = request.cookies.get("count")

    if count:
        count = int(count) + 1
    else:
        count = 1


    response = make_response(f"""
        <h2>Welcome {username}!</h2>
        <p>You have visited this page {count} times.</p>
        <a href= "/welcome">Refresh</a>
    """)

    response.set_cookie("username", username)
    response.set_cookie("count", str(count))

    return response

@app.route("/welcome")
def visit_again():
    username = request.cookies.get("username")
    count = request.cookies.get("count")

    if not username:
        return "Please enter your name first"
    
    count = int(count) + 1 

    response = make_response(f"""
        <h2>Welcome {username}!</h2>
        <p>You have visited this page {count} times.</p>
        <a href= "/welcome">Refresh</a>
    """)

    response.set_cookie("count", str(count))
    return response

if __name__ == "__main__":
    app.run(debug=True)