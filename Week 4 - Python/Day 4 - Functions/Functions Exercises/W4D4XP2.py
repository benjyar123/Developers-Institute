# Exercise 1
current_year = 2020
current_month = 4
current_day = 22

def get_age (*args):
    years_diff = current_year - int(args[0])
    month_diff = current_month - int(args[1])
    days_diff = current_day - int(args[2])
    if month_diff < 0:
        years_diff -= 1
        month_diff += 11
    elif month_diff == 0 and days_diff < 0:
        years_diff -= 1
        month_diff += 11
    print("Your age is " + str(years_diff) + " years and " + str(month_diff) + " completed months.")
    if years_diff < 67 and sex == "m":
        print("You can not retire yet")
    elif years_diff < 62 and sex == "f":
        print("You can not retire yet")
    else:
        print("Enjoy your retirement!")

# collect user details
birth_date = input("Please enter your birth date in this format YYYY/MM/DD:")
sex = input("m/f: ")
date_details = birth_date.split("/")
for x in date_details:
    int(x)
# call function with user details as args
get_age(*date_details)

# Exercise 2
def make_shirt(size="large", message="I love Python"):
    print(f"This shirt is {size} size and contains the message: '{message}'.")
make_shirt()
make_shirt("medium")
make_shirt("small", "keep calm and carry on")

# Exercise 3
def describe_city (city, country = "Israel"):
    print(f"{city} is a city in {country}")
describe_city("Paris")
describe_city("London", "England")
describe_city("Tel Aviv")

# Exercise 4
def display_message():
    print("We are learning about functions.")
display_message()