import flask
import json

# import other modules?

app = flask.Flask(__name__)



@app.route('/')
def index():

	html = flask.render_template("index.html")

	return html

@app.route('/products')
def products():

	# MODEL fetching data from db
	with open("product_db.json", "r") as f:
		data = json.load(f)

	# MODEL processing the data
	# data = dict(data)

	# VIEW creating the page
	html = flask.render_template("products.html", data=data)
	# html = flask.render_template("products.html")
	return html

@app.route('/products/<product_id>')
def details(product_id):
	with open("product_db.json", "r") as f:
		data = json.load(f)
	for product in data:
		if product["ProductId"] == product_id:
			this_product = product

	html = flask.render_template("details.html", product=this_product)

	return html

# check section above if there are problem




if __name__ == "__main__":
	app.run(debug=True)
