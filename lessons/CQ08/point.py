"""Creating a point class: Challenge Question 8."""

from __future__ import annotations

__author__ = "730559378"


class Point:
    """Mutates a point and returns the new point."""
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Init function for point class."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Mutates a point."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Creates a new point."""
        return Point(self.x * factor, self.y * factor)
    
    # the __""__ format indicates a magic method, now we can overwrite str
    def __str__(self):
        """Print prettier version of our point."""
        return f"({self.x}, {self.y})"

    

a: Point = Point(1.0, 2.0)
b: Point = a.scale(3.0)

# turns the integer into a string
str(1)

# still has the functionality to make Point into a string, 
# but it is not pretty and not readable
str(a)

# we can use a Magic Method to give str a different meaning

print(str(a))
print(b)
print(f"My point is: {b}")