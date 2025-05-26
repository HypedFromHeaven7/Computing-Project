import numpy as np
import sys
import os
import mpmath as mat
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.shapes import Shape
class RegularPolygon(Shape):
    """
    A subclass of shapes desribing regular polygons.
    
    Inputs:
    number of sides.
    side length.
    colour.
    """
    def __init__(self, n_sides=3, side_length=1.0, colour="Blue"):
        super().__init__(colour)
        self.__sides = n_sides
        self.__sidel = side_length

    def area(self):
        mat.mp.dps = 10  # Set precision to 30 decimal places
        n = mat.mpf(self.__sides)
        s = mat.mpf(self.__sidel)
        angle_rad = mat.pi() / n
        tan_angle = mat.tan(angle_rad)
        computed_area = (n * s ** 2) / (4 * tan_angle)
        return float(computed_area)
    
    def interior_angle(self):
        angle = 360/self.__sides
        return 180 - angle
    
    def can_tessellate(self):
        if np.round(360.%self.interior_angle(), 3) == 0:
            return True
        
        else:
            return False



class Pentagon(RegularPolygon):
    """
    A subclass of the superclass RegularPolygon, defining a 5 sided polygon.
    
    Inputs:
    side length.
    colour.
    """
    def __init__(self, side_length=1.0, colour="Blue"):
        super().__init__(n_sides=5, side_length=side_length, colour=colour)

class EquilateralTriangle(RegularPolygon):
    """
    A subclass of the superclass RegularPolygon, defining a 3 sided polygon.

    Inputs:
    side length.
    colour.
    """

    def __init__(self, side_length=1.0, colour="Blue"):
        super().__init__(n_sides=3, side_length=side_length, colour=colour)


class Square(RegularPolygon):
    """
    A subclass of the superclass RegularPolygon, defining a 3 sided polygon.

    Inputs:
    side length.
    colour.
    """

    def __init__(self, side_length=1, colour="Blue"):
        super().__init__(n_sides=4, side_length=side_length, colour=colour)


s = RegularPolygon(4,5)
print(s.colour())
print(s.area())