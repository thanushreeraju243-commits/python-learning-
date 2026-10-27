class file():
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "city": self.city
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["city"])
    print("Class file defined with methods to_dict and from_dict.")
    print(input("Press Enter to continue..."))
    print("This class can be used to create instances of file objects with name, age, and city attributes.")
    