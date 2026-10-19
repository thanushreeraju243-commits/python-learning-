class shape:
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled

class circle(shape):
    def __init__(self,color,filled ,radius):
        super().__init__(color,filled)
        self.radius = radius
class sqaure(shape):
    def __init__(self,color,filled ,side):
        super().__init__(color,filled)
        self.side = side
class triangle(shape):
    def __init__(self,color,filled ,base,height):
        super().__init__(color,filled)
        self.base = base
        self.height = height
circle1 = circle("red",True,5)
print("Circle color:", circle1.color)
print("Circle filled:", circle1.filled)
print("Circle radius:", circle1.radius)
square1 = sqaure("blue",False,4)
print("Square color:", square1.color)
print("Square filled:", square1.filled)
print("Square side:", square1.side)
triangle1 = triangle("green",True,3,6)
print("Triangle color:", triangle1.color)
print("Triangle filled:", triangle1.filled)
print("Triangle base:", triangle1.base)
print("Triangle height:", triangle1.height)
