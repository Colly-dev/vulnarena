from sqlalchemy import text
from ..app import db

def seed_data():
    """
    Seeds the database with initial demo data.
    """
    # Check if data already exists
    result = db.session.execute(text("SELECT count(*) FROM users")).fetchone()
    if result[0] > 0:
        return

    # Add users
    # ⚠️ WARNING: Using plaintext passwords for demonstration of SQLi auth bypass
    users = [
        (1, 'admin', 'P@ssw0rd123!', 'admin@vulnarena.local', 'Administrator'),
        (2, 'user1', 'password', 'user1@example.com', 'User'),
        (3, 'alice', 'alice123', 'alice@company.com', 'User'),
        (4, 'bob', 'bob456', 'bob@company.com', 'User')
    ]
    
    for u in users:
        db.session.execute(text(f"INSERT INTO users (id, username, password, email, role) VALUES ({u[0]}, '{u[1]}', '{u[2]}', '{u[3]}', '{u[4]}')"))
    
    db.session.commit()
