from flask import jsonify, request
from .db import mongo
import app


users_collection = mongo.db.users


@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.json
    users_collection.insert_one(user_data)
    return jsonify({"message": "User created successfully"}), 201


@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in users_collection.find():
        # Convert ObjectId to string for JSON serialization
        user['_id'] = str(user['_id'])
        users.append(user)
    return jsonify(users), 200
