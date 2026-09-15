import os
import re
from flask import Flask, render_template, request, redirect, url_for, flash, abort

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "elevate-labs-task-6-secret-key-2026")

# Portfolio Data Model (In-Memory Database)
PROFILE_DATA = {
    "name": "Geetanjali Khurana",
    "title": "Python & Backend Developer Intern",
    "bio": "Passionate Python developer specializing in Flask web applications, RESTful APIs, data structures, and clean software architecture.",
    "location": "New Delhi, India",
    "email": "geetanjali@example.com",
    "github": "https://github.com/Geetanjalikhurana",
    "linkedin": "https://linkedin.com/in/geetanjalikhurana",
    "skills": [
        {"name": "Python", "category": "Backend", "level": "Advanced"},
        {"name": "Flask", "category": "Web Framework", "level": "Advanced"},
        {"name": "Jinja2", "category": "Templating", "level": "Intermediate"},
        {"name": "HTML5 / CSS3", "category": "Frontend", "level": "Intermediate"},
        {"name": "JavaScript", "category": "Frontend", "level": "Intermediate"},
        {"name": "SQLite / SQL", "category": "Database", "level": "Intermediate"},
        {"name": "Git & GitHub", "category": "DevOps", "level": "Intermediate"},
        {"name": "Pytest", "category": "Testing", "level": "Intermediate"}
    ]
}

PROJECTS_DATA = [
    {
        "id": 1,
        "title": "Flask Personal Portfolio Site",
        "category": "Web Development",
        "description": "A dynamic portfolio website built with Flask, Jinja2 templates, and responsive CSS with interactive contact form processing.",
        "technologies": ["Python", "Flask", "Jinja2", "HTML5", "CSS3", "JavaScript"],
        "github": "https://github.com/Geetanjalikhurana/Elevate_labs_tasks",
        "demo": "#",
        "featured": True
    },
    {
        "id": 2,
        "title": "RESTful Task Management API",
        "category": "Backend Service",
        "description": "A secure REST API using Flask-RESTful and SQLite for task scheduling, user authentication, and data validation.",
        "technologies": ["Python", "Flask", "SQLite", "Pytest", "JWT"],
        "github": "https://github.com/Geetanjalikhurana/Elevate_labs_tasks",
        "demo": "#",
        "featured": True
    },
    {
        "id": 3,
        "title": "Automated Web Data Scraper",
        "category": "Data Engineering",
        "description": "Python CLI tool and scraper built with BeautifulSoup and Pandas to extract, clean, and export structured dataset records.",
        "technologies": ["Python", "BeautifulSoup4", "Pandas", "Requests"],
        "github": "https://github.com/Geetanjalikhurana/Elevate_labs_tasks",
        "demo": "#",
        "featured": False
    }
]

EXPERIENCE_DATA = [
    {
        "role": "Python Developer Intern",
        "company": "Elevate Labs",
        "period": "2026 - Present",
        "highlights": [
            "Developed responsive web applications using Flask, Jinja2, and CSS3.",
            "Implemented form handling, server-side data validation, and clean template inheritance.",
            "Wrote unit test suites using Pytest to achieve robust test coverage."
        ]
    }
]

# Helper function to validate email
def is_valid_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(regex, email) is not None

@app.route("/")
def index():
    """Renders the main portfolio landing page."""
    return render_template(
        "index.html",
        profile=PROFILE_DATA,
        projects=PROJECTS_DATA,
        experiences=EXPERIENCE_DATA
    )

@app.route("/project/<int:project_id>")
def project_detail(project_id):
    """Renders detailed page for a specific project."""
    project = next((p for p in PROJECTS_DATA if p["id"] == project_id), None)
    if not project:
        abort(404)
    return render_template("project_detail.html", profile=PROFILE_DATA, project=project)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Handles contact form display and POST form submissions."""
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        subject = request.form.get("subject", "").strip()
        message = request.form.get("message", "").strip()

        # Validation
        errors = []
        if not name:
            errors.append("Please provide your name.")
        if not email or not is_valid_email(email):
            errors.append("Please provide a valid email address.")
        if not subject:
            errors.append("Please provide a message subject.")
        if not message or len(message) < 10:
            errors.append("Message must be at least 10 characters long.")

        if errors:
            for error in errors:
                flash(error, "danger")
            return render_template("index.html", profile=PROFILE_DATA, projects=PROJECTS_DATA, experiences=EXPERIENCE_DATA, form_data=request.form)

        # Success case - pass submission data to success page
        contact_submission = {
            "name": name,
            "email": email,
            "subject": subject,
            "message": message
        }
        flash("Thank you! Your message has been received successfully.", "success")
        return render_template("contact_success.html", profile=PROFILE_DATA, submission=contact_submission)

    # GET request redirects to home section
    return redirect(url_for("index") + "#contact")

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 error page handler."""
    return render_template("404.html", profile=PROFILE_DATA), 404

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
