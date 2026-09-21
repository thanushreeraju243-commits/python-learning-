import math
radius = float(input("enter the radius of a circle"))
circumference = 2 * math.pi * radius
print(f"the circumference of the circle is {round(circumference, 2) }")
a = float(input("enter the side of a triangle"))
b = float(input("enter the other side of a triangle"))
c = math.sqrt(math.pow(a, 2) + b**2)
print(f"the hypotenuse of the triangle is {round(c, 2)}")       