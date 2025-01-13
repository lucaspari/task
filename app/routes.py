from dataclasses import asdict
from bson import ObjectId
from flask import Blueprint, request,jsonify
from pymongo import MongoClient
user_routes = Blueprint("user_routes", __name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['app']
users_collection = db['users']



@user_routes.route("/users", methods=["GET"])
def get_users():
    users = list(users_collection.find())
    for user in users:
        user["_id"] = str(user["_id"])
    return jsonify(users)

@user_routes.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user_data = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user_data:
        return jsonify({"error": "User not found"}), 404
    user_data["_id"] = str(user_data["_id"])
    return jsonify(user_data)

@user_routes.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        
        if 'users' not in data:
            return jsonify({"error": "Invalid data format"}), 400
        
        result = users_collection.insert_many(data['users'])
        return jsonify({"message": "Users added successfully", "ids": [str(id) for id in result.inserted_ids]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
@user_routes.route("/users/<user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.json
    try:
        updated_fields = {}
        if "username" in data:
            updated_fields["username"] = data["username"]
        if "password" in data:
            updated_fields["password"] = data["password"]
        if "roles" in data:
            updated_fields["roles"] = data["roles"]
        if "preferences" in data:
            updated_fields["preferences"] = data["preferences"]
        if "active" in data:
            updated_fields["active"] = data["active"]
        result = users_collection.update_one(
            {"_id": ObjectId(user_id)}, {"$set": updated_fields}
        )
        if result.matched_count == 0:
            return jsonify({"error": "User not found"}), 404
        return jsonify({"message": "User updated"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@user_routes.route("/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    result = users_collection.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"})