import os
from couplinganalyzer.app import app
from flask import request
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = {'zip'}

class InvalidFileError(Exception):
    """A simple Exception class for handling invalid files"""
    pass

def allowed_file(filename):
    '''checks the file extension of the uploaded file.'''
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def upload_file():
    '''try to upload the file to the server and return the local file path if
    successful'''
    if 'zipfile' not in request.files:
        raise InvalidFileError('No file part')

    file = request.files['zipfile']
    if file.filename == '':
        raise InvalidFileError('No selected file')

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)

        # for simplicity's sake, the uploads folder is simply relative to the
        # app.py file, in the same folder
        abs_name = os.path.join(app.root_path,
                        app.config['UPLOAD_FOLDER'], filename)
        file.save(abs_name)
        return abs_name
    else:
        raise InvalidFileError('Invalid file format')
