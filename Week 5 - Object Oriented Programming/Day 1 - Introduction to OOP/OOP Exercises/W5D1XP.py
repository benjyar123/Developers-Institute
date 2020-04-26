# Exercise 1

class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

cat1 = Cat("William", 10)
cat2 = Cat("Harry", 8)
cat3 = Cat("Charles", 13)

def oldest_cat(first_cat, second_cat, third_cat):
    if first_cat.age > second_cat.age and first_cat.age > third_cat.age:
        print(f"{first_cat.name} is {first_cat.age} years old and is the oldest cat.")
    elif second_cat.age > first_cat.age and second_cat.age > third_cat.age:
        print(f"{second_cat.name} is {second_cat.age} years old and is the oldest cat.")
    elif third_cat.age > first_cat.age and third_cat.age > second_cat.age:
        print(f"{third_cat.name} is {third_cat.age} years old and is the oldest cat.")
    else:
        print("There isn't a cat that is older than all the other cats.")

oldest_cat(cat1, cat2, cat3)

# Exercise 2

class Dog:
    species = 'mammal'
    def __init__(self, name_dog, height_dog):
        self.name = name_dog
        self.height = height_dog

    def talk(self):
        print("WOOF!")

    def jump(self, height_dog):
        jump_height = height_dog * 2
        return jump_height

davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Teacup", 20)

print(davids_dog.name)
print(davids_dog.height)
davids_dog.talk()
print(davids_dog.jump(davids_dog.height))

print(sarahs_dog.name)
print(sarahs_dog.height)
sarahs_dog.talk()
print(sarahs_dog.jump(sarahs_dog.height))

def jump_check(dog1, dog2):
    if dog1.jump(dog1.height) > dog2.jump(dog2.height):
        dog1.winner = True
        print(dog1.name + " is now a winner")
    elif dog2.jump(dog2.height) > dog1.jump(dog1.height):
        dog2.winner = True
        print(dog2.name + " is now a winner")
    else:
        print("No winner")

jump_check(sarahs_dog, davids_dog)

# Another Exercise 2

class Zoo ():

    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    # def __str__(self):
    #     return self.name
    #
    # def __iter__(self):
    #     return self.animals

    def add_animal (self, new_animal):
        self.animals.append(new_animal)

    def get_animals (self):
        print(self.animals)

    def sell_animal (self, animal_sold):
        print(f"Goodbye {animal_sold}, have a nice life!")
        self.animals.remove(animal_sold)

    def sort_animals (self):
        self.animals.sort()
        animal_pens = {}
        for x in range (len(self.animals)):
            animal_pens[x+1] = self.animals[x]
        return animal_pens

    def get_pen (self, penNumber):
        print(self.sort_animals()[2])

ramatGanSafari = Zoo("Ramat Gan Safari")

ramatGanSafari.add_animal("Monkey")
ramatGanSafari.add_animal("Elephant")
ramatGanSafari.add_animal("Penguin")
ramatGanSafari.add_animal("Zebra")
ramatGanSafari.add_animal("Crocodile")

ramatGanSafari.get_animals()

ramatGanSafari.sell_animal("Penguin")

ramatGanSafari.get_animals()

ramatGanSafari.sort_animals()
ramatGanSafari.get_animals()



# print(ramatGanSafari)

# print(dir(ramatGanSafari))









