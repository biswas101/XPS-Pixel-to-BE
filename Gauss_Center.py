# This script fit the raw XPS data using Gaussian Funtion and show the center point
# THis can be used to find true Pixel/eV, or Kintetic Energy width of Image XPS data
# You need two file to calculate the shift.
# While taking XPS data make sure to take two spectra of a same peak with 1, or 2 ev KE shift.
# This code is inspired from - https://lmfit.github.io/lmfit-py/model.html

import matplotlib.pyplot as plt
from numpy import exp, pi, sqrt

from lmfit import Model
import numpy as np
import math
from numpy import genfromtxt

data= genfromtxt('txt_database/XPS_1FA_140eV_93eV_As-3d_annealed_590C.txt',delimiter='',dtype=None, usecols=[0,1])


x=np.array(data[:, 0])
y=np.array(data[:, 1])


print("len(x): ",len(x))
center= int(len(x)/2)
print("center point:", center)
l_range= center-200
r_range= center+200

y_max= y[l_range:r_range].max()
print("Max value of Y in center region: ",y_max)

rel_index = y[l_range:r_range].argmax()
#print("Relative X index: ",rel_index)

tru_index= int(len(x)/2) -200 + rel_index
print("Approximate Pixel position:", tru_index )

# you may need to change this values for better fiting
L_value= 280
R_value= 280

x_tr = x[tru_index-L_value:tru_index+R_value]
y_tr = y[tru_index-L_value:tru_index+R_value]

def gaussian(x, amp, cen, wid):
    """1-d gaussian: gaussian(x, amp, cen, wid)"""
    return (amp / (sqrt(2*pi) * wid)) * exp(-(x-cen)**2 / (2*wid**2))


def line(x, slope, intercept):
    """a line"""
    return slope*x + intercept


mod = Model(gaussian) + Model(line)
pars = mod.make_params(amp=13, cen=tru_index, wid=10, slope=0, intercept=3.65)

result = mod.fit(y_tr, pars, x=x_tr)


comps = result.eval_components()
##plt.plot(x, y, 'b-')
##plt.plot(x_tr, comps['gaussian'], 'k--', label='Gaussian component')
##plt.plot(x_tr, comps['line'], 'r--', label='Line component')


print(result.fit_report())
#print(result.params.pretty_print())

plt.plot(x, y, 'b-')
#plt.plot(x_tr, result.init_fit, 'k--', label='initial fit')
plt.plot(x_tr, result.best_fit, 'r-', label='Gaussian fit')
plt.plot(x_tr, comps['line'], 'r--', label='Line component')
#plt.plot(x_tr, comps['gaussian'], 'k--', label='Gaussian component')

plt.legend(loc='best')
plt.show()
