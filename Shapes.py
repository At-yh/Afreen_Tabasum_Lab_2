class Shape:
    def __init__(self, x=0, y=0):
        # save position as internal
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x  # this is only for read
    
    @property
    def y(self):
        return self._y  # this is only for read
    

    def __str__(self):
        return f"shape at ({self._x}, {self._y})"
    
    def __repr__(self):  # use it for how code will look like
        return f"shape({self._x}, {self._y})"
    
    def translate (self, dx, dy):  # to see dx and dy are numbers
        if not isinstance(dx, (int, float)):   # if dx is not a number, then will stop and give erroe.
            raise TypeError("dx must be a number")
        
        elif not isinstance(dy, (int, float)):    # if dy is not a number, then will give error
            raise TypeError("dy must be a number")
        
        self._x += dx   # update x & y with dx and dy
        self._y += dy


    # Comparison Operators
    def __eq__(self, other):   # looking if two forms are same
        return(self._x == other._x) and (self._y == other._y)   # compare the x & y values
    
    def __gt__(self, other):
        return(self._x > other._x) and (self._y > other._y)   # looking for if one form is greater than other
    
    def __lt__(self, other):   # looking for if one form is lessthan the other
        return(self._x < self._y) and (other._x < other._y)  # compare x & y values as tuples
    
    def __ge__(self, other):
        return(self._x >= other._x) and (self._y >= other._y)  # looking for if one form is greater than or equal with other    
    
    def __le__(self, other):
        return(self._x <= other._x) and (self._y <= other._y)  # looking for if one form is less than or equal with other