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
        if r is None:
            self.__r = np.array([0,0,0])

        elif isinstance(r, np.ndarray):  
             self.__r = r
            
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

    # Copying
    def copy(self):
        return FourVector(ct=self.__ct, r=(self.__r))
    

    # Arithmatic
    def __add__(self, other):
        return FourVector(ct=(self.__ct + other.__ct), r=(self.__r + other.__r))
    
    def __sub__(self, other):
        return FourVector(ct=(self.__ct - other.__ct), r=(self.__r - other.__r))
    
    def __iadd__(self, other):
        self.__ct += other.__ct
        self.__r += other.__r
        return self
    
    def __isub__(self, other):
        self.__ct -= other.__ct
        self.__r -= other.__r
        return self
    
    # Vector Math
    def inner(self, other):
        vim = self.__ct * other.__ct
        tim = np.inner(self.__r, other.__r)
        return vim - tim
    
    def magsquare(self):
        vim = self.__ct * self.__ct
        tim = np.inner(self.__r, self.__r)
        return vim -tim

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
P4 = P3.copy()
P4.setct(99.3)
P4 += P3
P5 = P4.inner(P3)

print("###~~~###~~~###~~~")
print(P2.ct())
print("")
print(f"Initially we define P0 as {P0}\nAfter modifications we set P2 as {repr(P2)}")
print("")
print(P3,P4,P5)
