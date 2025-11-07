# Rectangle class that inherits from Shape

from shapes import Shape
from typing import Any
from __future__ import annotations
import math 


class Rectangle(Shape):   # Inherits from Shape class
    def __init__(self, x: float = 0.0, y: float = 0.0, width: float = 1.0, height: float = 1.0) -> None:
        super().__init__(x, y)
        # Validate width and height
        if not self._is_number(width) or not self._is_number(height):
            raise TypeError("width and height must be numbers (int or float)")
        if width < 0 or height < 0:
            raise ValueError("width and height cannot be negative")
        self._width = float(width)
        self._height = float(height)

    @property
    def width(self) -> float:
        return self._width
    
    @property
    def height(self) -> float:
        return self._height

    # read-only area property
    @property
    def area(self) -> float:
        return self._width * self._height 
    
    #  read-only perimeter property
    @property
    def perimeter(self) -> float:
        return 2 * (self._width + self._height) 
    
    #  equality: same type and same (width,height) ignoring position
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return math.isclose(self.width, other.width) and math.isclose(self.height, other.height)
    

    # Comparison operators based on area
    def _check_other_for_comapre(self, other: Any) -> None:
        from shapes import Shape as _Shape
        if not isinstance(other, _Shape):
            raise TypeError("Can only compare Rectangle with another Shape")
        
    def __lt__(self, other: Any) -> bool:
        self._check_other_for_compare(other)
        return self.area < other.area
    
    def __le__(self, other: Any) -> bool:
        self._check_other_for_compare(other)
        return self.area <= other.area
    
    def __gt__(self, other: Any) -> bool:
        self._check_other_for_compare(other)
        return self.area > other.area
    
    def __ge__(self, other: Any) -> bool:
        self._check_other_for_compare(other)
        return self.area >= other.area
    
    def is_square(self) -> bool:
        # return True if width == height (allowing small float error)
        return math.isclose(self.width, self.height)
    
    def __repr__(self) -> str:
        return f"Rectangle(x={self.x}, y={self.y}, width={self.width}, height={self.height})"
    
    def __str__(self) -> str:
        return f"Rectangle centered at ({self.x}, {self.y}) with width {self.width} and height {self.height}"