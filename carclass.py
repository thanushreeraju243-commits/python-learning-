class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print(f"The {self.year} {self.brand} {self.model} engine is starting.")
car1 = car("Toyota", "Camry", 2020)
car2 = car("Honda", "Civic", 2019)
car3 = car("Ford", "Mustang", 2021)
car1.start_engine()  # This will print "The 2020 Toyota Camry engine is starting."
car2.start_engine()  # This will print "The 2019 Honda Civic engine is starting."
car3.start_engine()  # This will print "The 2021 Ford Mustang engine is starting."
print(f"{car1.brand} {car1.model} ({car1.year})")
print(f"{car2.brand} {car2.model} ({car2.year})")
print(f"{car3.brand} {car3.model} ({car3.year})")
