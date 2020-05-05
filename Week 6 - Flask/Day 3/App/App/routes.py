# First, we are in a different file, so we need to import the app
import flask
from App import app    # app.app is package_name.variable_name

@app.route("/")
def index():
    posts = [
        {"author":"John", "body":"I love python"},
        {"author":"Fish", "body":"I love water"},
        {"author":"Herpetolog", "body":"I love pythons"},
    ]
    return flask.render_template('index.html',posts=posts)