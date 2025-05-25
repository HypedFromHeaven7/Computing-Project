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
        mat.mp.dps = 30  # Set precision to 30 decimal places
        n = mat.mpf(self.__sides)
        s = mat.mpf(self.__sidel)
        angle_rad = mat.pi() / n
        tan_angle = mat.tan(angle_rad)
        computed_area = (n * s ** 2) / (4 * tan_angle)
        return float(computed_area)

        # angle_rad = np.pi / self.__sides  # Convert degrees to radians for np.tan
        # return (self.__sides * self.__sidel ** 2) / (4 * np.tan(angle_rad))

        # cons = self.__sidel * self.__sidel * self.__sides
        # mons = 4 * np.tan(np.pi/self.__sides)
        # area = cons / mons
        # return area
    

s = RegularPolygon(4,5)
print(s.colour())
print(s.area())