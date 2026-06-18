from sqlalchemy import text
from ..app import db

def init_db():
    """
    Initializes the database schema.
    """
    # Create users table
    db.session.execute(text("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            email TEXT,
            role TEXT NOT NULL
        )
    """))
    
    # Create posts table for XSS
    db.session.execute(text("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            author TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """))
    
    db.session.commit()
