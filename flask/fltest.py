from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello Muxi!'

# show the user profile for that user
@app.route('/user/<username>')
def show_user_profile(username):
    return 'Welcome! User %s!' % username


# show the post with the given id, the id is an integer
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


if __name__ == '__main__':
    app.run(debug = True)
