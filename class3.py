class Class3:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"
print("Class3 Greeting:")
class3_instance = Class3(input("Enter your name: "))
print(class3_instance.greet())
