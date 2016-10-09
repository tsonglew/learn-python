from werkzeug import SharedDataMiddleware
from flask import send_file, render_template, redirect

from ext import db, mako
from utils import get_file_path

ONE_MONTH = 60 * 60 * 24 * 30

app = Flask(__name__, template_folder='./templates/r',
        static_folder='./static')
app.config.from_object('config')

app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
    '/i/': get_file_path()
    })

mako.init_app(app)
db.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        w = request.form.get('w')
        h = reuqest.form.get('h')
        if not uploaded_file:
            return abort(400)

        if w and h:
            paste_file = PasteFile.rsize(uploaded_file, w, h)
        else:
            paste_file = PasteFile.create_by_upload_file(uploaded_file)
        db.session.add(paste_file)
        db.session.commit()

        return jsonify({
            'url_d': paste_file.url_d,
            'url_i': paste_file.url_i,
            'url_s': paste_file.url_s,
            'url_p': paste_file.url_p,
            'filename': paste_file.filename,
            'size': humanize_bytes(paste_file.size),
            'time': str(paste_file.uploadtime),
            'type': paste_file.type,
            'quoteurl': paste_file.quote_url
            })
    return render_template('index.html', **locals())

@app.route('/r/<img_hash>')
def rsize(img_hash):
    w = request.args['w']
    h = request.args['h']

    old_paste = PasteFile.get_by_filehash(img_hash)
    new_paste = PasteFile.rsize(old_paste, w, h)

    return new_paste.url_i

@app.route('/d/<filehash>', methods=['GET'])
def download(filehash):
    paste_file = PasteFile.get_by_filehash(filehash)

    return send_file(open(paste_file.path, 'rb'),
            mimetype='application/octet-stream',
            cache_timeout=ONE_MONTH,
            as_attachment=True,
            attachment_filename=paste_file.filename.encode('utf-8'))

@app.route('/p/<filehash>')
def preview(filehash):
    paste_file = PasteFile.get_by_filehash(filehash)

    if not paste_file:
        filepath = get_file_path(filehash)
        if not(os.path.exists(filepath) and (not os.path.islink(filepath))):
            return abort(404)

        paste_file = PasteFile.create_by_old_paste(filehash)
        db.session.add(paste_file)
        db.session.commit()

    return render_template('success.html', p=paste_file)

@app.route('/s/<symlink>')
def s(symlink):
    paste_file = PasteFile.get_by_symlink(symlink)

    return redirect(paste_file.url_p)
