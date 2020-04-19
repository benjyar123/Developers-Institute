# Exercise 2

a = int(input("Give me a number"))
b = int(input("And another one..."))
if a > b:
    print("Hello World")

# Exercise 3
 
month = int(input("Number between 1 and 12 to represent a month..."))

if 2 < month < 6:
    print("spring")
elif 5 < month < 9:
    print("summer")
elif 8 < month < 12:
    print("autumn")
elif month == 12 or month < 3:
    print("winter")