'''
This file Normalize the XPS data into ~12 eV Kinetic energy width
But before using this file, check that, BE width is actually 12 eV or not.
You can check this, using Pixel_per_eV.py......
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

import time
start_time = time.time()

data= genfromtxt('XPS_1FA_140eV_93eV_As-3d_as_loaded_1.txt',delimiter='',dtype=None, usecols=[0,1])

fig = plt.figure()

X=np.array(data[:, 0])
Y=np.array(data[:, 1])

print(" Total Number of Pixel:", len(X))

R =np.zeros(len(X))

print(" Total Number of normalized pixel:", len(R))

BE_wdith = 12  #from Gauss_Center.py or Pixel_per_eV.py

# -- Reverse Normalization ------------------------
Xmax = X.max()
Xmin = X.min()

for i in range(len(X)):
    R[i] = BE_wdith*((Xmax - X[i])/(Xmax - Xmin))
#-----------------------------------------------

plt.xlim(BE_wdith, 0)
plt.plot(R, Y)
plt.xlabel('Binding Energy Width [eV]')
plt.ylabel('Intensity [arb. units]')

np.savetxt('XPS_1FA_140eV_93eV_As-3d_as_loaded_1_n.txt', np.c_[R,Y])
#https://stackoverflow.com/questions/15192847/saving-arrays-as-columns-with-np-savetxt

plt.show()