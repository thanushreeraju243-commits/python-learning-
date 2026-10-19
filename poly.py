from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
class square(shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
class triangle(shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class pizza(circle):
    def __init__(self,radius,toppings):
        super().__init__(radius)
        self.toppings = toppings
    def area(self):
        return super().area() + (self.toppings * 0.5)
shapes = [circle(5), square(4), triangle(3, 6), pizza(5, 3)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area()}")
    
