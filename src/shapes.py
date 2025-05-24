import numpy as np

class Shape:
    """
    Super class for shapes.
    
    Inputs:
    Color of shape.
    """
    noshape = 0
    num_red = 0
    def __init__(self, colour="Blue"):
        self.__colour = colour
        Shape.noshape += 1
        if colour == "Red":
            Shape.num_red += 1


    def set(self, new_col):
        if self.__colour == "Red" and new_col != "Red":
            Shape.num_red -= 1

        elif self.__colour != "Red" and new_col == "Red":
            Shape.num_red += 1

        else:
            pass

        self.__colour = new_col
        return self

    def colour(self):
        return self.__colour

class Rectangle(Shape):
    """
    A subclass shape.
    
    Inputs:
    side a length.
    side b length.
    """

    def __init__(self, a=1.0, b=1.0):
        self.width = a
        self.length = b

    def area(self):
        return self.width * self.length
    
class Triangle(Shape):
    """
    A subclass shape.
    
    Inputs:
    side a length.
    side b length.
    """

    def __init__(self, a=1.0, b=1.0):
        self.base = a
        self.height = b

    def area(self):
        sq = self.base * self.height
        return sq/2

class Ellipse(Shape):
    """
    A subclass shape.
    
    Inputs:
    side a length.
    side b length.
    """

    def __init__(self, a=1.0, b=1.0):
        self.majr = a
        self.minr = b

    def area(self):
        arp = self.majr * self.minr
        return arp * np.pi


def redfunc(obj):
    if isinstance(obj, Shape) == True:
        obj.set("Red")
    
    return obj

s = Rectangle(3., 4.)
s.set("yellow")
g = Shape()
f = Ellipse()
redfunc(4)
print(s.noshape)