# Exercise 1
#
cars = int(input("Number of cars today?"))
drivers = int(input("Number of drivers today?"))
passengers = int(input("Number of passengers today?"))

available_cars = "Available cars: " + str(cars)
registered_drivers = "Registered drivers: " + str(drivers)
passenger_capacity = "Passenger capacity: " + str(int(drivers) * 4)
unused_cars = "Unused cars: " + str(cars - drivers)
average_passengers = "Average passengers per car: " + str(passengers / drivers)

intro = "***Carpool Report***\n"

print(intro)
print(available_cars)
print(registered_drivers)
print(passenger_capacity)
print(unused_cars)
print(average_passengers)
#
# # Exercise 2
#
vowels = ['a', 'e', 'i', 'o', 'u']

letter = input("Type a letter")

if letter in vowels:
    print("That is a vowel")
elif len(letter) == 1 :
    print("That is a consonant")
#
# Exercise 3

special_characters = ["$", "#", "@"]
contains_number = False
contains_lower = False
contains_upper = False
contains_special = False
good_length = False
good_password = 0
password = input("Choose a password. Must be 6 - 12 characters long and contain at least one; lower case letter, upper case letter, number, special character ($, @ #): ")

while good_password != 5:
    for letters in range(len(password)):
        if password[letters].isdigit():
                contains_number = True
        if password[letters].islower():
                contains_lower = True
        if password[letters].isupper():
                contains_upper = True
        if password[letters] in special_characters:
                contains_special = True
    if 13 > len(password) > 5:
            good_length = True

    good_password = contains_upper + contains_lower + contains_number + contains_special + good_length

    if good_password == 5:
        break

    contains_number = False
    contains_lower = False
    contains_upper = False
    contains_special = False
    good_length = False
    password = input(
        "TRY AGAIN! Choose a password. Must be 6 - 12 characters long and contain at least one; lower case letter, upper case letter, number, special character ($, @ #): ")

print("You have successfully chosen a password. Don't forget it!")









