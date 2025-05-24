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
        if self.__colour == "Red":
            Shape.num_red -= 1

        if new_col == "Red":
            Shape.num_red += 1

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
    colour.
    """

    def __init__(self, a=1.0, b=1.0, colour="Blue"):
        Shape.__init__(self,colour=colour)
        self.width = a
        self.length = b

    def area(self):
        return self.width * self.length
    
class Square(Rectangle):
    """
    A subsubclass shape.
    
    Inputs:
    side length.
    colour.
    """

    def __init__(self, a=1, colour="Blue"):
        Rectangle.__init__(self, a=a, b=a, colour=colour)




class Triangle(Shape):
    """
    A subclass shape.
    
    Inputs:
    side a length.
    side b length.
    colour.
    """

    def __init__(self, a=1.0, b=1.0, colour="Blue"):
        Shape.__init__(self, colour=colour)
        self.base = a
        self.height = b

    def area(self):
        sq = self.base * self.height
        return sq/2

class EquilateralTriangle(Triangle):
    """
    A subsubclass shape.
    
    Inputs:
    side length.
    colour.
    """

    def __init__(self, a=1.0, colour="Blue"):
        height = a * np.sqrt(3)/2 
        Triangle.__init__(self, a=a, b=height, colour=colour)



    

class Ellipse(Shape):
    """
    A subclass shape.
    
    Inputs:
    side a length.
    side b length.
    """

    def __init__(self, a=1.0, b=1.0, colour="Blue"):
        Shape.__init__(self, colour=colour)
        self.majr = a
        self.minr = b

    def area(self):
        arp = self.majr * self.minr
        return arp * np.pi


class Circle(Ellipse):
    """
    A subsubclass Shape:
    
    Inputs:
    radius.
    colour.
    """

    def __init__(self, a=1, colour="Blue"):
        Ellipse.__init__(self, a=a, b=a, colour=colour)

def redfunc(obj):
    if isinstance(obj, Shape) == True:
        obj.set("Red")
    
    return obj



s = Rectangle(3., 4.)
# s.set("Red")
print(Shape.num_red)
# g = Shape()
# f = Ellipse()
# redfunc(4)
# print(s.noshape)