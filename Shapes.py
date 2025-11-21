#   Base shape class used by Circle and Rectangle
# This class stores the common information for all shapes, the centre position x and y

from __future__ import annotations
from typing import Any

class Shape:
    def __init__(self, x: float = 0.0, y: float = 0.0) -> None:
        # Validate inputs are numeric
        if not self._is_number(x) or not self._is_number(y):
            raise TypeError("x and y must be numbers (int or float)")
        self._x = float(x)
        self._y = float(y)
        
    #  Both x & y are read only properties means we can only read them but cannot chng them directly
    # read-only x property
    @property
    def x(self) -> float:
        return self._x
    
    # read-only y property 
    @property
    def y(self) -> float:
        return self._y
    
    # Also has a translate method which moves the shape by adding a change in x and y called dx and dy
    def translate(self, dx: float, dy: float) -> None:
        # Move the shape by dx in x-direction and dy in y-direction.
        # Raises TypeError if dx or dy are not numeric.
        if not self._is_number(dx) or not self._is_number(dy):
            raise TypeError("translate dx and dy must be numbers (int or float)")
        self._x += float(dx)
        self._y += float(dy)

    # helper : this also defines a helper method to check if value is a number
    @staticmethod
    def _is_number(value: Any) -> bool:
        return isinstance(value, (int, float))
    
    # The subclasses should implement area and perimeter
    @property
    def area(self) -> float: 
        raise NotImplementedError
    
    @property
    def perimeter(self) -> float:
        raise NotImplementedError 
