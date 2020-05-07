from flask import Flask, render_template, flash, session, redirect, url_for
from _datetime import datetime

myapp = Flask(__name__)

@myapp.route('/')
def index():
    return render_template("index.html")

@myapp.route('/blah')
def blah():
    return redirect(url_for("index"))
# use name of method you want to run

@myapp.route('/home')
@myapp.route('/home/<username>')
def home(username="anonymous"):

    if username != "anonymous":
        flash(f"you are logged in as {username}", "success")
        flash(f"you are logged in at {datetime.now()}", "danger")
        # could do conditional redirect within routes
    else:
        flash(f"you are not logged in")
# could do redirect to login page

    return render_template("index.html", username=username)

@myapp.errorhandler(404)
def error_404(error):
    return render_template('404_error.html'), 404




if __name__ == "__main__":
    myapp.secret_key = "super_secret_key"
    myapp.run(debug=True)
