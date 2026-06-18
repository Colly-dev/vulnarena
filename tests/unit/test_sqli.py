import pytest
from src.flask_app.app import create_app, db
from sqlalchemy import text

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
    })
    
    with app.app_context():
        db.create_all()
        db.session.execute(text("INSERT INTO users (id, username, password, email, role) VALUES (1, 'admin', 'pass', 'a@b.com', 'admin')"))
        db.session.commit()
        yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_sqli_auth_bypass(client):
    """Test that SQLi auth bypass works as intended in the lab."""
    payload = {
        'username': "admin' --",
        'password': 'wrong_password'
    }
    response = client.post('/login', data=payload, follow_redirects=True)
    assert b"Logged in successfully" in response.data
