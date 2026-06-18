"""
✅ SECURE IMPLEMENTATION ✅
Module: SQL Injection Prevention
Description: Uses parameterized queries (prepared statements) to prevent SQL injection.
"""

from sqlalchemy import text

def secure_user_search(db_session, user_id):
    """
    Securely searches for a user by ID using parameterized queries.
    """
    # SECURE: Using bound parameters
    query = text("SELECT id, username, email FROM users WHERE id = :user_id")
    result = db_session.execute(query, {"user_id": user_id})
    return result.fetchall()

def secure_login(db_session, username, password):
    """
    Securely authenticates a user using parameterized queries.
    Note: In a real app, you should also hash passwords!
    """
    # SECURE: Using bound parameters
    query = text("SELECT id, username, role FROM users WHERE username = :username AND password = :password")
    result = db_session.execute(query, {"username": username, "password": password})
    return result.fetchone()
