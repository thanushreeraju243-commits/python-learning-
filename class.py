class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        sounds = {
            "Lion": "Roar",
            "Cat": "Meow",
            "Dog": "Woof"
        }
        return sounds.get(self.species)  # Return the sound for the animal's species

animal1 = Animal("Leo", "Lion")
animal2 = Animal("Milo", "Cat")
animal3 = Animal("Max", "Dog")
sound1 = animal1.make_sound()  # This will return "Roar"
sound2 = animal2.make_sound()  # This will return "Meow"
sound3 = animal3.make_sound()  # This will return "Woof"
print(f"{animal1.name} the {animal1.species} says: {sound1}")
print(f"{animal2.name} the {animal2.species} says: {sound2}")
print(f"{animal3.name} the {animal3.species} says: {sound3}")


    
