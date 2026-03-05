from flask import Blueprint

hr = Blueprint("hr", __name__, url_prefix="/hr")

from . import routes