from flask import Blueprint, request, jsonify
from .models import User
from . import db

api_blueprint = Blueprint('api', __name__)

# Add User
@api_blueprint.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    try:
        user = User(name=data['name'], family=data['family'])
        db.session.add(user)
        db.session.commit()
        return jsonify({"id": user.id, "message": "User created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Get All Users
@api_blueprint.route('/users', methods=['GET'])
def get_users():
    try:
        users = User.query.all()
        return jsonify([{
            "id": u.id,
            "name": u.name,
            "family": u.family
        } for u in users])
    except Exception as e:
        return jsonify({"error": str(e)}), 500