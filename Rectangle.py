from shapes import Shape

class Rectangle(Shape):
    def __init__(self, x=0, y=0, width = 1, height = 1):
        super().__init__(x, y)
        if not (isinstance(width, (int, float)) and isinstance(height, (int, float))):
            raise TypeError("width and height must be numbers")
        if width <= 0 or height <= 0:
            raise ValueError("width and height must be positive")
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        # check if rectangle is a square
        return self.width == self.height
    
    def __eq__(self, other):
        return isinstance(other, Rectangle) and self.area == other.area
    

    # comparison operators based on area
    def __lt__(self, other):
        return self.area < other.area
    
    def __le__(self, other):
        return self.area <= other.area
    
    def __gt__(self, other):
        return self.area > other.area
    
    def __ge__(self, other):
        return self.area >= other.area