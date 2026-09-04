import pytest
import app as flask_app


@pytest.fixture
def client():
    """Flask test client fixture."""
    flask_app.app.config["TESTING"] = True
    # Reset in-memory database before each test
    flask_app.users = {
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
    flask_app.next_user_id = 3
    
    with flask_app.app.test_client() as client:
        yield client


def test_home_route(client):
    """Test root endpoint returns welcome message and 200 status code."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert "message" in data
    assert data["status"] == "online"


def test_get_users(client):
    """Test retrieving list of all users."""
    response = client.get("/api/users")
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["count"] == 2
    assert len(data["users"]) == 2


def test_get_user_by_id_success(client):
    """Test retrieving a single existing user by ID."""
    response = client.get("/api/users/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["user"]["id"] == 1
    assert data["user"]["name"] == "Alice Smith"


def test_get_user_by_id_not_found(client):
    """Test retrieving a non-existent user returns 404."""
    response = client.get("/api/users/999")
    assert response.status_code == 404
    data = response.get_json()
    assert data["success"] is False
    assert "not found" in data["error"]


def test_create_user_success(client):
    """Test creating a user with valid payload."""
    payload = {
        "name": "Charlie Brown",
        "email": "charlie@example.com",
        "role": "Product Manager"
    }
    response = client.post("/api/users", json=payload)
    assert response.status_code == 201
    data = response.get_json()
    assert data["success"] is True
    assert data["user"]["id"] == 3
    assert data["user"]["name"] == "Charlie Brown"
    assert data["user"]["email"] == "charlie@example.com"
    assert data["user"]["role"] == "Product Manager"

    # Verify user was saved in-memory
    get_res = client.get("/api/users/3")
    assert get_res.status_code == 200


def test_create_user_missing_name(client):
    """Test creating user without required 'name' field fails with 400."""
    payload = {"email": "noname@example.com"}
    response = client.post("/api/users", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "name" in data["error"]


def test_create_user_missing_email(client):
    """Test creating user without required 'email' field fails with 400."""
    payload = {"name": "No Email User"}
    response = client.post("/api/users", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False
    assert "email" in data["error"]


def test_create_user_non_json_body(client):
    """Test POST request with non-JSON payload returns 400."""
    response = client.post("/api/users", data="not json", content_type="text/plain")
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False


def test_update_user_success(client):
    """Test updating existing user fields."""
    payload = {
        "name": "Alice Cooper",
        "role": "Lead Developer"
    }
    response = client.put("/api/users/1", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert data["user"]["name"] == "Alice Cooper"
    assert data["user"]["role"] == "Lead Developer"
    assert data["user"]["email"] == "alice@example.com"  # Unmodified field remains


def test_update_user_not_found(client):
    """Test updating a non-existent user returns 404."""
    payload = {"name": "Ghost User"}
    response = client.put("/api/users/999", json=payload)
    assert response.status_code == 404
    data = response.get_json()
    assert data["success"] is False


def test_update_user_invalid_name(client):
    """Test updating user with empty string name returns 400."""
    payload = {"name": "   "}
    response = client.put("/api/users/1", json=payload)
    assert response.status_code == 400
    data = response.get_json()
    assert data["success"] is False


def test_delete_user_success(client):
    """Test deleting an existing user."""
    response = client.delete("/api/users/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "deleted successfully" in data["message"]

    # Verify user no longer exists
    get_res = client.get("/api/users/1")
    assert get_res.status_code == 404


def test_delete_user_not_found(client):
    """Test deleting non-existent user returns 404."""
    response = client.delete("/api/users/999")
    assert response.status_code == 404
    data = response.get_json()
    assert data["success"] is False


def test_method_not_allowed(client):
    """Test invalid HTTP method on endpoint returns 405."""
    response = client.delete("/api/users")
    assert response.status_code == 405
    data = response.get_json()
    assert data["success"] is False
    assert "Method not allowed" in data["error"] or "method not allowed" in data["error"].lower()
