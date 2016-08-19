# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, url_for
from redirect_urls import is_safe_url, get_redirect_target, redirect_back

app = Flask(__name__)

@app.route('/')
def index():
    return 'this is index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    next = get_redirect_target()
    if request.method == 'POST':
        # login code here
        return redirect_back(url_for("index"))
    return render_template('index.html', next=next)

if __name__ == '__main__':
    app.run(debug=True)
