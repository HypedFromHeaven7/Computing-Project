import numpy as np

class FourVector:
    """
    A class to store time and position information

    Attributes:
        ct (float): Time component
        r (ndarray): Space component, given by a numpy array
    """

    def __init__(self, ct = 0.0, r = None):
        self.ct = ct
        if r == None:
            self.r = np.array([0,0,0])
        else:
            self.r = np.array(r)
    
    def __repr__(self):
        formattedlist = ", ".join(map(str, self.r))
        return f"FourVector(ct={self.ct}, r=array([{formattedlist}]))"
    
    def __str__(self):
        formattedlist = ", ".join(map(str, self.r))
        return f'({self.ct}, {formattedlist})'

P0 = FourVector()
P2 = FourVector(ct = 99.9, r=[1.0, 2.0, 3.0])

print("")
print(f"Initially we define P0 as {P0}\nAfter modifications we set P2 as {repr(P2)}")
print("")
