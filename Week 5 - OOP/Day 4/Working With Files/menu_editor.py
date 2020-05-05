import menu_manager

def load_manager():
    return menu_manager.MenuManager()

my_menu_manager = load_manager()

def show_restaurant_menu(menu):
    print()
    print("Items               Prices\n")
    for x in range(len(menu.menu["items"])):
        print(menu.menu["items"][x]["name"] + (" " * (20 - len(menu.menu["items"][x]["name"]))) + str(menu.menu["items"][x]["price"]))
    print()

def show_user_menu(menu):
    menu_display = ("""
    **********************
    *     Menu           *
    * (a) Add an item    *
    * (d) Delete an item *
    * (c) Change a price *
    * (v) View the menu  *
    * (x) Exit           *
    **********************
        """)
    user_selection = "u"
    while user_selection != "x":
        print(menu_display)
        user_selection = input("Select Menu Option: ")
        if user_selection == "a":
            name = input("What item would you like to add to the menu?")
            price = input("How much will it cost?")
            my_menu_manager.add_item(name, price)
            print("The following item has been added to the menu...")
            print("Name: " + name + "    Price: " + str(price))
        elif user_selection == "d":
            item = input("What item would you like to remove from the menu?")
            check = my_menu_manager.remove_item(item)
            if check == True:
                print("The following item has been removed from the menu...")
                print("Item: " + item)
            elif check == False:
                print("That item is not in the menu...")
        elif user_selection == "c":
            item = input("Which item would you like to change the price for?")
            new_price = input("What should the new price new?")
            my_menu_manager.change_price(item, new_price)
            print("The new price for " + item + " is " + str(new_price))
        elif user_selection == "v":
            show_restaurant_menu(menu)
        elif user_selection == "x":
            my_menu_manager.save_to_file()
            print("Your menu has been saved to file")



# runs whole programme loading previously saved menu
show_user_menu(my_menu_manager)