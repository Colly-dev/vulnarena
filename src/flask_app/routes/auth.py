from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from ..app import db, login_manager
from sqlalchemy import text

auth_bp = Blueprint('auth', __name__)

class User:
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role
        self.is_authenticated = True
        self.is_active = True
        self.is_anonymous = False
    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    # Simplified for the lab
    result = db.session.execute(text(f"SELECT id, username, role FROM users WHERE id = {user_id}")).fetchone()
    if result:
        return User(result[0], result[1], result[2])
    return None

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    ⚠️ INTENTIONALLY VULNERABLE ROUTE ⚠️
    Vulnerability: SQL Injection (Auth Bypass)
    """
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # VULNERABLE: SQL Injection in login query
        query = f"SELECT id, username, role FROM users WHERE username = '{username}' AND password = '{password}'"
        user_data = db.session.execute(text(query)).fetchone()
        
        if user_data:
            user = User(user_data[0], user_data[1], user_data[2])
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials', 'danger')
            
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))
