# circle.py
# Circle class that inherits from Shape

from __future__ import annotations
import math
from shapes import Shape   # base class  
from typing import Any


class Circle(Shape):  # Inherits from Shape class
    def __init__(self, x: float = 0.0, y: float = 0.0, radius: float = 1.0) -> None:
        super().__init__(x, y)
        # Validate radius
        if not self._is_number(radius):
            raise TypeError("radius must be a number (int or float).")
        if radius < 0:
            raise ValueError("radius cannot be negative")
        self._radius = float(radius)

    # radius read-only property
    @property
    def radius(self) -> float:
        return self._radius

    # read-only area property
    @property
    def area(self) -> float:
        return math.pi * (self._radius ** 2)

    # read-only perimeter property
    @property
    def perimeter(self) -> float:
        return 2 * math.pi * self._radius

    # equality: same type and same radius (position ignored)
    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Circle):
            return False
        return math.isclose(self.radius, other.radius)

    # comparisons by area: allow comparing to other Shapes
    def _check_other_for_compare(self, other: Any) -> None:
        from shapes import Shape as _Shape
        if not isinstance(other, _Shape):
            raise TypeError("Can only compare Circle with another Shape")

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

    def is_unit_circle(self) -> bool:
        # return True if radius == 1 (allowing small float error)
        return math.isclose(self.radius, 1.0)

    # __repr__ and __str__ for helpful text
    def __repr__(self) -> str:
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self) -> str:
        return f"Circle with center ({self.x}, {self.y}) and radius {self.radius}"






# # Circle class that inherits from Shape

# from __future__ import annotations
# import math
# from shapes import Shape   # base class  
# from typing import Any 


# class Circle(Shape):        #  Inherits from Shape class
#     def __init__(self, x: float = 0.0, y: float = 0.0, radius: float =1.0) -> None:
#         super().__init__(x, y)
#         # Validate radius 
#         if not self.isnumber(radius):
#             raise TypeError("radius must be a number (int or float).")
#         if radius < 0:
#             raise ValueError("radius cannot be negative")
#         self._radius = float(radius)

#         # radius read-only property
#         @property 
#         def radius(self) -> float:
#             return self._radius    

#         # read-only area property
#         @property
#         def area(self) -> float:
#           return math.pi * (self._radius ** 2)  
    
#     # read-only perimeter property
#     @property
#     def perimeter(self) -> float:
#         return 2 * math.pi * self._radius
    
#     #  equality: same type and same radius (position ignored)
#     def __eq__(self, other: Any) -> bool:  
#         if not isinstance(other, Circle):
#             return False
#         return math.isclose(self.radius, other.radius)
    
#     # comparisons by area: allow comparing to other Shapes
#     def _check_other_for_compare(self, other: Any) -> None:
#         from shapes import Shape as _Shape 
#         if not isinstance(other, Shape):
#             raise TypeError("Can only compare Circle with another Shape")
        
#         def __lt__(self, other: Any) -> bool:
#             self._check_other_for_compare(other)
#             return self.area < other.area
        
#         def __le__(self, other: Any) -> bool:
#             self._check_other_for_compare(other)
#             return self.area <= other.area
        
#         def __gt__(self, other: Any) -> bool:
#             self._check_other_for_compare(other)
#             return self.area > other.area
        
#         def __ge__(self, other: Any) -> bool:
#             self._check_other_for_compare(other)
#             return self.area >= other.area
        
#         def is_unit_circle(self) -> bool:
#             # return Trure if radius == 1 (allowing small float error)
#             return math.isclose(self.radius, 1.0)
    
#         # __repr__and__str__for helpful text
#         def __repr__(self) -> str:
#             return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"
    
#         def __str__(self) -> str:
#             return f"Circle with center ({self.x}, {self.y}) and radius {self.radius}"