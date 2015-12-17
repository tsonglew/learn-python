# upload files
from flask import request, Flask
from werkzeug import secure_filename
app = Flask(__name__)


@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
