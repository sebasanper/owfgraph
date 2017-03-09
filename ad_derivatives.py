__author__ = 'Sebastian Sanchez Perez-Moreno. Email: s.sanchezperezmoreno@tudelft.nl'

from ad import adnumber
from ad.admath import *
x = adnumber([1, -2, 4])
p = 9 * (x[1] * x[2] * x[0]) / (x[1] + x[2] + x[0])

print p.d(x[0])