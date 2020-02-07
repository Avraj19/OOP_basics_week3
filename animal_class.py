class Animal:
    # characteristics
    def __init__(self, name, legs, eyes, claws, tasty):
        self.name = name
        self.legs = legs
        self.eyes = eyes
        self.claws = claws
        self.tasty = tasty

    # behavior
    # def __init__(self):


# Create an instance of an animal object.
# an instance must be assigned to a variable
animal_1 = Animal('Randy Marsh','many', 10, 'lots of claws', 'with some cremeee fraiche, yes.')
animal_2 = Animal('Cartmen','4', 8, 'none, but I do have fangs', 'if you like fried shrimp')
print(animal_1)
print(type(animal_1))
