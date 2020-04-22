# Exercise 1
def favourite_book(title):
    print(f"My favourite book is {title}.")
favourite_book("1984")

# Exercise 2
def make_shirt(size, message):
    print(f"This shirt is {size} size and contains the message: '{message}'.")
make_shirt("medium", "hello there")
make_shirt(size="large", message="save the dolphins")

# Exercise 3
chipmunks = ["Alvin", "Simon", "Theodore"]
def show_list(list):
    for x in list:
        print(x)
show_list(chipmunks)

# Exercise 4
def make_chipmunks(list):
    for x in range (len(list)):
        list[x] += " the chipmunk"
make_chipmunks(chipmunks)
show_list(chipmunks)

# Exercise 5
def check_driver_age(age):
    # age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
check_driver_age(10)
check_driver_age(18)
check_driver_age(25)