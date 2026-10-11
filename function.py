def my_function(param1, param2):
    param1 = param1 * 2
    param2 = param2 + 5
    return param1, param2
print("enter the first number")
param1 = int(input())
print("enter the second number")
param2 = int(input())

result1, result2 = my_function(param1, param2)
print("Result 1:", result1)
print("Result 2:", result2)
