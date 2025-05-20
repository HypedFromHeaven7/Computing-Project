import numpy as np

class FourVector:
    """
    A class to store time and position information
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
