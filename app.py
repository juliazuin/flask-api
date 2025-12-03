from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://admin:admin@mongodb:27017/usuarios?authSource=admin"
mongo = PyMongo(app)

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
        user['_id'] = str(user['_id']) # Convert ObjectId to string for JSON serialization
        users.append(user)
    return jsonify(users), 200


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")