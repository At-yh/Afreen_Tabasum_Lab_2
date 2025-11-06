from shapes import Shape   # here importing the shape class from shape.py
from math import pi       

class Circle(Shape):        # here inherits from Shape class
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.radius = radius    

    @property
    def area(self):
        return pi * self.radius ** 2
    
    @property
    def perimeter(self):
        return 2 * pi * self.radius
    
    def is_unit_circle(self):
        # check if circle has radius = 1 and centered at origin
        return self.radius == 1 and self.x == 0 and self.y == 0
    
    def __eq__(self, other):
        return isinstance(other, Circle) and self.radius == other.radius
    

# comparison operators based on area
def __lt__(self, other):
    return self.area < other.area

def __le__(self, other):
    return self.area <= other.area

def __gt__(self, other):
    return self.area > other.area

def __ge__(self, other):
    return self.area >= other.area
