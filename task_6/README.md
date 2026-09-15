# Task 6: Build a Portfolio Website with Flask

**Elevate Labs — Python Developer Internship**

---

## 📌 Project Overview
This repository contains a full-featured personal portfolio web application built with **Flask**, **Jinja2**, **HTML5**, **CSS3**, and **JavaScript**. The application showcases profile details, dynamic skill lists, project highlights, internship experience, and an interactive contact form with server-side validation and dynamic success notifications.

---

## ✨ Key Features
- **Dynamic Routing**: Clean Flask route definitions for home (`/`), project detail views (`/project/<id>`), contact submission (`/contact`), and custom 404 error handling.
- **Jinja2 Template Inheritance**: Modular template hierarchy utilizing a parent layout (`base.html`) extended by views (`index.html`, `project_detail.html`, `contact_success.html`, `404.html`).
- **Interactive Web Forms & Validation**: Handles HTTP `POST` form submissions, performs regex email and field length validation, flashes alert messages, and renders summary output.
- **Static Assets Serving**: Organized CSS custom properties (`static/css/style.css`) and client-side JavaScript (`static/js/main.js`) served via Flask's `url_for('static', ...)`.
- **Automated Pytest Suite**: 8 unit tests in `tests/test_app.py` validating route HTTP status codes, form submissions, edge cases, and custom error handlers.

---

## 📁 Project Directory Structure
```
task_6/
├── app.py                  # Main Flask application entry point with route handlers & logic
├── requirements.txt        # Python package dependencies (Flask, pytest)
├── static/
│   ├── css/
│   │   └── style.css       # Responsive stylesheet with custom CSS variables & components
│   └── js/
│       └── main.js         # Mobile nav toggle, live form validation, flash auto-dismiss
├── templates/
│   ├── base.html           # Base Jinja2 layout with navbar, flash alerts, and footer
│   ├── index.html          # Portfolio home page (Hero, About, Skills, Projects, Experience, Form)
│   ├── project_detail.html # Individual project detail view (Dynamic parameter routing demo)
│   ├── contact_success.html# Submission confirmation & data summary view
│   └── 404.html            # Custom page-not-found error template
├── tests/
│   └── test_app.py         # Pytest automated test suite
└── README.md               # Project documentation & Answers to Interview Questions
```

---

## 🚀 Setup & Execution Guide

### Prerequisites
- Python 3.8+ installed on your system.

### 1. Installation
Clone the repository and navigate into the `task_6` directory:
```bash
git clone https://github.com/Geetanjalikhurana/Elevate_labs_tasks.git
cd task_6
```

Create and activate a Python virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 2. Running the Flask Web Server
Execute `app.py` to start the local development server:
```bash
python app.py
```
Open your web browser and navigate to:
```
http://127.0.0.1:5000/
```

### 3. Running Automated Unit Tests
To run the automated pytest test suite:
```bash
pytest -v
```

---

## 🧠 Interview Questions & Answers

### 1. What is a template in Flask?
> A **template** in Flask is an external file (typically written in HTML combined with template tags) that separates the user interface / presentation layer from the Python application logic. Instead of hardcoding HTML strings inside Python functions, Flask loads HTML files from the `templates/` folder and dynamically inserts variable data into them before serving them to the client.

### 2. What’s Jinja2?
> **Jinja2** is the default template engine used by Flask. It allows developers to generate dynamic HTML pages using Python-like expressions. Core Jinja2 syntax includes:
> - `{{ variable }}`: Interpolates variable values.
> - `{% logic %}`: Executes control flow logic like loops (`{% for ... %}`) and conditionals (`{% if ... %}`).
> - `{# comment #}`: Contains template comments that are not rendered in the final HTML.
> - **Template Inheritance**: Enables creating a `base.html` template that child templates extend (`{% extends "base.html" %}`).

### 3. How do you pass data to a template?
> Data is passed to a template by providing keyword arguments to Flask's `render_template()` function inside a route view function:
> ```python
> @app.route('/')
> def home():
>     user_name = "Geetanjali"
>     user_skills = ["Python", "Flask", "SQL"]
>     return render_template('index.html', name=user_name, skills=user_skills)
> ```
> Inside `index.html`, these passed variables can be accessed using `{{ name }}` and looped over using `{% for skill in skills %}`.

### 4. How are forms handled in Flask?
> Forms in Flask are handled by defining routes that accept the `POST` HTTP method (in addition to or instead of `GET`).
> 1. In the HTML form, specify `method="POST"` and set the `action` attribute to the target route (e.g., `action="{{ url_for('contact') }}"`).
> 2. Inside the Flask route, import `request` from `flask` and extract input values via `request.form.get('field_name')` or `request.form['field_name']`.
> 3. Perform server-side validation and return appropriate success/error responses or flash messages.

### 5. What is `render_template()`?
> `render_template()` is a built-in Flask function provided by the `flask` module. It searches the `templates/` directory for a specified HTML file, parses any Jinja2 tags or expressions embedded inside it using context data provided via keyword arguments, and returns the rendered HTML string along with an HTTP response status code (defaulting to `200 OK`).

### 6. How to style your app?
> Flask apps are styled using CSS stylesheets (along with images and JavaScript files) stored in the `static/` directory. You link static stylesheets in Jinja2 templates using Flask's `url_for()` helper:
> ```html
> <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
> ```
> This ensures correct URL path generation regardless of application mounting or deployment configurations.

### 7. What’s POST vs GET method in forms?
> - **GET Method**: Appends form data directly to the URL string as query parameters (e.g., `/search?q=flask`). It is idempotent, bookmarkable, and visible in browser history. It should **never** be used for sensitive data or operations that modify server state.
> - **POST Method**: Sends form data inside the HTTP request body. It is non-idempotent, does not expose data in the URL, supports large payloads (like file uploads), and is used for actions that change data on the server (e.g., submitting contact forms, creating user accounts).

### 8. What are static files?
> **Static files** are assets that do not change dynamically per user request. Examples include CSS files, JavaScript scripts, images (`.jpg`, `.png`, `.svg`), fonts, and static PDFs. In Flask, static files are placed in the `static/` folder and served directly by the web server via the `/static/` route.

### 9. How is routing done in Flask?
> Routing in Flask maps URL paths to specific Python view functions using the `@app.route()` decorator.
> ```python
> @app.route('/')
> def index():
>     return render_template('index.html')

> @app.route('/user/<username>')  # Dynamic URL variable rule
> def show_user_profile(username):
>     return f"User: {username}"
> ```
> Flask supports dynamic parameter converters like `<int:id>`, `<string:name>`, and method restrictions via `methods=['GET', 'POST']`.

### 10. Can Flask serve HTML/CSS/JS?
> **Yes, absolutely!** Flask is designed specifically to serve HTML templates from the `templates/` folder and CSS/JS static files from the `static/` folder. For production deployments, Flask often sits behind a reverse proxy web server (such as Nginx or Apache) or a WSGI server (such as Gunicorn or Waitress) which handles static file serving at high throughput while Flask processes dynamic Python application requests.

---

## 📜 License & Acknowledgments
Created as part of the **Elevate Labs Python Developer Internship** program (Task 6).
