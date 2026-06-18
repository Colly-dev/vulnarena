from flask import Blueprint, render_template, flash, redirect, url_for
from flask_login import login_required, current_user

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/admin')
@login_required
def admin_panel():
    """
    ⚠️ INTENTIONALLY VULNERABLE ROUTE ⚠️
    Vulnerability: Broken Access Control
    Description: Weak check for admin privileges.
    """
    # VULNERABLE: Only checking if role string contains 'admin'
    if 'admin' not in current_user.role.lower():
        flash('Access Denied: Admins Only', 'danger')
        return redirect(url_for('index'))
        
    return render_template('admin.html')
