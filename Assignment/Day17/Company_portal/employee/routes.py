from flask import request, redirect, url_for, render_template
from . import employee

@employee.route("/dashboard")
def dashboard():
    role = request.cookies.get("role")
    if role != "employee":
        return redirect(url_for("auth.login"))
    username = request.cookies.get("username")

    return render_template("employee_dashboard.html", username=username)