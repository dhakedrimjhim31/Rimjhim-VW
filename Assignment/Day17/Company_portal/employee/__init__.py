from flask import Blueprint

employee = Blueprint("employee", __name__, url_prefix="/employee")

from . import routes