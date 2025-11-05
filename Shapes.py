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
    
    def translate (self, dx, dy):  # 