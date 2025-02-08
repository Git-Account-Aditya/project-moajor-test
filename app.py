from flask import Flask, request, jsonify, render_template, url_for
from werkzeug.utils import secure_filename
import numpy as np
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def default():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file found in request'}), 400

    image = request.files['image']

    if image.filename == '':
        return jsonify({'error': 'No selected image'}), 400

    # Save the image with a secure filename
    image_path = os.path.join(UPLOAD_FOLDER, secure_filename(image.filename))
    image.save(image_path)

    # Normalize the path for JSON response
    normalized_path = image_path.replace("\\", "/")
    
    # Render template and pass the image path for display
    return render_template('submit.html', image=normalized_path)


@app.route('/services', methods=['GET'])
def services():
    return jsonify({'services': ['Super Resolution', 'Tools', 'Blury Image']})


if __name__ == '__main__':
    app.run(debug = True)