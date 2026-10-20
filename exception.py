num = int(input("Enter a number: "))
result = 10 / num
try:
    print("The result is:", result)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed.")
    
