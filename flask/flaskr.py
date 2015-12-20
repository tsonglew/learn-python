# all the imports
import sqlite3, os
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing


# create application
app = Flask(__name__)


# configuration
app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'flaskr.db'), 
    DEBUG = True,
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent = True)    # specify a confg file to be loaded which will overide the default values


# connect to the database specified.
#def connect_db():
#    rv = sqlite3.connect(app.config['DATABASE'])
#    rv.row_factory = sqlite3.Row
#    return rv


# create a function to initialize the database
#def init_db():
#    with closing(connect_db()) as db:    # closing() helper function allows us to keep a connection open for the duration of the with block
#        with app.open_resource('shema.sql', mode = 'r') as f:
#            db.cursor().executescript(f.read())
#        db.commit()


# before_request() call function before a request and it will pass no arguments
# after_request() call after request and it will pass the response that will be sent to the client
#@app.before_request
#def before_request():
#    g.db = connect_db()


# get called after the response has been constructed. They are not allowed to
# modify the request, and their return values are ignored. If an exception
# occurred while the request was being processed, it is passed to each
# function; otherwise, None is passed in.
#@app.teardown_request
#def teardown_request(exception):
#    db = getattr(g, 'db', None)
#    if db is not None:
#        db.close()
#    g.db.close()



# pass the entries as dicts to the show_entries.html template and return the
# rendered one

#@app.route('/')
#def show_entries():
#    cur = g.db.execute('select title, text from entries order by id desc')
#    entries = [dict(title = row[0], text = row[1]) for row in cur.fetchall()]
#    return render_template('show_entries.html, entries = entries')


# login
#@app.route('/login', method = ['GET', 'POST'])
#def login():
#    error = None
#    if request.method == 'POST':
#        if request.form['username'] != app.config['USERNAME']:
#            error = 'Invalid username'
#        elif request.form['password'] != app.config['PASSWORD']:
#            error = 'Invalid password'
#        else:
#            session['logged_in'] = True
#            flash('You were logged in')
#            return redirect(url_for('show_entries'))
#        return render_template('login.html', error = error)

# log out
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/hello')
@app.route('/hello/<name>')
def hello (name = None):
    return render_template('hello.html', name = name)


if __name__ == '__main__':
    app.run(debug = True)
