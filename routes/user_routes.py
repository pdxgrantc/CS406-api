from flask import Flask, Blueprint, jsonify, request
from  google.cloud import datastore

user_bp = Blueprint("user", __name__)

db = datastore.Client()

@user_bp.route("/settings", methods=["GET"])
def get_user_settings():
    user_id = request.args.get("user_id")
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400

    key = db.key("UserSettings", user_id)
    entity = db.get(key)

    if not entity:
        return jsonify({"error": "User settings not found"}), 404

    return jsonify(entity)