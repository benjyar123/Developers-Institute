string = input("Please type a string that is 10 characters long")

print(len(string))

while len(string) != 10:
  string = input("Please type a string that is 10 characters long")
  if len(string) == 10:
    break

first = string[0]
last = string[9]

output1 = 'The first character of your string is ' + first + ', and the last chacter of your string is ' + last
print(output1)

for x in range(10):

  print(string[0:x+1])

import random
scrambled = ''.join(random.sample(string,len(string)))

output2 = 'Your original string was: ' + string + '. This is what it might look like scrambled: ' + scrambled
print(output2)

