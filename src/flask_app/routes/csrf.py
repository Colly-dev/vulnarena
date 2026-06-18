from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..app import db
from sqlalchemy import text

csrf_bp = Blueprint('csrf', __name__)

@csrf_bp.route('/csrf', methods=['GET', 'POST'])
@login_required
def change_email():
    """
    ⚠️ INTENTIONALLY VULNERABLE ROUTE ⚠️
    Vulnerability: CSRF (Cross-Site Request Forgery)
    Description: Action performed without CSRF token validation.
    Secure Version: See src/secure_versions/secure_sessions/csrf_tokens.py
    """
    if request.method == 'POST':
        new_email = request.form.get('email')
        # VULNERABLE: No CSRF protection
        db.session.execute(text(f"UPDATE users SET email = '{new_email}' WHERE id = {current_user.id}"))
        db.session.commit()
        flash(f'Email updated to {new_email}!', 'success')
        return redirect(url_for('csrf.change_email'))
        
    return render_template('dashboard.html', user=current_user)
