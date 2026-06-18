import os
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from werkzeug.utils import secure_filename

uploads_bp = Blueprint('uploads', __name__)

@uploads_bp.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """
    ⚠️ INTENTIONALLY VULNERABLE ROUTE ⚠️
    Vulnerability: Insecure File Upload
    Description: Allows uploading any file type to the server.
    """
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        
        # VULNERABLE: No extension validation
        filename = secure_filename(file.filename)
        upload_folder = os.path.join(current_app.root_path, 'static/uploads')
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        
        file.save(os.path.join(upload_folder, filename))
        flash(f'File {filename} uploaded successfully to static/uploads/{filename}', 'success')
        
    return render_template('upload.html')
