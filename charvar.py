user_name = input("Enter your name: ")
if len(user_name) > 12:
    print("Name is too long. Please enter a name with 12 characters or fewer.")
elif not user_name.isalpha():
    print("Invalid input. Please enter a name with only alphabetic characters.")
elif not user_name.find(" "):
    print("Invalid input. Please enter a name without spaces.")
else:
    print(f"Hello, {user_name}!")