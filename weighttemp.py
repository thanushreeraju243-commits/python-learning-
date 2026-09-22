 
num = float(input("Enter the weight : "))
unit = input("Enter the unit (k for kilograms, p for pounds): ").lower()
if unit == "k":
        k = num * 2.20462
        print(f"The weight in pounds is: {round(k, 2)}")
elif unit == "p":
    p = num / 2.20462
    print(f"The weight in kilograms is: {round(p, 2)}")
else:
    print("Invalid input. Please enter 'k' for kilograms or 'p' for pounds.")

num = float(input("Enter the temperature: "))
unit = input("Enter the unit (c for Celsius, f for Fahrenheit): ").lower()
if unit == "c":
    c = (num * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {round(c, 2)}")
elif unit == "f":
    f = (num - 32) * 5/9
    print(f"The temperature in Celsius is: {round(f, 2)}")
else:
    print("Invalid input. Please enter 'c' for Celsius or 'f' for Fahrenheit.")
