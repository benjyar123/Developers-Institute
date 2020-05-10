import flask
import json
import flask_wtf
import wtforms

app = flask.Flask(__name__)

@app.route('/')
@app.route('/home')
def home():

	html = flask.render_template("home.html")

	return html

@app.route('/main')
def main():

	html = flask.render_template("main.html")

	return html

@app.route('/cart')
def cart():

	html = flask.render_template("cart.html")

	return html


if __name__ == "__main__":
	app.secret_key = "super_secret_key"
	app.run(debug=True)
