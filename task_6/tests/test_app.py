import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SECRET_KEY'] = 'test-secret-key'
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test that index page loads successfully and contains key profile details."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Geetanjali Khurana" in response.data
    assert b"Python Developer" in response.data
    assert b"Flask Personal Portfolio Site" in response.data

def test_project_detail_success(client):
    """Test that existing project detail page loads successfully."""
    response = client.get('/project/1')
    assert response.status_code == 200
    assert b"Flask Personal Portfolio Site" in response.data
    assert b"Tech Stack" in response.data

def test_project_detail_not_found(client):
    """Test that requesting an invalid project ID returns 404."""
    response = client.get('/project/999')
    assert response.status_code == 404
    assert b"404" in response.data
    assert b"Page Not Found" in response.data

def test_contact_get_redirect(client):
    """Test that GET /contact redirects to homepage #contact section."""
    response = client.get('/contact')
    assert response.status_code == 302
    assert response.location.endswith('/#contact')

def test_contact_post_success(client):
    """Test valid contact form submission renders success template."""
    payload = {
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "subject": "Project Collaboration",
        "message": "Hello Geetanjali, I would love to discuss a Flask development opportunity with you."
    }
    response = client.post('/contact', data=payload, follow_redirects=True)
    assert response.status_code == 200
    assert b"Thank You, Jane Smith!" in response.data
    assert b"janesmith@example.com" in response.data
    assert b"Message Summary" in response.data

def test_contact_post_invalid_email(client):
    """Test form submission with invalid email displays error flash."""
    payload = {
        "name": "Jane Smith",
        "email": "invalid-email-address",
        "subject": "Inquiry",
        "message": "This is a test message that is long enough."
    }
    response = client.post('/contact', data=payload, follow_redirects=True)
    assert response.status_code == 200
    assert b"Please provide a valid email address." in response.data

def test_contact_post_short_message(client):
    """Test form submission with too short message displays error flash."""
    payload = {
        "name": "Jane Smith",
        "email": "jane@example.com",
        "subject": "Inquiry",
        "message": "Too short"
    }
    response = client.post('/contact', data=payload, follow_redirects=True)
    assert response.status_code == 200
    assert b"Message must be at least 10 characters long." in response.data

def test_custom_404_handler(client):
    """Test that requesting an unmapped URL returns 404 custom template."""
    response = client.get('/unknown-page')
    assert response.status_code == 404
    assert b"404" in response.data
    assert b"Page Not Found" in response.data
