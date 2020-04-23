# I couldn't understand exactly what the daily challenge was actually asking
# I have made a function that converts integers into a binary string

def convert_to_binary(integer):
    remainders = []

    while integer > 0:
        remainders.append(integer % 2)
        integer = integer//2

    remainders.reverse()
    remainders = "".join(map(str, remainders))
    return remainders

print(convert_to_binary(int(input("Input a number to convert to binary..."))))




