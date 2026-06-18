"""
⚠️ CRITICAL WARNING ⚠️
================================================================================
VulnArena is an INTENTIONALLY VULNERABLE web application designed SOLELY for:
- Security education and training
- Penetration testing practice
- AppSec research in isolated environments

⚠️ DO NOT deploy this application on public-facing servers or production environments.
================================================================================
"""

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
import yaml

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    config_path = os.path.join(os.path.dirname(__file__), '../../config/config.yaml')
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    
    app.config['SECRET_KEY'] = config.get('flask', {}).get('secret_key', 'dev-key-very-insecure')
    app.config['SQLALCHEMY_DATABASE_URI'] = config.get('database', {}).get('uri', 'sqlite:///vulnarena.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.debug = config.get('flask', {}).get('debug', True)

    # Initialize extensions with app
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    CORS(app)

    # Register Blueprints
    from .routes.auth import auth_bp
    from .routes.sqli import sqli_bp
    from .routes.xss import xss_bp
    from .routes.csrf import csrf_bp
    from .routes.ssrf import ssrf_bp
    from .routes.idor import idor_bp
    from .routes.uploads import uploads_bp
    from .routes.admin import admin_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(sqli_bp)
    app.register_blueprint(xss_bp)
    app.register_blueprint(csrf_bp)
    app.register_blueprint(ssrf_bp)
    app.register_blueprint(idor_bp)
    app.register_blueprint(uploads_bp)
    app.register_blueprint(admin_bp)

    @app.route('/')
    def index():
        return render_template('dashboard.html')

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('error.html', error="404 - Page Not Found"), 404

    # Initialize database
    with app.app_context():
        from .database.init_db import init_db
        from .database.seed_data import seed_data
        init_db()
        seed_data()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000)
