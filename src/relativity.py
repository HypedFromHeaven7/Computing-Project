import numpy as np

class FourVector:
    """
    A class to store time and position information

    Attributes:
        ct (float): Time component
        r (ndarray): Space component, given by a numpy array
    """

    def __init__(self, ct = 0, r = None):
        self.ct = ct
        if r == None:
            self.r = np.array([0,0,0])
        else:
            self.r = np.array(r)

P0 = FourVector()
P2 = FourVector(ct=99.9, r=[1, 2, 3])


print(f"Initially we define P0 as {P0.ct} {P0.r}")
print(f"After modifications we set P2 as {P2.ct} {P2.r}")

import numpy as np

class FourVector:
    """
    A class to represent spacetime four-vectors in special relativity.
    
    Attributes:
        ct (float): Time-like component (speed of light multiplied by time).
        r (ndarray): Space-like components as a NumPy array.
    """
    
    def __init__(self, ct=0, r=None):
        self.ct = ct
        self.r = np.array(r if r is not None else [0, 0, 0], dtype=float)

# Test the class
P0 = FourVector()  # Default initialization
P2 = FourVector(ct=99.9, r=[1, 2, 3])

print(P0.ct, P0.r)  # Output: 0 [0. 0. 0.]
print(P2.ct, P2.r)  # Output: 99.9 [1. 2. 3.]
