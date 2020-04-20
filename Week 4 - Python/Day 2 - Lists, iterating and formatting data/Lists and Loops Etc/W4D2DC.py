i = "i"
underscore = "_"
squiggle = "~"
arrow = "^"
colon = ":"
message = "Happy Birthday"
age = input("How old are you today?")
last = age[-1]
space = " "
print(underscore * 25)
print(underscore * (12 - int(last)))
print(i * int(last))

# ___iiiii___
# |:H: a:p: p:y: |
# __ | ___________ | __
# | ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ |
# |:B: i:r: t:h: d:a: y: |
# | |
# ~~~~~~~~~~~~~~~~~~~


for letters in message[0:5]:
    print(letters)