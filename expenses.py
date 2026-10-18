print("enter all the expenses:")
rent = float(input("1. Rent: $"))
utilities = float(input("2. Utilities: $"))
groceries = float(input("3. Groceries: $"))
transportation = float(input("4. Transportation: $"))
entertainment = float(input("5. Entertainment: $"))
total_expenses = rent + utilities + groceries + transportation + entertainment
print("Total Expenses: $", total_expenses)
average_expenses = total_expenses / 5
print("Average Expenses: $", average_expenses)
if total_expenses > 1000:
    print("You are spending too much!")
    print(f"High expenses: ${total_expenses:.2f}")
elif total_expenses < 500:
    print("You are spending too little!")
    print(f"Low expenses: ${total_expenses:.2f}")
else:
    print("Your expenses are within a reasonable range.")
    print(f"Total expenses: ${total_expenses:.2f}")
total_expenses = max(rent, utilities, groceries, transportation, entertainment)
print("The highest expense is: $", total_expenses)
total_expenses = min(rent, utilities, groceries, transportation, entertainment)
print("The lowest expense is: $", total_expenses)
    
print("Thank you for using the expense tracker!")
