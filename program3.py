a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
if a > b and a > c:
    print("The first number is the largest.")      
elif b > a and b > c:
    print("The second number is the largest.")
else:
    print("The third number is the largest.")   