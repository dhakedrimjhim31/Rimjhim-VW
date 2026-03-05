from flask import request, redirect, url_for, render_template
from . import hr

@hr.route("/dashboard")
def dashboard():
    role = request.cookies.get("role")
    if role != "hr":
        return redirect(url_for("auth.login"))
    username = request.cookies.get("username")

    return render_template("hr_dashboard.html", username=username)