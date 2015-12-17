from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])    # escape() to do escaping for you
    return 'You are not logged in'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action = "" method = "post">
            <p><input type = text name = username>
            <p><input type = submit value = Login>
        </form>
        '''

@app.route('/logout')
def logout():
    # delete the username if it exists
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key
app.secret_key = 'AOZr98j/3yX R~XHH!jmN]LWX/,?RT'
