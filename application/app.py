from flask import jsonify, request
from .db import mongo


def home():
    return "Welcome to the User API"


def create_user():
    user_data = request.json
    mongo.db.users.insert_one(user_data)
    return jsonify({"message": "User created successfully"}), 201


def get_users():
    users = []
    for user in mongo.db.users.find():
        # Convert ObjectId to string for JSON serialization
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users), 200


def healthcheck():
    response = mongo.db.healthcheck.find_one({"status": "healthy"})

    if response:
        return "Healthy", 200
    else:
        mongo.db.healthcheck.insert_one({"status": "healthy"})
        return "Healthy", 200
