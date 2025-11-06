from shapes import Shape   # here importing the shape class from shape.py
from math import pi   
import matplotlib.pyplot as plt 
from matplotlib.patches import circle as CirclePatch

class Circle(Shape):        # here inherits from Shape class
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius <= 0:
            raise ValueError("radius must be positive")
        self.radius = radius    

    # read-only area property
    @property
    def area(self):
        return pi * self.radius ** 2
    
    # read-only perimeter property
    @property
    def perimeter(self):
        return 2 * pi * self.radius
    
    def is_unit_circle(self):
        return self.radius == 1 and self.x == 0 and self.y == 0
    
    #  equality check
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

def draw(self, ax):
    # Drawing the circle using matplotlib.
    circle_patch = CirclePatch((self.x, self.y), self.radius, fill=False, edgecolor = 'sky blue')
    ax.add_patch(circle_patch)
    ax.set_aspect('equal', adjustable = 'box')