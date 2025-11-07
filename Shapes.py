#   Base shape class used by Circle and Rectangle

from __future__ import annotations
from typing import Any

class Shape:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        # Validate inputs are numbers
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x and y must be numbers (int or float).")
        # store internally with underscore to make read-only properties
        self._x = float(x)
        self._y = float(y)

    # read-only x property
    @property
    def x(self) -> float:
        return self._x
    
    # read-only y property 
    @property
    def y(self) -> float:
        return self._y
    
    def translate(self, dx: float, dy: float) -> None:
        # Move shape center by dx and dy. Raise TypeError if dx/dy not number.
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise TypeError("dx and dy must be numbers (int or float).")
        self._x += float(dx)
        self._y += float(dy)

    # area and perimeter are not implemented in base class( subclasses must provide)
    @property
    def area(self) -> float:
        raise NotImplementedError("Subclasses must implement area property.")

    @property
    def perimeter(self) -> float:
        raise NotImplementedError("Subclasses must implement perimeter property.")
    
    # Comparisons based on area. Works across different shape types.
    def _other_area(self, other: Any) -> float:
        # Helper: return other.area if available, else raise TypeError.
        if not hasattr(other, "area"):
            raise TypeError("Can only campare shapes (objects with 'area' property).")
        return other.area
    
    def __eq__(self, other: Any) -> bool:
        return NotImplemented
    
    def __lt__(self, other: Any) -> bool:
        return self.area < self._other_area(other)
    
    def __le__(self, other: Any) -> bool:
        return self.area <= self._other_area(other)
    
    def __gt__(self, other: Any) -> bool:
        return self.area > self._other_area(other)
    
    def __ge__(self, other: Any) -> bool:
        return self.area >= self._other_area(other)
    
    def __repr__(self)  -> str:
        # useful for debugging: exact class name and internal state
        return f"{self.__class__.__name__}(x={self._x}, y={self._y})"
    
    def __str__(self) -> str:
        # friendly string for users
        return f"{self.__class__.__name__} centered at ({self._x}, {self._y})"