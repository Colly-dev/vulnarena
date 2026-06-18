from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..app import db
from sqlalchemy import text

idor_bp = Blueprint('idor', __name__)

@idor_bp.route('/idor/<int:user_id>')
@login_required
def view_user(user_id):
    """
    ⚠️ INTENTIONALLY VULNERABLE ROUTE ⚠️
    Vulnerability: IDOR (Insecure Direct Object Reference)
    Description: No check if the current user is authorized to view user_id's data.
    """
    # VULNERABLE: No authorization check
    user_data = db.session.execute(text(f"SELECT id, username, email, role FROM users WHERE id = {user_id}")).fetchone()
    
    if user_data:
        return render_template('idor.html', profile=user_data)
    else:
        flash('User not found', 'danger')
        return redirect(url_for('index'))
