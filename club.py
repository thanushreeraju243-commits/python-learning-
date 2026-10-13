def student(name,dept,usn,sem,year):
    print("Student Name:", name)
    print("Department:", dept)
    print("USN:", usn)
    print("Semester:", sem)
    print("Year:", year)
name = input("Enter your name: ")
dept = input("Enter your department: ") 
usn = input("Enter your USN: ")
sem = input("Enter your semester: ")
year = input("Enter your year: ")
student(name, dept, usn, sem, year) 
if sem == "1" or sem == "2":
    print("You are in the first year.")
    while True:
        choice = input("enter your choice (1-5): ")
        if choice == "1":
            print("techinal events")
        elif choice == "2":
            print("cultural events")
        elif choice == "3":
            print("sports events")
        elif choice == "4":
            print("workshops")
        elif choice == "5":
            print("seminars")   
        decide = input("Do you want to continue? (yes/no): ")
        if decide.lower() != "yes":
            break
elif sem == "3" or sem == "4":
    print("You are in the second year.")
    while True:
        choice = input("enter your choice (1-5): ")
        if choice == "1":
            print("coordinator: John Doe")
            print("techinal events")
        elif choice == "2":
            print("coordinator: Jane Smith")
            print("cultural events")
        elif choice == "3":
            print("coordinator: Mike Johnson")
            print("sports events")
        elif choice == "4":
            print("coordinator: Emily Davis")
            print("workshops")
        elif choice == "5":
            print("coordinator: Sarah Brown")
            print("seminars")
        decide = input("Do you want to continue? (yes/no): ")
        if decide.lower() != "yes":
            break
elif sem == "5" or sem == "6":
    print("youre not eligible for any events")
else: sem == "7" or sem == "8"
print("youre not eligible for any events")

