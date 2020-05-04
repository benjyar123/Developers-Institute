# Exercise 1

class Menu_Manager ():

    def __init__(self):
        self.menu = {}

    def add_item (self, name, price, spice, gluten):
        item = {
            name : {
            "Price": price,
            "Spice": spice,
            "Gluten": gluten
        }
        }
        self.menu.update(item)

    def update_item (self, name, price, spice, gluten):
        if name in self.menu:
            item = {
                name: {
                    "Price": price,
                    "Spice": spice,
                    "Gluten": gluten
                }
            }
            self.menu.update(item)
        elif name not in self.menu:
            print("That's not on the menu.")

    def remove_item (self, name):
        if name in self.menu:
            del self.menu[name]
        elif name not in self.menu:
            print("Can't lose what you haven't got.")

my_cafe = Menu_Manager()

my_cafe.add_item("Soup", 10, "B", False)
my_cafe.add_item("Hamburger", 15, "A", True)
my_cafe.add_item("Salad", 18, "A", False)
my_cafe.add_item("French Fries", 5, "C", False)
my_cafe.add_item("Beef Bourgignon", 25, "B", True)

# Exercise 2

from farm import Farm

macdonald = Farm("McDonald")
macdonald.add_animal("cow", 5)
macdonald.add_animal("sheep")
macdonald.add_animal("sheep")
macdonald.add_animal("duck", 8)
macdonald.add_animal("pig", 15)
macdonald.add_animal("duck")
macdonald.add_animal("sheep")
macdonald.add_animal("chicken", 7)

# EXECUTION

macdonald.get_info()

macdonald.get_short_info()

