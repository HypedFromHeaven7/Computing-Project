import numpy as np

class FourVector:
    """
    A class to store time and position information

    Attributes:
        ct (float): Time component
        r (ndarray): Space component, given by a numpy array
    """

    def __init__(self, ct = 0.0, r = None):
        self.__ct = ct
        if r == None:
            self.__r = np.array([0,0,0])
        else:
            self.__r = np.array(r)

    # Access Methods:
    def ct(self):
        return self.__ct
    
    def r(self):
        return self.__r

    # Modifier Methods 
    def setct(self, new_ct):
        self.__ct = new_ct

    def setr(self, new_r):
        self.__r = np.array(new_r)

    # Output format
    def __repr__(self):
        formattedlist = ", ".join(map(str, self.__r))
        return f"FourVector(ct={self.__ct}, r=array([{formattedlist}]))"
    
    def __str__(self):
        formattedlist = ", ".join(map(str, self.__r))
        return f'({self.__ct}, {formattedlist})'

P0 = FourVector()
P2 = FourVector()
P2.setct(99.9)
P2.setr([1,2,3])
P3 = FourVector(ct=100.3, r=[3,4,5])

print("###~~~###~~~###~~~")
print(P2.ct())
print("")
print(f"Initially we define P0 as {P0}\nAfter modifications we set P2 as {repr(P2)}")
print("")
print(P3)
