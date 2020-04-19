# Fizbuzz

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

# Exercise 1

print('Hello World \n'*4)

# Exercise 2

print((99**3) * 8)

# Exercise 3

name = "Benjy"
age = 34
shoe_size = 9
info = "My name is " + name + ", I am " + str(age) + " years old, and my shoe size is " + str(shoe_size)
print(info)

# # Exercise 4
#
sentence = "I have a razer computer"
brand = "Lenovo"
print(sentence.replace("razer", brand))

# Exercise 6
#
height = input("What is your height in inches?")
if int(height) < 35 :
    print("Sorry pal, no ride for you...")
elif int(height) >= 35 :
    print("Off you go, enjoy the ride!")

# Exercise 7

number = input("give me a number")
if int(number) % 2 == 0:
    print("Even")
elif int(number) % 2 == 1:
    print("Odd")



