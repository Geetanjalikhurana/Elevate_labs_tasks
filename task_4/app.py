from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database storing users keyed by ID
users = {
    1: {
        "id": 1,
        "name": "Alice Smith",
        "email": "alice@example.com",
        "role": "Software Developer"
    },
    2: {
        "id": 2,
        "name": "Bob Jones",
        "email": "bob@example.com",
        "role": "UI/UX Designer"
    }
}
next_user_id = 3


@app.route("/", methods=["GET"])
def home():
    """Root route providing API welcome message and documentation overview."""
    return jsonify({
        "message": "Welcome to the Flask User Management REST API!",
        "status": "online",
        "endpoints": {
            "GET /api/users": "Fetch all users",
            "GET /api/users/<id>": "Fetch a specific user by ID",
            "POST /api/users": "Create a new user (requires 'name' and 'email' in JSON body)",
            "PUT /api/users/<id>": "Update user details by ID",
            "DELETE /api/users/<id>": "Delete a user by ID"
        }
    }), 200


@app.route("/api/users", methods=["GET"])
def get_users():
    """Retrieve all users in the system."""
    user_list = list(users.values())
    return jsonify({
        "success": True,
        "count": len(user_list),
        "users": user_list
    }), 200


@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Retrieve a single user by ID."""
    user = users.get(user_id)
    if not user:
        return jsonify({
            "success": False,
            "error": f"User with ID {user_id} not found."
        }), 404
    
    return jsonify({
        "success": True,
        "user": user
    }), 200


@app.route("/api/users", methods=["POST"])
def create_user():
    """Create a new user."""
    global next_user_id

    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({
            "success": False,
            "error": "Invalid payload format. JSON request body is required."
        }), 400

    name = data.get("name")
    email = data.get("email")
    role = data.get("role", "User")  # Default role if unspecified

    if not name or not isinstance(name, str) or not name.strip():
        return jsonify({
            "success": False,
            "error": "Field 'name' is required and must be a non-empty string."
        }), 400

    if not email or not isinstance(email, str) or not email.strip():
        return jsonify({
            "success": False,
            "error": "Field 'email' is required and must be a non-empty string."
        }), 400

    new_user = {
        "id": next_user_id,
        "name": name.strip(),
        "email": email.strip(),
        "role": role.strip() if isinstance(role, str) else "User"
    }

    users[next_user_id] = new_user
    created_id = next_user_id
    next_user_id += 1

    return jsonify({
        "success": True,
        "message": "User created successfully.",
        "user": new_user
    }), 201


@app.route("/api/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Update an existing user's details by ID."""
    if user_id not in users:
        return jsonify({
            "success": False,
            "error": f"User with ID {user_id} not found."
        }), 404

    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({
            "success": False,
            "error": "Invalid payload format. JSON request body is required."
        }), 400

    user = users[user_id]

    if "name" in data:
        name = data["name"]
        if not isinstance(name, str) or not name.strip():
            return jsonify({
                "success": False,
                "error": "Field 'name' must be a non-empty string."
            }), 400
        user["name"] = name.strip()

    if "email" in data:
        email = data["email"]
        if not isinstance(email, str) or not email.strip():
            return jsonify({
                "success": False,
                "error": "Field 'email' must be a non-empty string."
            }), 400
        user["email"] = email.strip()

    if "role" in data:
        role = data["role"]
        if isinstance(role, str) and role.strip():
            user["role"] = role.strip()

    return jsonify({
        "success": True,
        "message": f"User with ID {user_id} updated successfully.",
        "user": user
    }), 200


@app.route("/api/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Delete a user by ID."""
    if user_id not in users:
        return jsonify({
            "success": False,
            "error": f"User with ID {user_id} not found."
        }), 404

    deleted_user = users.pop(user_id)
    return jsonify({
        "success": True,
        "message": f"User '{deleted_user['name']}' (ID: {user_id}) deleted successfully."
    }), 200


@app.errorhandler(404)
def not_found_handler(error):
    return jsonify({
        "success": False,
        "error": "Endpoint or resource not found."
    }), 404


@app.errorhandler(405)
def method_not_allowed_handler(error):
    return jsonify({
        "success": False,
        "error": "HTTP method not allowed for this route."
    }), 405


@app.errorhandler(500)
def internal_error_handler(error):
    return jsonify({
        "success": False,
        "error": "An internal server error occurred."
    }), 500


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
