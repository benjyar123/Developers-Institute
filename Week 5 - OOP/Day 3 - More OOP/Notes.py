class Racecar():

    def __init__(self, model, reg_no, top_speed=0, nitros=False):
        self.model = model
        self.reg_no = reg_no
        self.top_speed = top_speed
        self.nitros = nitros

        if self.nitros:
            self.top_speed += 50

    def __str__(self):
        return self.model.capitalize()

    def __repr__(self):
        return f"This is a Racecar with registration: {self.reg_no}"

    def __call__(self):
        print(f"Vroom Vroom. The {self.model} Engines Started")

    def __gt__(self, other):
        if self.top_speed > other.top_speed:
            return True
        else:
            return False

    def drive(self, km):
        print(f"You drove the {self.model} {km} km in {km / self.top_speed} hours.")

    def race(self, other_car):
        if self > other_car:
            print(f"I am the winner")
        else:
            print(f"The {other_car.model} is the winner")


class PrintList():

    def __init__(self, my_list):
        self.mylist = my_list

    def __repr__(self):
        return str(self.mylist)

# printlist = PrintList(["a", "b", "c"])
# print(printlist.__repr__())
# printlist





# Example1

def runThreeTimes(func):
	def myWrapper():
		func()
		func()
		func()

	return myWrapper

@runThreeTimes
def sayHi():
	print("Hi!")



@runThreeTimes
def sayBye():
	print("Bye!")


# Example2

def checkIntegers(func):
	def wrapper(num1, num2):
		if isinstance(num1, int) and isinstance(num2, int):
			return func(num1, num2)
		else:
			return "Inputs must be integers"


	return wrapper


@checkIntegers
def addWithCheck(num1,num2):
	return add(num1, num2)


def add(num1, num2):
	return num1 + num2


@checkIntegers
def sub(num1, num2):
	return num1 - num2



# Example3

def title(func):
    def wrapper(*args, **kwargs):
        args = [arg.title() for arg in args]
        func(*args, **kwargs)
    return wrapper


@title
def printMessage(text):
	print(text1)


# SOME NOTES ABOUT *args AND *kwargs

# arguments: positionally passed into function
# keyword argument: can be passed in in any postions as long as they have the correcty keywords (names)

# *  variable number of arguments
# ** variable number of keyword arguments


# def max(*args)
# 	pass


# def func(**kwargs)
# 	pass


# def signup(email, password, first_name="", middle_name="", last_name="",  post_code=00000, favorite_color="Black like your heart", **favorite_foods):
# 	pass


# signup("jonny@gmail.com", "blahblah", last_name = "spiller", first_name="jon", "apples", "oranges", "bananas", "hamburgers")


# def generic_function(*arg, **kwargs):
# 	pass


# generic_function("jon", "spiller", hair="brown", eyes="green", dog="womble")
# generic_function()

def cap_decorator(func):
    def wrapper(name):
        name = name.capitalize()
        func(name)
    return wrapper

@cap_decorator
def print_my_name(name):
    print("Hello world from",name)

@cap_decorator
def say_hello_to_me(name):
    print("Hello to",name)

print_my_name("eyal")
say_hello_to_me("eyal")

import datetime

def my_decorator(inner):
    def inner_decorator(num_copy):
        print(datetime.datetime.utcnow())
        inner(int(num_copy) + 1)
        print(datetime.datetime.utcnow())
    return inner_decorator

@my_decorator
def decorated(number):
    print("This happened : " + str(number))

decorated(5)
