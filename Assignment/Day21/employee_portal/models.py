from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(50), unique=True)

    password = db.Column(db.String(100))

    role = db.Column(db.String(20))


class Employee(db.Model):

    __tablename__ = "employees"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))

    email = db.Column(db.String(100))

    department = db.Column(db.String(100))

    manager_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    manager = db.relationship("User", backref="team_members")
