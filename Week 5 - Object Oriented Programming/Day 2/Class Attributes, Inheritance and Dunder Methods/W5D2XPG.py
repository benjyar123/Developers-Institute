# Exercise 1

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Persian(Cat):
    def sing(self, sounds):
        return f'{sounds}'

my_cats = []

billy = Bengal("Billy", 10)
charlie = Chartreux("Charlie", 6)
perry = Persian("Perry", 7)

my_cats.append(billy)
my_cats.append(charlie)
my_cats.append(perry)

print(my_cats)

test = Pets(billy)

print(test.animals)

test.walk()
