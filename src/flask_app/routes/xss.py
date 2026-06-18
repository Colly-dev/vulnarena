from flask import Blueprint, render_template, request, Markup

xss_bp = Blueprint('xss', __name__)

@xss_bp.route('/xss', methods=['GET', 'POST'])
def reflected_xss():
    """
    ⚠️ INTENTIONALLY VULNERABLE ROUTE ⚠️
    Vulnerability: Reflected XSS
    Description: User input is rendered back to the page without escaping.
    Secure Version: See src/secure_versions/secure_xss/output_encoding.py
    """
    name = request.args.get('name', '')
    # VULNERABLE: Rendering raw input using Markup or disabling auto-escaping
    return render_template('search.html', xss_name=name)

@xss_bp.route('/xss/dom')
def dom_xss():
    """
    ⚠️ INTENTIONALLY VULNERABLE ROUTE ⚠️
    Vulnerability: DOM-based XSS
    """
    return render_template('dom_xss.html')
