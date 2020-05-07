import flask
import json


app = flask.Flask(__name__)

@app.route('/')
def index():

	html = flask.render_template("index.html")

	return html

@app.route('/pets')
def pets():

	with open("all_pets.json", "r") as f:
		data = json.load(f)

	html = flask.render_template("pets.html", data = data)
	return html

@app.route('/cart')
def view_cart():
	with open("all_pets.json", "r") as f:
		data = json.load(f)
	with open("cart.json", "r") as f:
		cart = json.load(f)
	total = 0
	for items in cart["pets_in_cart"]:
		total += data["pets"][items]["price"]

	html = flask.render_template("cart.html", cart=cart, data=data, total=total)
	return html


@app.route('/pets/<pet_id>')
def pet_details(pet_id):
	with open("all_pets.json", "r") as f:
		data = json.load(f)
		pet = data["pets"][int(pet_id)]

	html = flask.render_template("pet.html", pet = pet)
	return html


@app.route('/pets/add_pet/<pet_id>')
def add_to_cart(pet_id):
	with open("cart.json", "r") as f:
		cart = json.load(f)
	pet_list = cart["pets_in_cart"]
	pet_list.append(int(pet_id))
	cart["pets_in_cart"] = pet_list
	with open('cart.json', 'w') as f:
		json.dump(cart, f)

	return flask.redirect(flask.url_for("pets"))

@app.route('/clear')
def clear():
	cart = {"pets_in_cart": []}
	with open('cart.json', 'w') as f:
		json.dump(cart, f)

	return flask.redirect(flask.url_for("view_cart"))

if __name__ == "__main__":
	app.run(debug=True)




