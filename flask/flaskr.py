# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
        abort, render_template, flash
from contextlib import closing


# configuration
# DATABASE = '/tmp/flaskr.db'
# DEBUG = True
# SECRET_KEY = 'development key'
# USERNAME = 'admin'
# PASSWORD = 'default'


# create our little application :)
app = Flask(__name__)
# app.config.from_envvar('FLASKR_SETTINGS', silent = True)


# def connect_db():
#     return sqlite3.connect(app.config['DATABASE'])


# def init_db():
#     with closing(connect_db()) as db:
#         with app.open_resource('shema.sql', mode = 'r') as f:
#             db.cursor().executescript(f.read())
#         db.commit()


# @app.before_request
# def before_request():
#     g.db = connect_db()


# @app.teardown_request
# def teardown_request(exception):
#     db = getattr(g, 'db', None)
#     if db is not None:
#         db.close()
#     g.db.close()

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
    return render_template('hello.html', name = name)


if __name__ == '__main__':
    app.run(debug = True)
