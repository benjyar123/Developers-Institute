class Hamburger():
	def __init__(self, name, price):
		self.name = name
		self.price = price
		if "deluxe" in self.name.lower():
			self.price *= 2
	def putKetchup(self):
		print(f"Your {self.name} burger is now covered in ketchup")
	def eat(self):
		print(f"That was a tasty {self.name} burger!")
	def pay(self):
		print(f"Your {self.name} burger costs ${self.price}")
	def share(self, number_of_people):
		print(f"You get 1/{number_of_people} of a {self.name} burger.")
		print(f"You will need to pay ${self.price / number_of_people}.")