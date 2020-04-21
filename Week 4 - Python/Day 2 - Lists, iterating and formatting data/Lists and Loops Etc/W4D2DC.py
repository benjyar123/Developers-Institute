i = "i"
age = input("How old are you?")
last = str(age)[-1]
candles = (i * int(last))
underscores = (13 - len(candles))
top = (" ")

if (13 - len(candles)) % 2 == 0 :
    underscores = underscores / 2
    top = ("        " + (int(underscores) * "_") + candles + (int(underscores) * "_"))
elif (13 - len(candles)) % 2 == 1 :
    underscores1 = (underscores - 1) / 2
    underscores2 = (underscores + 1) / 2
    top = ("        " + (int(underscores1) * "_") + candles + (int(underscores2) * "_"))



print(top)
print("       |:H: a:p: p:y:|")
print("    __ | ___________ | __")
print("   |^^^^^^^^^^^^^^^^^^^^^|")
print("   |  :B:i:r:t:h:d:a:y:  |")
print("   |                     |")
print("   ~~~~~~~~~~~~~~~~~~~~~~~")

