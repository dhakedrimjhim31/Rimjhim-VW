from flask import request, session, jsonify
from . import auth_bp

@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get("username")

    if not username:
        return jsonify({"error": "Username required"}), 400

    session['username'] = username

    return jsonify({
        "message": f"{username} logged in successfully"
    })