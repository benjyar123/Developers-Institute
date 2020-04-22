# *args and **kwargs
#
# *args inside a function is a tuple which can accept any number of arguments
# # ** key words like num1=5, num2=10, etc. can declare variables
#
# def funk (*args, **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
#
# print(funk(1, 2, 3, 4, 5, a=5, b=10))

# Order for parameters: parameters, *args, default paramteres, **kwargs

integers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(str, integers)))

print(list(filter(lambda x: x>5, integers)))

print(list(filter(lambda x: x%2, integers)))

