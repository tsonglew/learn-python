from flask import Flask, render_template
from redirect import RedirectForm
from wtforms import TextField, HiddenField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'


class LoginForm(RedirectForm):
    username = TextField('Username')
    password = TextField('Password')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return form.redirect('index')
    return render_template('login.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
