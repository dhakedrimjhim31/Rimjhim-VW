from flask import Blueprint, request, jsonify
from models.models import db, Event, Registration

event_bp = Blueprint("event_bp", __name__)

# Create event
@event_bp.route("/events", methods=["POST"])
def create_event():

    data = request.json

    event = Event(
        name=data["name"],
        total_seats=data["total_seats"],
        available_seats=data["total_seats"]
    )

    db.session.add(event)
    db.session.commit()

    return jsonify({"message": "Event created"})


# List events
@event_bp.route("/events", methods=["GET"])
def list_events():

    events = Event.query.all()

    result = []

    for e in events:
        result.append({
            "id": e.id,
            "name": e.name,
            "total_seats": e.total_seats,
            "available_seats": e.available_seats
        })

    return jsonify(result)


# Register user
@event_bp.route("/register/<int:event_id>", methods=["POST"])
def register(event_id):

    event = Event.query.get(event_id)

    if event.available_seats == 0:
        return jsonify({"message": "Event full"}), 400

    data = request.json

    registration = Registration(
        user_name=data["user_name"],
        event_id=event_id
    )

    event.available_seats -= 1

    db.session.add(registration)
    db.session.commit()

    return jsonify({"message": "Registration successful"})


# Full events
@event_bp.route("/events/full")
def full_events():

    events = Event.query.filter_by(available_seats=0).all()

    result = []

    for e in events:
        result.append({
            "id": e.id,
            "name": e.name
        })

    return jsonify(result)