# Exercise 1

import math
import random

class Circle ():

    def __init__(self, radius=1):
        self.radius = radius

    def circumference (self):
        return math.pi * (self.radius*2)

    def area (self):
        return math.pi * (self.radius**2)

    def definition (self):
        print("A circle is the locus of all points equidistant from a central point.")

# Exercise 2

class My_List ():

    def __init__(self, input):
        if isinstance(input, list):
            self.standard_list = input
        else:
            print("That's not a list!")

    def reverse_list(self):
        reversed_list = self.standard_list[::-1]
        return reversed_list

    def sort_list(self):
        self.standard_list.sort()
        return self.standard_list

    def random_list(self):
        randomlist = []
        for i in range (len(self.standard_list)):
            n = random.randint(1,100)
            randomlist.append(n)
        return randomlist

test = My_List([1, 2, 3, 4])

print(test.reverse_list())
print(test.sort_list())
print(test.random_list())
