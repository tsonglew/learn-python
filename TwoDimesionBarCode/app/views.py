# coding: utf-8
from . import app
from flask import render_template
from qrcode import make


# test views
@app.route('/test/')
def test():
    return "<h1>just tell you everything is ok!</h1>"

# you can writing your views here
@app.route('/')
def index():
    img = make('http://www.baidu.com')
    return render_template('index.html', img=img)
