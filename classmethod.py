class patient:
    count = 0
    total_age = 0
    def __init__(self, name, age, bill):
        self.name = name
        self.age = age
        self.bill = bill
        patient.count += 1
        patient.total_age += age
    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Bill: {self.bill}"
    @classmethod
    def get_average_age(cls):
        if cls.count == 0:
            return 0
        return cls.total_age / cls.count
patient1 = patient("John", 30, 1000)
patient2 = patient("Alice", 25, 1500)
print(patient1.get_details())
print(patient2.get_details())
print("Average age of patients:", patient.get_average_age())

    
    