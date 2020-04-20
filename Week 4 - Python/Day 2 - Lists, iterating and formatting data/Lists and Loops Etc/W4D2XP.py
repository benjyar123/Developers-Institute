basket = ["Banana", "Apples", "Oranges", "Blueberries"];

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0, "Apples")
basket.count("Apples")
basket.clear()
print(basket)

# Exercise 1

my_fav_numbers = {2, 13, 61, 85}
my_fav_numbers.add(26)
my_fav_numbers.add(12)
my_fav_numbers.update([33, 99])
my_fav_numbers.remove(61)
your_fav_numbers = {10, 20, 30, 40}
my_fav_numbers.update(your_fav_numbers)
print(my_fav_numbers)

# Exercise 2

my_tuple = (2, 13, 61, 85)
my_list = list(my_tuple)
my_list.append(26)
my_list.append(12)
my_list.remove(61)
your_tuple = (10, 20, 30, 40)
your_list = list(your_tuple)
joint_list = my_list + your_list
my_tuple = tuple(joint_list)
print(my_tuple)

# Exercise 3

import decimal

def float_range(start, stop, step):
  while start < stop:
    yield float(start)
    start += decimal.Decimal(step)

print(list(float_range(1, 5, '0.5')))

# Exercise 4

quit = False
i = 1
toppings = []
while i < 10 and not quit:
  topping = input("Choose a topping to add to your pizza: ")
  if topping == "quit":
      print("Your pizza will be ready in 10 minutes")
      break
  else:
      toppings.append(topping)
      print("Your pizza contains: ")
      print(toppings)
  i += 1

# Exercises 5 and 7

customer_ages = []
ticket_prices = []
num_customers = int(input("Hello. How many cinema tickets would you like to buy?"))

for customers in range(num_customers):
  age = int(input("Customer number " + str(customers + 1) + ", what is your age?"))
  customer_ages.append(age)
  if 12 >= age > 2:
      price = 10
      ticket_prices.append(price)
  elif age > 12:
      price = 15
      ticket_prices.append(price)
  elif age < 3:
      price = 0
      ticket_prices.append(price)
  print("Your ticket will cost " + str(price) + " dollars.")

print("Thank you very much. That will be " + str(sum(ticket_prices)) + " dollars in total please!")

# Exercise 6

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(list):
    print(list[i])
    i+=1
#
# # Exercise 8

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
while i < len(list2):
    print(list2[i])
    i += 2

# Exercise 9

names = []
ages = []
name = None

i = 0
while i < 10 and name != "quit":
    check = input("New customer? y / n: ")
    if check == "y":
        name = input("What is your name? ")
        age = input("How old are you?")
        names.append(name)
        ages.append(age)
        i += 1
    elif check == "n":
        print("OK let's see what we've got here...")
        break

x=0
for x in range(len(names)):
    print(names[x] + " is " + ages[x] + " years old.")
    if int(ages[x]) < 16:
        print("Sorry " + names[x] + ", you are too young to watch this film!")
    elif int(ages[x]) >= 16:
        print("Enjoy the film " + names[x])



















