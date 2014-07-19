from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello Chris!"

@app.route("/")
def index():
    return 'Index Page'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    # return 'Post %d' % post_id
    if post_id % 2 == 0:
    	message="Even"
    else:
    	message="Odd"
    return 'Post %d, this must be a %s number' % (post_id, message)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    # return 'User %s' % username
    return 'Hey %s welcome back!' % username

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# 
@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

if __name__ == "__main__":

    app.run(debug=True)