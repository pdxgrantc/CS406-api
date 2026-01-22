import os
from datetime import datetime, timezone

from flask import Flask, request, jsonify
from flask_cors import CORS
from google.cloud import firestore

app = Flask(__name__)

# Allow requests from your frontend (adjust as needed)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000", "https://web-dot-YOUR-PROJECT.uc.r.appspot.com"]}})

# Firestore client (uses ADC / service account)
db = firestore.Client()

def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


@app.route("/")
def index():
	return "Hello, World!"

@app.post("/login")
def login():
    """
    Receives user data from frontend and stores it in Firestore.

    Expected JSON body (example):
    {
      "sub": "google-user-id",
      "email": "user@example.com",
      "name": "User Name",
      "picture": "https://...."
    }
    """
    req = request.get_json(silent=True) or {}
    data = req.get("data")

    print(f"Received login data: {data}")

    sub = data.get("sub")
    print (f"sub: {sub}")
    if not sub:
        return jsonify({"error": "Missing required field: sub"}), 400

    # Only allow fields you actually want to store (prevents junk writes)
    user_doc = {
        "sub": sub,
        "updatedAt": utc_now_iso(),
        "lastLoginAt": utc_now_iso(),
        "given_name": data.get("given_name"),
        "family_name": data.get("family_name"),
        "email": data.get("email"),
        "picture" : data.get("picture"), 
        "name": data.get("name")
    }

	

    # Use sub as the document id so it’s unique per Google account
    ref = db.collection("users").document(sub)

    # Upsert:
    # - if doc exists: update fields
    # - if doc doesn’t exist: create it
    # Also set createdAt only on first creation
    ref.set(
        {
            **user_doc,
            "createdAt": firestore.SERVER_TIMESTAMP,  # set once when created
        },
        merge=True
    )

    return jsonify({"status": "ok", "user_id": sub}), 200

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
