list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)] = 200
print(list1)
# swaps 200 for 20 above
list = [1, 2, 3]
tuple = ("a", "b", "c")
set = (["hello", list, tuple])

dictionary = {"name": "Fred", "last": "Flintstone"}

print(dictionary.keys())
print(dictionary.values())
print(dictionary)

dictionary["name"] = "Wilma"
dictionary["town"] = "Bedrock"

print(dictionary.keys())
print(dictionary.values())
print(dictionary)

# append to end
# list.append(4)
# # pop by index
# list.pop(1)



# tuple[start:end:step]

print(list)

# in reverse
print(tuple[::-1])


aTuple = (10, 20, 30, 40)

a, b, c, d = aTuple
print(a)
print(b)
print(c)
print(d)

letters = ['d', 'a', 'g', 'b']
print(sorted(letters))
print(letters)
letters = sorted(letters)
print(letters)


for hamburgers in aTuple:
    print(hamburgers + 10)

r = range(10, 100, 2)

for i in r:
    print(i)

for index in range(len(aTuple)):
    print(aTuple[index])





list.extend([4, 5, 6, 7, 8])
print(list)

for index in range(len(list)):
    if index%2 == 0:
        print(list[index])
    else:
        print("no")

userNum = int(input("Number please: "))

table = range (1, 13)

for number in table:
    print(userNum*number)

for key, value in dictionary.items():
    print(key, value)

print(dictionary.items())

password = ''
while password != 'hello':
  password = input('What is the top secret password? ')

print('You guessed the right password!')




