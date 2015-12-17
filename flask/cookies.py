from flask import Flask, request, make_response
app = Flask(__name__)


# reading cookies
@app.route('/')
def index():
    username = request.cookies.get('username')
    # use cookies.get(key) instead of cookies.get[key] to not get a
    # KeyError if the cookie is missing


# storing cookies
@app.route('/')
def index():
    resp = make_response(render_template(...))
    resp.set_cookies('username', 'the username')
    return resp
