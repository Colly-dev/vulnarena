"""
VulnArena Report Engine
"""

import os
from jinja2 import Template

REPORT_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Pentest Report - VulnArena</title>
    <style>
        body { font-family: sans-serif; padding: 40px; }
        .vulnerability { border: 1px solid #ccc; padding: 20px; margin-bottom: 20px; }
        .high { color: red; }
    </style>
</head>
<body>
    <h1>VulnArena Penetration Test Report</h1>
    <p>Target: Localhost Lab</p>
    <hr>
    {% for vuln in findings %}
    <div class="vulnerability">
        <h2 class="high">{{ vuln.name }}</h2>
        <p><strong>Status:</strong> VULNERABLE</p>
        <p><strong>Description:</strong> {{ vuln.description }}</p>
        <p><strong>Remediation:</strong> {{ vuln.remediation }}</p>
    </div>
    {% endfor %}
</body>
</html>
"""

def generate_report(findings, output_path="docs/reports/sample_report.html"):
    template = Template(REPORT_TEMPLATE)
    html_content = template.render(findings=findings)
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(html_content)
    print(f"[+] Report generated at {output_path}")
