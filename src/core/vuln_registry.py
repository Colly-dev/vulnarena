"""
VulnArena Vulnerability Registry
"""

VULNERABILITIES = {
    "sqli_auth_bypass": {
        "name": "SQL Injection (Auth Bypass)",
        "vulnerable_route": "/login",
        "secure_version": "src/secure_versions/secure_sql/prepared_statements.py",
        "description": "Bypassing login by injecting SQL into the username field."
    },
    "sqli_union": {
        "name": "SQL Injection (UNION-based)",
        "vulnerable_route": "/sqli",
        "secure_version": "src/secure_versions/secure_sql/prepared_statements.py",
        "description": "Extracting data using UNION SELECT statements."
    },
    "reflected_xss": {
        "name": "Reflected XSS",
        "vulnerable_route": "/xss",
        "secure_version": "src/secure_versions/secure_xss/output_encoding.py",
        "description": "Injecting scripts through URL parameters."
    },
    "csrf_email_change": {
        "name": "CSRF (Email Change)",
        "vulnerable_route": "/csrf",
        "secure_version": "src/secure_versions/secure_sessions/csrf_tokens.py",
        "description": "Changing user email without CSRF protection."
    }
}

def get_vuln_info(vuln_id):
    return VULNERABILITIES.get(vuln_id)
