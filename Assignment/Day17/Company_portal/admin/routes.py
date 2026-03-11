from flask import request, redirect, url_for, render_template
from . import admin

@admin.route("/dashboard")
def dashboard():
    role = request.cookies.get("role")
    if role != "admin":
        return redirect(url_for("auth.login"))
    username = request.cookies.get("username")

    return render_template("admin_dashboard.html", username=username)