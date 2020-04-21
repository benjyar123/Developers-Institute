# Ex1.
fruits = input("What are your favourite fruits? Type as many as you like separated by a single space: ")
fruits_list = fruits.split()

chosen_fruit = input("What fruit would you like?")

if chosen_fruit in fruits_list:
    print("You chose one of your favorite fruits! Enjoy!")
elif chosen_fruit not in fruits_list:
    print("You chose a new fruit. I hope you enjoy it too!")

string = "Your favourite fruits are "
if len(fruits_list) > 2:
    for x in range(len(fruits_list) - 2):
        string += fruits_list[x] + ", "
    string += fruits_list[-2] + " and " + fruits_list[-1]
elif len(fruits_list) == 1:
    string = "Your favourite fruit is " + fruits_list[0]

print(string)

# Ex3
threes = [x*3 for x in range(11)]
print(threes)

# Ex6
list = [x for x in range(1500, 2700) if x%5 == 0 and x%7 == 0]
print(list)

# Some exercises skipped as repetitions of things already done or concepts I am comfortable with already