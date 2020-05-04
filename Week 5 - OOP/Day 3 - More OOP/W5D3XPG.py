from random import randint
import time

class ForceWielder():

    def __init__(self, name, power=0, wisdom=0):
        self.name = name
        self.power = power
        self.wisdom = wisdom
        self.harmonic_mean = (2 / ((1/self.power) + (1/self.wisdom)))

    def train(self):
        pass

    def is_jedi(self):
        pass

    def fight(self, opponent):
        if self.harmonic_mean > opponent.harmonic_mean:
            return (self.name)
        elif self.harmonic_mean < opponent.harmonic_mean:
            return (opponent.name)
        elif self.harmonic_mean == opponent.harmonic_mean:
            return ("tie")

class Jedi(ForceWielder):

    def __init__(self, name, power, wisdom):

        super().__init__(name, power, wisdom)
        if self.wisdom > self.power:
            self.lightsaber_colour = "Green"
        elif self.power > self.wisdom:
            self.lightsaber_colour = "Blue"
        elif self.power == self.wisdom:
            self.lightsaber_colour = "Violet"
        self.wisdom += 10

    def is_jedi(self):
        return True

    def train(self):
        print(self.name + " is training...\n")
        time.sleep(2)
        print(f"Pre-Training Stats\nPower: {self.power}\nWisdom: {self.wisdom}\n")
        self.wisdom += randint(10, 20)
        self.power += randint(5, 15)
        time.sleep(2)
        print(f"Post-Training Stats\nPower: {self.power}\nWisdom: {self.wisdom}\n")


class Sith(ForceWielder):

    def __init__(self, name, power, wisdom):

        super().__init__(name, power, wisdom)
        self.name = "Darth " + name
        self.lightsaber_colour = "Red"
        self.power += 10

    def is_jedi(self):
        return False

    def train(self):
        print(self.name + " is training...\n")
        time.sleep(2)
        print(f"Pre-Training Stats\nPower: {self.power}\nWisdom: {self.wisdom}\n")
        self.wisdom += randint(10, 20)
        self.power += randint(5, 15)
        time.sleep(2)
        print(f"Post-Training Stats\nPower: {self.power}\nWisdom: {self.wisdom}\n")

