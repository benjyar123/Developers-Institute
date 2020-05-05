import json

class MenuManager():

    def __init__(self):
        self.menu = open('menu.json')
        menu_json = self.menu.read()
        self.menu.close()
        self.menu = json.loads(menu_json)


    def add_item(self, name, price):
        new_item = {"name": name, "price": price}
        self.menu["items"].append(new_item)

    def change_price(self, name, price):
        for x in range(len(self.menu["items"])):
            if self.menu["items"][x]["name"] == name:
                self.menu["items"][x]["price"] = price
                return True
        return False

    def remove_item(self, name):
        for x in range (len(self.menu["items"])):
            if self.menu["items"][x]["name"] == name:
                del self.menu["items"][x]
                return True
        return False

    def save_to_file(self):
        menu_json = json.dumps(self.menu)
        menu_file = open('menu.json', 'w+')
        menu_file.write(menu_json)


