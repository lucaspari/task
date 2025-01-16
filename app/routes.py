from bson import ObjectId
from flask import Blueprint, json, request, jsonify
from pymongo import MongoClient
from parser import parse_user_data_to_db, parse_user_data_to_server 
user_routes = Blueprint("user_routes", __name__)
client = MongoClient('mongodb://mongodb:27017/')
db = client['app']
users_collection = db['users']

def insertUsers():
    if users_collection.count_documents({}) == 0:
        with open('app/users.json') as f:
            users_data = json.load(f)
            user_objects = [parse_user_data_to_db(user_data) for user_data in users_data['users']]
            users_collection.insert_many([user.__dict__ for user in user_objects])

insertUsers()
        
        
@user_routes.route("/users", methods=["GET"])
def get_users():
    users = list(users_collection.find())
    user_objects = [parse_user_data_to_server(user) for user in users]
    return jsonify([user.__dict__ for user in user_objects]) 

@user_routes.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user_data = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user_data:
        return jsonify({"error": "User not found"}), 404
    user = parse_user_data_to_server(user_data)
    return jsonify(user.__dict__)

@user_routes.route("/users", methods=["POST"])
def create_user():
    try:
        data = request.get_json()
        
        if 'users' not in data:
            return jsonify({"error": "Invalid data format"}), 400
        
        user_objects = [parse_user_data_to_db(user_data) for user_data in data['users']]
        result = users_collection.insert_many([user.__dict__ for user in user_objects])
        return jsonify({"message": "Users added successfully", "ids": [str(id) for id in result.inserted_ids]}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_routes.route("/users/<username>", methods=["PUT"])
def update_user(username):
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data provided"}), 400
        
        user_data = parse_user_data_to_db(data)
        result = users_collection.update_one(
            {"username": username},
            {"$set": user_data.__dict__}
        )
        
        if result.matched_count == 0:
            return jsonify({"error": "User not found"}), 404
        
        return jsonify({"message": "User updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@user_routes.route("/users/<username>", methods=["DELETE"])
def delete_user(username):
    print(username)
    result = users_collection.delete_one({"username": username})
    if result.deleted_count == 0:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"message": "User deleted"})