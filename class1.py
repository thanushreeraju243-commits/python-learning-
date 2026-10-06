class student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
print("Student Information:")
student1 = student(input("Enter student name: "), int(input("Enter student age: ")))
student1.display_info()
