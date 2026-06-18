from flask import Blueprint, render_template, request
from ..app import db
from sqlalchemy import text

sqli_bp = Blueprint('sqli', __name__)

@sqli_bp.route('/sqli', methods=['GET', 'POST'])
def sqli_search():
    """
    ⚠️ INTENTIONALLY VULNERABLE ROUTE ⚠️
    Vulnerability: SQL Injection (UNION-based)
    Description: User input is directly concatenated into the SQL query.
    Secure Version: See src/secure_versions/secure_sql/prepared_statements.py
    """
    results = []
    query_str = ""
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        # VULNERABLE: Direct string concatenation
        query_str = f"SELECT id, username, email FROM users WHERE id = {user_id}"
        try:
            # Using text() with direct string is still vulnerable to SQLi
            result_proxy = db.session.execute(text(query_str))
            results = result_proxy.fetchall()
        except Exception as e:
            return render_template('search.html', error=str(e), query=query_str)

    return render_template('search.html', results=results, query=query_str)
