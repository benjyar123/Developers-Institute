num = input("Choose a number: ")
divisors = []

for x in range(1, int(num)):
    if int(num) % x == 0:
        divisors.append(x)

if sum(divisors) == int(num):
    print(num + " is a perfect number.")
else:
    print(num + " is not a perfect number")