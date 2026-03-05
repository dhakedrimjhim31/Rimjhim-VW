from flask import render_template, request, redirect, url_for, make_response
from datetime import timedelta
from . import auth

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/submit", methods=["POST"])
def submit():
    username = request.form["username"]
    role = request.form["role"]
    remember = request.form.get("remember")

    if role not in ["admin", "hr", "employee"]:
        return redirect(url_for("auth.login"))

    if role == "admin":
        redirect_to = url_for("admin.dashboard")
    elif role == "hr":
        redirect_to = url_for("hr.dashboard")
    else:
        redirect_to = url_for("employee.dashboard")

    response = make_response(redirect(redirect_to))

    if remember:
        response.set_cookie("username", username, max_age=60*60*24*7)
        response.set_cookie("role", role, max_age=60*60*24*7)
    else:
        response.set_cookie("username", username)
        response.set_cookie("role", role)

    return response

@auth.route("/logout")
def logout():
    response = make_response(redirect(url_for("auth.login")))
    response.delete_cookie("username")
    response.delete_cookie("role")
    return response