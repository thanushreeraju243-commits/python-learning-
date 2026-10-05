class animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
class prey(animal):
    def __init__(self, name, species, speed):
        super().__init__(name, species)
        self.speed = speed

    def flee(self):
        print(f"{self.name} the {self.species} is fleeing at {self.speed} mph!")
class predator(animal):
    def __init__(self, name, species, strength):
        super().__init__(name, species)
        self.strength = strength

    def hunt(self):
        print(f"{self.name} the {self.species} is hunting with a strength of {self.strength}!")
class animal(prey, predator):
    def __init__(self, name, species, speed, strength):
        prey.__init__(self, name, species, speed)
        predator.__init__(self, name, species, strength)

    def display_info(self):
        print(f"{self.name} the {self.species} has a speed of {self.speed} mph and a strength of {self.strength}!")
rabbit = prey("Bunny", "Rabbit", 25)
wolf = predator("Wolfie", "Wolf", 80)
rabbit.flee()
wolf.hunt()