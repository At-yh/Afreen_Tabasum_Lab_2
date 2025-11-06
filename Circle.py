from shape import Shape   # here importing the shape class from shape.py
from math import pi       

class Circle(Shape):        # here inherits from Shape class
    def __init__(self, x=0, y=0, radius=5):
        super().__init__(x, y)
        self.radius = radius    # using the radius setter to set the radius attribute

    @property
    def area(self):
        