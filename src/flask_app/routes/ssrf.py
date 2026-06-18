from flask import Blueprint, render_template, request
import requests

ssrf_bp = Blueprint('ssrf', __name__)

@ssrf_bp.route('/ssrf', methods=['GET', 'POST'])
def fetch_url():
    """
    ⚠️ INTENTIONALLY VULNERABLE ROUTE ⚠️
    Vulnerability: SSRF (Server-Side Request Forgery)
    Description: App fetches a user-provided URL without validation.
    """
    content = ""
    url = ""
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            # VULNERABLE: No validation of the URL
            response = requests.get(url, timeout=5)
            content = response.text
        except Exception as e:
            content = f"Error fetching URL: {str(e)}"
            
    return render_template('ssrf.html', content=content, url=url)
