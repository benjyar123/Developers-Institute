class Family ():

    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, name, gender, age=0, is_child=True):
        new_family_member = {'name':name,'age':age,'gender':gender,'is_child':is_child}
        self.members.append(new_family_member)

    def add_member(self, name, age, gender, is_child):
        new_family_member = {'name': name, 'age': age, 'gender': gender, 'is_child': is_child}
        self.members.append(new_family_member)

    def is_18(self, name):
        for x in range(len(self.members)):
            if name == self.members[x]["name"]:
                index = x
                if self.members[index]["age"] > 17:
                    return True
                else:
                    return False

    def represent_family(self):
        for x in range(len(self.members)):
            print(self.members[x]["name"] + " " + self.last_name + ", " + str(self.members[x]["age"]) + " year old " + self.members[x]["gender"])


smith_family = Family("Smith")

smith_family.add_member("Michael", 35, "Male", False)
smith_family.add_member("Sarah", 32, "Female", False)
smith_family.add_member("Kevin", 16, "Male", True)
smith_family.born("Emily", "Female")

smith_family.represent_family()

print(smith_family.is_18("Michael"))
print(smith_family.is_18("Sarah"))
print(smith_family.is_18("Kevin"))
print(smith_family.is_18("Emily"))

# Exercise 2

class The_Incredibles(Family):

    def add_member(self, name, age, gender, is_child, power, incredible_name):
        new_family_member = {'name': name, 'age': age, 'gender': gender, 'is_child': is_child, 'power': power, 'incredible_name': incredible_name}
        self.members.append(new_family_member)

    def use_power(self, name):
        for x in range(len(self.members)):
            if name == self.members[x]["name"]:
                index = x
                if self.members[index]["age"] > 17:
                    return self.members[index]["power"]
                else:
                    return "Too young to use powers!"

    def incredible_presentation(self):
        for x in range(len(self.members)):
            print(self.members[x]["name"] + " " + self.last_name + ", " + str(self.members[x]["age"]) + " year old " + self.members[x]["gender"])
            print("My super power is " + self.members[x]["power"] + " and my hero name is " + self.members[x]["incredible_name"])

the_incredibles = The_Incredibles("Parr")

the_incredibles.add_member("Bob", 35, "Male", False, "Strength", "Mr. Incredible")
the_incredibles.add_member("Helen", 33, "Female", False, "Elasticity", "Elastigirl")
the_incredibles.add_member("Violet", 14, "Female", True, "Invisibility", "Unknown")
the_incredibles.add_member("Dash", 10, "Male", True, "Speed", "Unknown")
print(the_incredibles.use_power("Dash"))
the_incredibles.represent_family()
the_incredibles.incredible_presentation()
the_incredibles.add_member("Jack", 0, "Male", True, "Unknown", "Unknown")

the_incredibles.incredible_presentation()