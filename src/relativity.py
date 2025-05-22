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

        else:
            array = np.array(r)
            
            if len(array) != 3:
                raise Exception("FourVector parameter r has incorrect size")
            
            else:
                self.__r = array
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
    
    # Pure Boost Lorentz Transform
    def boost(self, beta):
        gamma = 1/np.sqrt(1 - beta**2)
        vect4 = np.append(self.__ct, self.__r)
        boostvec = np.array([[gamma, 0, 0, gamma * beta],
                             [0, 1, 0, 0],
                             [0, 0, 1, 0],
                             [gamma * beta, 0, 0, gamma]])
        transform = boostvec.dot(vect4)
        return FourVector(ct=transform[0], r=transform[1:])

    # Output format
    def __repr__(self):
        formattedlist = ", ".join(map(str, self.__r)) 
        return f"FourVector(ct={self.__ct}, r=array([{formattedlist}]))"
    
    def __str__(self):
        formattedlist = ", ".join(map(str, self.__r))
        return f'({self.__ct}, {formattedlist})'

P0 = FourVector()
P2 = FourVector()
P2.setct(99.0)
P2.setr([1,2,3])
P3 = FourVector(ct=100.3, r=[3,4,5])
P4 = P3.copy()
P4.setct(99.3)
P4 += P3
P5 = P4.inner(P3)
P20 = P2.boost(0.4)


print("###~~~###~~~###~~~")
print(f"before the boost we have P2 = {P2} with magnitude {P2.magsquare()}\nafter the boost we have P2 = {P20} with magnitude {P20.magsquare()}")
print("")
print(f"Initially we define P0 as {P0}\nAfter modifications we set P2 as {repr(P2)}")
print("")
print(P3,P4,P5)

# P6 = FourVector(ct=3, r=[3,4])