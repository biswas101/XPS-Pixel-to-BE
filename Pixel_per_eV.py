# THis script load two data file and one can easily find Pixel/eV
# However, this will be a rough estimate, since no fitting is involved.
# For Accurate calculation of Pixel/eV or KE width, use Gauss_Center.py

import matplotlib.pyplot as plt
import numpy as np
from numpy import genfromtxt

data_1= genfromtxt('20200304_GaAs/XPS_1FA_120eV_93eV_Ga-3d_deposition_1.txt',delimiter='',dtype=None, usecols=[0,1])
data_2= genfromtxt('20200304_GaAs/XPS_1FA_120eV_96eV_Ga-3d_deposition_1.txt',delimiter='',dtype=None, usecols=[0,1])

x1=np.array(data_1[:, 0])
y1=np.array(data_1[:, 1])

x2=np.array(data_2[:, 0])
y2=np.array(data_2[:, 1])

print("len(x1): ",len(x1))
print("len(x2): ",len(x2))

# -- Normalization :  Y1------------------------
y1_n =np.zeros(len(y1))

y1max = y1.max()
y1min = y1.min()

for i in range(len(y1)):
    y1_n[i] = 1*((y1[i] - y1min)/(y1max - y1min))
#-------------------------------------------------

# -- Normalization : Y2------------------------
y2_n =np.zeros(len(y2))

y2max = y2.max()
y2min = y2.min()

for i in range(len(y2)):
    y2_n[i] = 1*((y2[i] - y2min)/(y2max - y2min))
#-------------------------------------------------

#plt.plot(x1, y1, x2,y2, 'b-')  # regular
plt.plot(x1, y1_n, x2, y2_n, 'b-')    # Normalized

plt.xlabel('Pixel Number')
plt.ylabel('Normalized Intensity [arb. units]')


plt.text(len(x1)-200, 0.95, 'len(x1)='+'%d' % (len(x1)))
plt.text(len(x1)-200, 0.88, 'len(x2)='+'%d' % (len(x2)))

plt.show()
