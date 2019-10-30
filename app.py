from flask import Flask, request, redirect, url_for, render_template, flash, send_file
import os
from werkzeug.utils import secure_filename
import basic

UPLOAD_FOLDER = 'static/video/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' in request.files:
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            basic.main(os.path.join(
                app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('processed', filename=filename))
    return render_template('index.html')


@app.route('/out')
def processed():
    return send_file('og.avi', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
