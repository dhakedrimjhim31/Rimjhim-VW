from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form.html")

@app.route("/register", methods=["GET"])
def register():
    username = request.args.get("username")
    email = request.args.get("email")
    password = request.args.get("password")

    # 1. Fields should not be blank
    if not username or not email or not password:
        return "Error: Fields should not be blank"
    
    # 2. Email should contain @
    if "@" not in email:
        return "Error: Email should contain '@' symbol"

    # 3. Password length validation
    if len(password) < 5 or len(password) > 8:
        return "Error: Password must be between 5 and 8 characters"
    
    return "Form submitted successfully!"


if __name__ == "__main__":
    app.run(debug=True)
    