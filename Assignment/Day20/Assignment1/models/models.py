from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    total_seats = db.Column(db.Integer)
    available_seats = db.Column(db.Integer)


class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100))
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))