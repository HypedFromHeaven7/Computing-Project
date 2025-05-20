import numpy as np
import seaborn as sns
import matplotlib as plt

def rtrings(rmax,nrings,multi):
    radis=rmax/nrings
    yield (0.0,0.0)
    for bn in range(0,nrings):
        rad=radis*(bn+1)
        arang=2*np.pi/multi/(bn+1)
        for tn in range(0,multi*(bn+1)):
            thet=arang*(tn)
            yield rad, thet

for n in rtrings(rmax=5, nrings=5, multi=6):
    print(n)