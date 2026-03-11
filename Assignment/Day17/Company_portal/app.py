from flask import Flask

from auth import auth
from admin import admin
from hr import hr
from employee import employee

app = Flask(__name__)

app.register_blueprint(auth)
app.register_blueprint(admin)
app.register_blueprint(hr)
app.register_blueprint(employee)

if __name__ == "__main__":
    app.run(debug=True, port=3000)