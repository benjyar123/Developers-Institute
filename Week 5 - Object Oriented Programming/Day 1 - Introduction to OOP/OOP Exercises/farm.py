class Farm ():

    def __init__(self, name):
        self.name = name
        self.animals = {}

    def add_animal (self, animal, number=1):
        if animal in self.animals:
            self.animals[animal] += number
        else:
            new_animals = {
            animal : number,
            }
            self.animals.update(new_animals)

    def total_animals(self):
        total = 0
        for animals in self.animals:
            total += self.animals[animals]
        return total

    def get_info (self):
        print(self.name + "'s Farm")
        for animals in self.animals:
            animal_type = animals
            display_space = 15
            if self.animals[animals] > 1 and animals != "sheep":
                animal_type = animals + "s"
                display_space = 14
            gap = display_space - len(animals)
            spaces = (gap * " ")
            string = animal_type + spaces + ": " + str(self.animals[animals])
            print(string)
        print("     E-I-E-I-O!")
        print("Different types of animal: " + str(len(self.animals)))
        print("Total number of animals:   " + str(self.total_animals()))

    def get_animal_types(self):
        types = []
        for animals in self.animals:
            types.append(animals)
        return types

    def get_short_info (self):
        inventory_list = []
        for animals in self.animals:
            animal_type = animals
            if self.animals[animals] > 1 and animals != "sheep":
                animal_type = animals + "s"
            string = str(self.animals[animals]) + " " + animal_type
            inventory_list.append(string)
        sentence_middle = ""
        for x in range(len(inventory_list) - 2):
            sentence_middle += inventory_list[x] + ", "
        sentence_end = inventory_list[-2] + " and " + inventory_list[-1] + "."
        sentence_start = self.name + "'s farm has "
        full_sentence = sentence_start + sentence_middle + sentence_end
        print(full_sentence)


