from shapes import Shape
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as RectanglePatch

class Rectangle(Shape):   # Inherits from Shape class
    def __init__(self, x=0, y=0, width = 1, height = 1):
        super().__init__(x, y)
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("width and height must be numbers")
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height

    # read-only area property
    @property
    def area(self):
        return self.width * self.height
    
    #  read-only perimeter property
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        # check if rectangle is a square
        return self.width == self.height
    
    #  equality check
    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.area == other.area
    

    # Comparison operators based on area
    def __lt__(self, other):
        return self.area < other.area
    
    def __le__(self, other):
        return self.area <= other.area
    
    def __gt__(self, other):
        return self.area > other.area
    
    def __ge__(self, other):
        return self.area >= other.area
    
    def draw(self, ax):
        #  Drawing the rectangle using matplotlib.
        rect_patch = RectanglePatch((self.x - self.width/2, self.y - self.height/2),
                                    self.width, self.height, fill=False, edgecolour = 'pink')
        ax.add_patch(rect_patch)
        ax.set_aspect('equal', adjustable = 'box')