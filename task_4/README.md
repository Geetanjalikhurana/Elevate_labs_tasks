# Task 4: Build a REST API with Flask

**Elevate Labs - Python Developer Internship**

A clean, modular, and fully-tested RESTful API built with Python and Flask for managing user data. This application implements standard CRUD (Create, Read, Update, Delete) routes with JSON payload validation, standardized HTTP status code responses, in-memory storage, and an automated `pytest` test suite.

---

## 📌 Features

- **Full RESTful CRUD Operations**:
  - `GET /api/users` - List all users.
  - `GET /api/users/<id>` - Retrieve details for a specific user.
  - `POST /api/users` - Create a new user with unique ID assignment.
  - `PUT /api/users/<id>` - Update details of an existing user.
  - `DELETE /api/users/<id>` - Remove a user by ID.
- **In-Memory Data Store**: Fast, lightweight dictionary-based persistence.
- **Robust Input Validation & Error Handling**: Returns clean JSON error messages for invalid formats, missing required fields, resource non-existence (404), and method errors (405).
- **Automated Unit Testing**: 14 unit and integration test cases using `pytest` ensuring 100% pass rate.

---

## 📁 Repository Structure

```
task_4/
│
├── app.py              # Main Flask application with API endpoints & error handlers
├── test_app.py         # Automated pytest test suite covering all routes & edge cases
├── requirements.txt    # Project dependencies (Flask, pytest)
└── README.md           # Documentation, API reference, & Interview Q&A
```

---

## 🚀 Quick Start Guide

### 1. Prerequisites
- Python 3.8+ installed on your system.

### 2. Install Dependencies
Open your terminal in the project directory and run:
```bash
pip install -r requirements.txt
```

### 3. Run the Flask Application
Start the development server:
```bash
python app.py
```
By default, the API will run locally at: `http://127.0.0.1:5000/`

---

## 🧪 Running Automated Tests

Run the `pytest` test suite to verify all endpoints and error cases:
```bash
python -m pytest test_app.py -v
```

---

## 📖 API Endpoint Reference

| Method | Endpoint | Description | Status Code (Success) |
| :--- | :--- | :--- | :--- |
| `GET` | `/` | API Health & Overview | `200 OK` |
| `GET` | `/api/users` | Retrieve all users | `200 OK` |
| `GET` | `/api/users/<id>` | Retrieve a user by ID | `200 OK` |
| `POST` | `/api/users` | Create a new user | `201 Created` |
| `PUT` | `/api/users/<id>` | Update user by ID | `200 OK` |
| `DELETE`| `/api/users/<id>` | Delete user by ID | `200 OK` |

---

## 💻 Sample Requests & Responses

### 1. Health Check Endpoint
- **Request**: `GET /`
- **Response (`200 OK`)**:
```json
{
  "endpoints": {
    "DELETE /api/users/<id>": "Delete a user by ID",
    "GET /api/users": "Fetch all users",
    "GET /api/users/<id>": "Fetch a specific user by ID",
    "POST /api/users": "Create a new user (requires 'name' and 'email' in JSON body)",
    "PUT /api/users/<id>": "Update user details by ID"
  },
  "message": "Welcome to the Flask User Management REST API!",
  "status": "online"
}
```

### 2. Fetch All Users
- **Request**: `GET /api/users`
- **Response (`200 OK`)**:
```json
{
  "count": 2,
  "success": true,
  "users": [
    {
      "email": "alice@example.com",
      "id": 1,
      "name": "Alice Smith",
      "role": "Software Developer"
    },
    {
      "email": "bob@example.com",
      "id": 2,
      "name": "Bob Jones",
      "role": "UI/UX Designer"
    }
  ]
}
```

### 3. Create New User
- **Request**: `POST /api/users`
- **Headers**: `Content-Type: application/json`
- **Body**:
```json
{
  "name": "Charlie Brown",
  "email": "charlie@example.com",
  "role": "Product Manager"
}
```
- **Response (`201 Created`)**:
```json
{
  "message": "User created successfully.",
  "success": true,
  "user": {
    "email": "charlie@example.com",
    "id": 3,
    "name": "Charlie Brown",
    "role": "Product Manager"
  }
}
```

### 4. Update Existing User
- **Request**: `PUT /api/users/1`
- **Body**:
```json
{
  "name": "Alice Cooper",
  "role": "Lead Developer"
}
```
- **Response (`200 OK`)**:
```json
{
  "message": "User with ID 1 updated successfully.",
  "success": true,
  "user": {
    "email": "alice@example.com",
    "id": 1,
    "name": "Alice Cooper",
    "role": "Lead Developer"
  }
}
```

### 5. Delete User
- **Request**: `DELETE /api/users/1`
- **Response (`200 OK`)**:
```json
{
  "message": "User 'Alice Smith' (ID: 1) deleted successfully.",
  "success": true
}
```

---

## 🛠️ Testing with cURL Commands

You can test the API endpoints directly from your command line using `curl`:

```bash
# GET all users
curl -X GET http://127.0.0.1:5000/api/users

# GET single user by ID
curl -X GET http://127.0.0.1:5000/api/users/1

# POST create a user
curl -X POST http://127.0.0.1:5000/api/users \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"David Miller\", \"email\": \"david@example.com\", \"role\": \"QA Engineer\"}"

# PUT update user details
curl -X PUT http://127.0.0.1:5000/api/users/1 \
  -H "Content-Type: application/json" \
  -d "{\"role\": \"Senior Architect\"}"

# DELETE a user
curl -X DELETE http://127.0.0.1:5000/api/users/2
```

---

## 📚 Interview Questions & Answers

### 1. What is Flask?
**Answer**: Flask is a lightweight WSGI web application framework written in Python. It is classified as a "microframework" because it does not require particular tools or libraries, keeping the core simple yet extensible. Flask provides essential web development features like routing, HTTP request handling, and templating (via Jinja2) while allowing developers complete freedom to choose their database ORM, validation libraries, and project design pattern.

### 2. What is REST?
**Answer**: REST (Representational State Transfer) is an architectural style for designing networked applications. RESTful web services use standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`) to perform operations on resources identified by URIs (e.g., `/api/users/1`). Key constraints of REST include:
- **Statelessness**: Every request contains all necessary context; the server stores no client session state.
- **Client-Server Architecture**: Separation of concerns between UI/client and data storage/server.
- **Uniform Interface**: Standardized resource representation (typically JSON or XML).

### 3. Difference between GET and POST?
**Answer**:
- **`GET`**: Used to retrieve data from a server. `GET` requests should be **safe and idempotent** (making multiple identical requests produces the same result without modifying server state). Data is sent in the URL query string.
- **`POST`**: Used to submit data to the server to create a new resource. `POST` requests are **non-idempotent** (sending the request multiple times creates multiple resources). Data is sent inside the HTTP request body.

### 4. How does a Flask route work?
**Answer**: Flask uses the `@app.route()` decorator to bind a URL pattern to a Python function (called a view function). When a request hits the Flask application server:
1. Flask matches the incoming URL path and HTTP method against registered URL rules in Werkzeug's routing map.
2. If a match is found (e.g., `@app.route('/api/users/<int:user_id>')`), Flask extracts path parameters, converts types if specified (e.g., integer `user_id`), and executes the associated view function.
3. The view function returns a response object (or tuple of content and status code), which Flask converts into an HTTP response.

### 5. What is `request.json`?
**Answer**: In Flask, `request.json` (or `request.get_json()`) is an attribute of the global `request` object that automatically parses incoming HTTP request body data formatted as `application/json` into a Python dictionary or list. If the request body is not valid JSON or the `Content-Type` header is missing/incorrect, `request.get_json(silent=True)` returns `None` without raising an unhandled exception.

### 6. What are status codes like 200, 404?
**Answer**: HTTP status codes indicate the result of a client's request:
- **`200 OK`**: Request succeeded; data returned.
- **`201 Created`**: Resource successfully created (`POST`).
- **`400 Bad Request`**: Malformed request payload or missing required parameters.
- **`404 Not Found`**: The requested URL or resource ID does not exist on the server.
- **`405 Method Not Allowed`**: Endpoint exists but does not accept the HTTP method used (e.g., `DELETE /api/users`).
- **`500 Internal Server Error`**: Unexpected server-side failure.

### 7. How do you run a Flask app?
**Answer**: There are two main ways to run a Flask app:
1. **Direct Execution**: Calling `app.run(debug=True)` in Python and executing `python app.py`.
2. **Flask CLI**: Setting the environment variable `export FLASK_APP=app.py` (or `$env:FLASK_APP="app.py"` in PowerShell) and running `flask run`.
In production, Flask apps are executed via WSGI servers like Gunicorn or uWSGI behind a reverse proxy like Nginx.

### 8. What is JSON?
**Answer**: JSON (JavaScript Object Notation) is a lightweight, text-based data-interchange format that is human-readable and machine-parseable. It represents structured data using two main structures: key-value pairs (objects `{}`) and ordered lists of values (arrays `[]`). JSON is language-independent and serves as the standard format for web API communication.

### 9. How to test an API?
**Answer**:
- **Automated Testing**: Writing test scripts using frameworks like `pytest` combined with Flask's built-in `test_client()` to programmatically simulate HTTP requests and assert expected status codes and JSON payloads.
- **Manual Testing**: Sending requests interactively using tools like **Postman**, **Insomnia**, **Hoppscotch**, or command-line tools like **cURL**.

### 10. Can we use a database instead of memory?
**Answer**: Yes, absolutely. While in-memory storage (like a Python dictionary) is suitable for rapid prototyping and testing, real-world production APIs store data in persistent databases. We can replace the dictionary store with:
- **Relational Databases (SQL)**: SQLite, PostgreSQL, MySQL using Flask-SQLAlchemy (ORM).
- **NoSQL Databases**: MongoDB using PyMongo or Flask-MongoEngine.
Using an ORM provides persistent storage, ACID compliance, data migrations (via Alembic/Flask-Migrate), and complex query capabilities.
